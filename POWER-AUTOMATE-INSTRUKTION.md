# Power Automate — Byathlon Anmälningsflöde

## Översikt

```
Hemsidan (anmalan.html)
    │
    ▼  POST JSON
Power Automate webhook
    │
    ├─► Steg 1: Ta emot data
    ├─► Steg 2: Kolla dubbletter i Excel
    ├─► Steg 3a: Om ny → Spara i Excel + Skicka bekräftelse
    └─► Steg 3b: Om dubblett → Skicka "redan anmäld"-mejl
```

---

## Förberedelse: Skapa Excel-filen

1. Gå till **OneDrive** (online)
2. Skapa en ny Excel-fil: `Byathlon_Anmalningar.xlsx`
3. I **Blad1**, skapa en **tabell** (markera rad 1, Infoga → Tabell):

| Förnamn | Efternamn | Epost | Telefon | Klubb | Klass | Meddelande | Tidpunkt |
|---------|-----------|-------|---------|-------|-------|------------|----------|

4. Namnge tabellen `Anmalningar` (klicka på tabellen → Tabelldesign → Tabellnamn)
5. **Stäng filen** (jobba alltid via Excel Online, inte desktop-appen)

---

## Steg-för-steg i Power Automate

### TRIGGER: "When an HTTP request is received"

1. Gå till https://make.powerautomate.com
2. Skapa nytt flöde → **Instant cloud flow** → hoppa över → **When an HTTP request is received**
3. Metod: **POST**
4. Klistra in detta JSON-schema:

```json
{
  "type": "object",
  "properties": {
    "fornamn":    { "type": "string" },
    "efternamn":  { "type": "string" },
    "epost":      { "type": "string" },
    "telefon":    { "type": "string" },
    "klubb":      { "type": "string" },
    "klass":      { "type": "string" },
    "meddelande": { "type": "string" },
    "tidpunkt":   { "type": "string" }
  }
}
```

5. **Spara** flödet en gång → kopiera URL:en som genereras → klistra in den i `anmalan.html` (WEBHOOK_URL)

---

### STEG 1: Initiera variabel — "lowercase_epost"

- Åtgärd: **Initialize variable**
- Namn: `lowercase_epost`
- Typ: String
- Värde: `toLower(triggerBody()?['epost'])`

*(Detta normaliserar e-post så Hugo@Epost.se och hugo@epost.se blir samma)*

---

### STEG 2: Sök dubbletter i Excel

- Åtgärd: **List rows present in a table** (Excel Online)
- Plats: OneDrive
- Fil: `Byathlon_Anmalningar.xlsx`
- Tabell: `Anmalningar`
- Filterförfrågan: `tolower(Epost) eq '@{variables('lowercase_epost')}' and tolower(Förnamn) eq '@{toLower(triggerBody()?['fornamn'])}'`

*(Kollar om det redan finns en rad med samma e-post + förnamn)*

---

### STEG 3: Villkor — "Finns dubbletter?"

- Åtgärd: **Condition**
- Villkor: `length(body('List_rows_present_in_a_table')?['value'])` **is greater than** `0`

---

### STEG 3a: Om NEJ (ny anmälan) →

#### 3a-1: Lägg till rad i Excel

- Åtgärd: **Add a row into a table** (Excel Online)
- Fil: `Byathlon_Anmalningar.xlsx`
- Tabell: `Anmalningar`
- Fält-mappning:

| Excel-kolumn | Värde från trigger |
|---|---|
| Förnamn | `triggerBody()?['fornamn']` |
| Efternamn | `triggerBody()?['efternamn']` |
| Epost | `variables('lowercase_epost')` |
| Telefon | `triggerBody()?['telefon']` |
| Klubb | `triggerBody()?['klubb']` |
| Klass | `triggerBody()?['klass']` |
| Meddelande | `triggerBody()?['meddelande']` |
| Tidpunkt | `triggerBody()?['tidpunkt']` |

#### 3a-2: Skicka bekräftelsemejl

- Åtgärd: **Send an email (V2)** (Office 365 Outlook)
- Till: `variables('lowercase_epost')`
- Ämne: `Bekräftelse — Anmälan till Byathlon 2026`
- Brödtext (HTML):

```html
<h2>Hej @{triggerBody()?['fornamn']}!</h2>

<p>Din anmälan till <strong>Byathlon 2026</strong> är mottagen.</p>

<table style="border-collapse:collapse; margin:16px 0;">
  <tr>
    <td style="padding:6px 16px 6px 0; color:#666;">Klass</td>
    <td style="padding:6px 0; font-weight:bold;">@{triggerBody()?['klass']}</td>
  </tr>
  <tr>
    <td style="padding:6px 16px 6px 0; color:#666;">Namn</td>
    <td style="padding:6px 0;">@{triggerBody()?['fornamn']} @{triggerBody()?['efternamn']}</td>
  </tr>
  <tr>
    <td style="padding:6px 16px 6px 0; color:#666;">Datum</td>
    <td style="padding:6px 0;">Lördag 25 juli 2026</td>
  </tr>
  <tr>
    <td style="padding:6px 16px 6px 0; color:#666;">Start</td>
    <td style="padding:6px 0;">@{if(equals(triggerBody()?['klass'],'Motion'),'Kl. 16:10','Kl. 16:00')}</td>
  </tr>
  <tr>
    <td style="padding:6px 16px 6px 0; color:#666;">Plats</td>
    <td style="padding:6px 0;">Sidensjö</td>
  </tr>
</table>

<h3>Glöm inte att ta med:</h3>
<ul>
  <li>Cykel &amp; hjälm (obligatoriskt!)</li>
  <li>Badkläder &amp; handduk</li>
  <li>Löparskor</li>
  <li>Vattenflaska</li>
</ul>

<p style="margin-top:24px; color:#666; font-size:13px;">
  Arrangör: By intresseförening<br>
  Vid frågor, svara på detta mejl.
</p>
```

#### 3a-3: Svara webben (200 OK)

- Åtgärd: **Response**
- Statuskod: `200`
- Body: `{"status":"ok"}`

---

### STEG 3b: Om JA (dubblett) → Uppdatera befintlig rad

#### 3b-1: Uppdatera raden i Excel

- Åtgärd: **Update a row** (Excel Online)
- Fil: `Byathlon_Anmalningar.xlsx`
- Tabell: `Anmalningar`
- Nyckelkolumn: Använd rad-ID:t från "List rows"-resultatet: `first(body('List_rows_present_in_a_table')?['value'])?['__PowerAppsId__']`
- Fält-mappning (samma som steg 3a-1):

| Excel-kolumn | Värde från trigger |
|---|---|
| Förnamn | `triggerBody()?['fornamn']` |
| Efternamn | `triggerBody()?['efternamn']` |
| Epost | `variables('lowercase_epost')` |
| Telefon | `triggerBody()?['telefon']` |
| Klubb | `triggerBody()?['klubb']` |
| Klass | `triggerBody()?['klass']` |
| Meddelande | `triggerBody()?['meddelande']` |
| Tidpunkt | `triggerBody()?['tidpunkt']` |

#### 3b-2: Skicka "anmälan uppdaterad"-mejl

- Åtgärd: **Send an email (V2)**
- Till: `variables('lowercase_epost')`
- Ämne: `Anmälan uppdaterad — Byathlon 2026`
- Brödtext:

```html
<h2>Hej @{triggerBody()?['fornamn']}!</h2>
<p>Din anmälan till <strong>Byathlon 2026</strong> har uppdaterats med dina senaste uppgifter.</p>

<table style="border-collapse:collapse; margin:16px 0;">
  <tr>
    <td style="padding:6px 16px 6px 0; color:#666;">Klass</td>
    <td style="padding:6px 0; font-weight:bold;">@{triggerBody()?['klass']}</td>
  </tr>
  <tr>
    <td style="padding:6px 16px 6px 0; color:#666;">Namn</td>
    <td style="padding:6px 0;">@{triggerBody()?['fornamn']} @{triggerBody()?['efternamn']}</td>
  </tr>
  <tr>
    <td style="padding:6px 16px 6px 0; color:#666;">Datum</td>
    <td style="padding:6px 0;">Lördag 25 juli 2026</td>
  </tr>
  <tr>
    <td style="padding:6px 16px 6px 0; color:#666;">Start</td>
    <td style="padding:6px 0;">@{if(equals(triggerBody()?['klass'],'Motion'),'Kl. 16:10','Kl. 16:00')}</td>
  </tr>
</table>

<p style="color:#666; font-size:13px;">
  Vid frågor, svara på detta mejl.<br>
  Arrangör: By intresseförening
</p>
```

#### 3b-3: Svara webben (200 OK)

- Åtgärd: **Response**
- Statuskod: `200`
- Body: `{"status":"duplicate"}`

*(Vi svarar 200 även vid dubblett så att användaren ändå hamnar på bekräftelsesidan — de får info via mejl att de redan är anmälda)*

---

## Flödesöversikt (visuellt)

```
┌─────────────────────────────────┐
│  TRIGGER: HTTP POST             │
│  (tar emot JSON från hemsidan)  │
└──────────────┬──────────────────┘
               ▼
┌─────────────────────────────────┐
│  Initiera variabel              │
│  lowercase_epost = toLower()    │
└──────────────┬──────────────────┘
               ▼
┌─────────────────────────────────┐
│  Lista rader i Excel            │
│  Filter: epost + förnamn        │
└──────────────┬──────────────────┘
               ▼
        ┌──────┴──────┐
        │  Dubblett?  │
        └──┬───────┬──┘
       NEJ │       │ JA
           ▼       ▼
    ┌──────────┐ ┌───────────────┐
    │ Spara i  │ │ Uppdatera rad │
    │ Excel    │ │ i Excel       │
    ├──────────┤ ├───────────────┤
    │ Bekräft. │ │ "Uppdaterad"  │
    │ mejl     │ │ mejl          │
    ├──────────┤ ├───────────────┤
    │ Response │ │ Response 200  │
    │ 200 "ok" │ │ "duplicate"   │
    └──────────┘ └───────────────┘
         │              │
         ▼              ▼
    bekraftelse    redan-anmald
      .html           .html
```

---

## Viktiga varningar

1. **Ändra ALDRIG kolumnnamnen i Excel** utan att uppdatera Power Automate
2. **Öppna Excel via webbläsaren** (Excel Online), inte desktop-appen, för att undvika fillåsning
3. **Testa flödet** genom att skicka en testanmälan från hemsidan
4. **Kolla Flödeskörningar** (Run history) i Power Automate om något går fel
5. **Webhook-URL:en** innehåller en signatur (`sig=...`) — dela den inte publikt
