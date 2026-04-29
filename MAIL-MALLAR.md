# E-postmallar för Power Automate

Klistra in HTML-koden i **Body**-fältet i "Send an email (V2)".
Välj **Is HTML: Yes** (klicka "Show advanced options" om du inte ser det).

Dynamiska fält (blixt-ikonen): ersätt `@{triggerBody()?['faltnamn']}` med motsvarande fält från triggern.

---

## MAIL 1: Ny anmälan (False-sidan)

**Till:** `@{triggerBody()?['epost']}`
**Ämne:** `Bekräftelse — Anmälan till Byathlon 2026`

**Body (HTML):**

```html
<div style="max-width:560px; margin:0 auto; font-family:Arial, Helvetica, sans-serif; color:#25231e; line-height:1.6;">

  <!-- Header -->
  <div style="background:#36342b; padding:24px 32px; border-radius:12px 12px 0 0; text-align:center;">
    <h1 style="margin:0; color:#eae1d7; font-size:22px; font-weight:700; letter-spacing:1px;">BYATHLON 2026</h1>
    <div style="margin:12px auto 0; width:80px; height:3px; display:flex;">
      <span style="flex:1; background:#669bbc;"></span>
      <span style="flex:1; background:#efca5c;"></span>
      <span style="flex:1; background:#606c38;"></span>
    </div>
  </div>

  <!-- Body -->
  <div style="background:#ffffff; padding:32px; border:1px solid #c1bfb3; border-top:none;">

    <h2 style="margin:0 0 8px; color:#25231e; font-size:20px;">Hej @{triggerBody()?['fornamn']}!</h2>
    <p style="margin:0 0 24px; color:#595648; font-size:15px;">Din anmälan till Byathlon är mottagen. Här är dina uppgifter:</p>

    <!-- Uppgifter -->
    <table style="width:100%; border-collapse:collapse; margin:0 0 24px;">
      <tr>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#7f7a67; font-size:13px; width:120px;">Namn</td>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#25231e; font-size:14px; font-weight:600;">@{triggerBody()?['fornamn']} @{triggerBody()?['efternamn']}</td>
      </tr>
      <tr>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#7f7a67; font-size:13px;">Klass</td>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#25231e; font-size:14px; font-weight:600;">@{triggerBody()?['klass']}</td>
      </tr>
      <tr>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#7f7a67; font-size:13px;">E-post</td>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#25231e; font-size:14px;">@{triggerBody()?['epost']}</td>
      </tr>
      <tr>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#7f7a67; font-size:13px;">Telefon</td>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#25231e; font-size:14px;">@{triggerBody()?['telefon']}</td>
      </tr>
      <tr>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#7f7a67; font-size:13px;">Klubb</td>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#25231e; font-size:14px;">@{triggerBody()?['klubb']}</td>
      </tr>
    </table>

    <!-- Eventinfo -->
    <div style="background:#efeeeb; border-radius:8px; padding:20px; margin:0 0 24px;">
      <table style="width:100%; border-collapse:collapse;">
        <tr>
          <td style="padding:4px 0; color:#7f7a67; font-size:13px; width:80px;">Datum</td>
          <td style="padding:4px 0; color:#25231e; font-size:14px; font-weight:600;">Lördag 25 juli 2026</td>
        </tr>
        <tr>
          <td style="padding:4px 0; color:#7f7a67; font-size:13px;">Start</td>
          <td style="padding:4px 0; color:#25231e; font-size:14px; font-weight:600;">@{if(equals(triggerBody()?['klass'],'Motion'),'Kl. 17:10','Kl. 17:00')}</td>
        </tr>
        <tr>
          <td style="padding:4px 0; color:#7f7a67; font-size:13px;">Plats</td>
          <td style="padding:4px 0; color:#25231e; font-size:14px; font-weight:600;">Sidensjö</td>
        </tr>
        <tr>
          <td style="padding:4px 0; color:#7f7a67; font-size:13px;">Samling</td>
          <td style="padding:4px 0; color:#25231e; font-size:14px;">Från kl. 16:00</td>
        </tr>
      </table>
    </div>

    <!-- Checklista -->
    <h3 style="margin:0 0 8px; color:#36342b; font-size:15px;">Ta med till tävlingen:</h3>
    <table style="margin:0 0 24px; border-collapse:collapse;">
      <tr><td style="padding:3px 8px 3px 0; color:#606c38; font-size:14px;">&#10003;</td><td style="padding:3px 0; color:#474439; font-size:14px;">Cykel &amp; hjälm <span style="color:#a41e1e; font-size:12px; font-weight:600;">(obligatoriskt)</span></td></tr>
      <tr><td style="padding:3px 8px 3px 0; color:#606c38; font-size:14px;">&#10003;</td><td style="padding:3px 0; color:#474439; font-size:14px;">Badkläder &amp; handduk</td></tr>
      <tr><td style="padding:3px 8px 3px 0; color:#606c38; font-size:14px;">&#10003;</td><td style="padding:3px 0; color:#474439; font-size:14px;">Löparskor</td></tr>
      <tr><td style="padding:3px 8px 3px 0; color:#606c38; font-size:14px;">&#10003;</td><td style="padding:3px 0; color:#474439; font-size:14px;">Vattenflaska</td></tr>
    </table>

    <p style="margin:0; color:#595648; font-size:14px;">Vi ses i Sidensjö!</p>

  </div>

  <!-- Footer -->
  <div style="background:#efeeeb; padding:20px 32px; border-radius:0 0 12px 12px; border:1px solid #c1bfb3; border-top:none; text-align:center;">
    <p style="margin:0 0 4px; color:#7f7a67; font-size:12px;">Arrangör: By intresseförening</p>
    <p style="margin:0; color:#a29d8b; font-size:11px;">Vid frågor, svara på detta mejl.</p>
  </div>

</div>
```

---

## MAIL 2: Uppdaterad anmälan (True-sidan)

**Till:** `@{triggerBody()?['epost']}`
**Ämne:** `Anmälan uppdaterad — Byathlon 2026`

**Body (HTML):**

```html
<div style="max-width:560px; margin:0 auto; font-family:Arial, Helvetica, sans-serif; color:#25231e; line-height:1.6;">

  <!-- Header -->
  <div style="background:#36342b; padding:24px 32px; border-radius:12px 12px 0 0; text-align:center;">
    <h1 style="margin:0; color:#eae1d7; font-size:22px; font-weight:700; letter-spacing:1px;">BYATHLON 2026</h1>
    <div style="margin:12px auto 0; width:80px; height:3px; display:flex;">
      <span style="flex:1; background:#669bbc;"></span>
      <span style="flex:1; background:#efca5c;"></span>
      <span style="flex:1; background:#606c38;"></span>
    </div>
  </div>

  <!-- Body -->
  <div style="background:#ffffff; padding:32px; border:1px solid #c1bfb3; border-top:none;">

    <h2 style="margin:0 0 8px; color:#25231e; font-size:20px;">Hej @{triggerBody()?['fornamn']}!</h2>
    <p style="margin:0 0 24px; color:#595648; font-size:15px;">Din anmälan har uppdaterats med dina senaste uppgifter:</p>

    <!-- Uppgifter -->
    <table style="width:100%; border-collapse:collapse; margin:0 0 24px;">
      <tr>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#7f7a67; font-size:13px; width:120px;">Namn</td>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#25231e; font-size:14px; font-weight:600;">@{triggerBody()?['fornamn']} @{triggerBody()?['efternamn']}</td>
      </tr>
      <tr>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#7f7a67; font-size:13px;">Klass</td>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#25231e; font-size:14px; font-weight:600;">@{triggerBody()?['klass']}</td>
      </tr>
      <tr>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#7f7a67; font-size:13px;">E-post</td>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#25231e; font-size:14px;">@{triggerBody()?['epost']}</td>
      </tr>
      <tr>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#7f7a67; font-size:13px;">Telefon</td>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#25231e; font-size:14px;">@{triggerBody()?['telefon']}</td>
      </tr>
      <tr>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#7f7a67; font-size:13px;">Klubb</td>
        <td style="padding:10px 12px; border-bottom:1px solid #dfded8; color:#25231e; font-size:14px;">@{triggerBody()?['klubb']}</td>
      </tr>
    </table>

    <!-- Info-ruta -->
    <div style="background:#fdf9ec; border-left:3px solid #efca5c; padding:12px 16px; border-radius:4px; margin:0 0 24px;">
      <p style="margin:0; color:#664f0a; font-size:13px;">
        <strong>OBS:</strong> Denna anmälan ersätter din tidigare registrering. Inga andra ändringar behövs.
      </p>
    </div>

    <!-- Eventinfo -->
    <div style="background:#efeeeb; border-radius:8px; padding:20px; margin:0 0 24px;">
      <table style="width:100%; border-collapse:collapse;">
        <tr>
          <td style="padding:4px 0; color:#7f7a67; font-size:13px; width:80px;">Datum</td>
          <td style="padding:4px 0; color:#25231e; font-size:14px; font-weight:600;">Lördag 25 juli 2026</td>
        </tr>
        <tr>
          <td style="padding:4px 0; color:#7f7a67; font-size:13px;">Start</td>
          <td style="padding:4px 0; color:#25231e; font-size:14px; font-weight:600;">@{if(equals(triggerBody()?['klass'],'Motion'),'Kl. 17:10','Kl. 17:00')}</td>
        </tr>
        <tr>
          <td style="padding:4px 0; color:#7f7a67; font-size:13px;">Plats</td>
          <td style="padding:4px 0; color:#25231e; font-size:14px; font-weight:600;">Sidensjö</td>
        </tr>
      </table>
    </div>

    <!-- Checklista -->
    <h3 style="margin:0 0 8px; color:#36342b; font-size:15px;">Påminnelse — ta med:</h3>
    <table style="margin:0 0 24px; border-collapse:collapse;">
      <tr><td style="padding:3px 8px 3px 0; color:#606c38; font-size:14px;">&#10003;</td><td style="padding:3px 0; color:#474439; font-size:14px;">Cykel &amp; hjälm <span style="color:#a41e1e; font-size:12px; font-weight:600;">(obligatoriskt)</span></td></tr>
      <tr><td style="padding:3px 8px 3px 0; color:#606c38; font-size:14px;">&#10003;</td><td style="padding:3px 0; color:#474439; font-size:14px;">Badkläder &amp; handduk</td></tr>
      <tr><td style="padding:3px 8px 3px 0; color:#606c38; font-size:14px;">&#10003;</td><td style="padding:3px 0; color:#474439; font-size:14px;">Löparskor</td></tr>
      <tr><td style="padding:3px 8px 3px 0; color:#606c38; font-size:14px;">&#10003;</td><td style="padding:3px 0; color:#474439; font-size:14px;">Vattenflaska</td></tr>
    </table>

    <p style="margin:0; color:#595648; font-size:14px;">Vi ses i Sidensjö!</p>

  </div>

  <!-- Footer -->
  <div style="background:#efeeeb; padding:20px 32px; border-radius:0 0 12px 12px; border:1px solid #c1bfb3; border-top:none; text-align:center;">
    <p style="margin:0 0 4px; color:#7f7a67; font-size:12px;">Arrangör: By intresseförening</p>
    <p style="margin:0; color:#a29d8b; font-size:11px;">Vid frågor, svara på detta mejl.</p>
  </div>

</div>
```

---

## Färgreferens (hemsidans palett)

| Användning | Färg | Hex |
|---|---|---|
| Header-bakgrund | DGreenC-700 | `#36342b` |
| Header-text | TanC-100 | `#eae1d7` |
| Brödtext | DGreenC-800 | `#25231e` |
| Sekundärtext | DGreenC-500 | `#595648` |
| Etikett/label | DGreenC-400 | `#7f7a67` |
| Linje/border | DGreenC-100 | `#dfded8` |
| Info-bakgrund | DGreenC-50 | `#efeeeb` |
| Checkmark-grön | GreenC-500 | `#606c38` |
| Varnings-gul (bg) | YellowC-50 | `#fdf9ec` |
| Varnings-gul (text) | YellowC-800 | `#664f0a` |
| Varnings-gul (kant) | YellowC-400 | `#efca5c` |
| Hjälm-varning | RedC-600 | `#a41e1e` |
| Tri-bar blå | BlueC-500 | `#669bbc` |
| Tri-bar gul | YellowC-400 | `#efca5c` |
| Tri-bar grön | GreenC-500 | `#606c38` |

---

# Sponsor-mail (manuella utskick)

Dessa mail skickas **inte** via Power Automate utan kopieras in i Outlook/Gmail
och anpassas per företag. Två nivåer erbjuds: **Huvudsponsor** och **Sponsor**.

Fyll i fält inom `{{...}}` per mottagare. Ta bort fält du inte använder.

## Sponsorpaket — översikt

**Huvudsponsor**
- Stor logga i sektionen "Huvudsponsorer" på byathlon.se
- Logga med i hero-raden "I samarbete med" på startsidan
- Omnämnande i deltagar-mail (bekräftelse + utskick före och efter event)
- Möjlighet till banderoll/skylt i målområdet
- Möjlighet att vara på plats med eget bord under eventet
- Bidrag: produkter till goodiebag och/eller pengainsats efter överenskommelse

**Sponsor**
- Logga i sektionen "Sponsorer" på byathlon.se
- Omnämnande i goodiebag-flyer
- Bidrag: produkter till goodiebag (ca 150 deltagare) och/eller pengainsats

---

## MAIL: Förfrågan – Huvudsponsor

**Till:** `{{epost}}`
**Ämne:** `Huvudsponsor till Byathlon 2026 — norrländsk premiär i Sidensjö`

**Body (klartext):**

```
Hej!

Den 25 juli 2026 är det premiär för Byathlon —
ett triathlon-evenemang med simning, cykling och löpning som arrangeras av By Intresseförening under Sidensjöveckan. Start och målgång sker vid By badplats.
Eventet vänder sig till både nybörjare och erfarna
multisportare då anmälan sker till två olika distanser.

Byathlon arrangeras av en lokal
intresseförening i Sidensjö. För oss representerar ni på {{företagsnamn}} {{personlig vinkel — t.ex. "den norrländska andan", "kvalitet hos motionssvensken", "återhämtning på riktigt"}}. Jag hör av mig till er på {{företagsnamn}} eftersom vi ser er som en given samarbetspartner, gärna som huvudsponsor, i premiären av Byathlon.

Som HUVUDSPONSOR får ni:
 • Stor logga på byathlon.se under rubriken "Huvudsponsorer"
 • Logga på startsidan under rubriken "I samarbete med"
 • Omnämnande i alla deltagar-mail (bekräftelse + utskick före/efter event)
 • Plats för banderoll/skylt vid målområdet
 • Möjlighet att vara på plats med eget bord under eventet

Vi söker ett ekonomiskt bidrag och/eller produkter till en goodiebag som deltagarna kommer att få när de går i mål.

Låter detta intressant? Jag berättar gärna mer
över telefon, men för att kunna börja marknadsföra eventet och ge våra sponsorer så mycket synlighet som möjligt behöver vi er återkoppling snarast.

Förhandsvisning av sidan: https://{{länk-till-sidan}}

Tack på förhand!

Vänliga hälsningar
Hugo Kjellsson
By Intresseförening — Byathlon 2026
hugo@kjellsson.nu | {{ditt-telefonnummer}}
byathlon.se
```

---

## MAIL: Förfrågan – Sponsor (goodiebag)

**Till:** `{{epost}}`
**Ämne:** `Sponsorsamarbete till Byathlon 2026 — produkter till goodiebag`

**Body (klartext):**

```
Hej!

Den 25 juli 2026 är det premiär för Byathlon —
ett triathlon-evenemang med simning, cykling och löpning som arrangeras av By Intresseförening under Sidensjöveckan. Start och målgång sker vid By badplats.
Eventet vänder sig till både nybörjare och erfarna
multisportare då anmälan sker till två olika distanser.

Byathlon arrangeras av en lokal
intresseförening i Sidensjö. För oss representerar ni på {{företagsnamn}} {{personlig vinkel — t.ex. "perfekt efter målgång", "stark närvaro i Norrland"}}. Jag hör av mig till er på {{företagsnamn}} eftersom vi ser er som en given samarbetspartner i premiären av Byathlon.

Som SPONSOR får ni:
 • Logga på byathlon.se under rubriken "Sponsorer"
 • Omnämnande i goodiebag-flyern som följer med varje deltagare
 • Möjlighet att lägga med eget reklammaterial (flyers, prover, klistermärken) i goodiebagen

Vi söker ett ekonomiskt bidrag och/eller produkter till en goodiebag som deltagarna kommer att få när de går i mål — t.ex. ca {{antal}} st {{produkt}}. Har ni något annat förslag är vi öppna för det också.

Låter detta intressant? Jag berättar gärna mer
över telefon, men för att kunna börja marknadsföra eventet och ge våra sponsorer så mycket synlighet som möjligt behöver vi er återkoppling snarast.

Förhandsvisning av sidan: https://{{länk-till-sidan}}

Tack på förhand!

Vänliga hälsningar
Hugo Kjellsson
By Intresseförening — Byathlon 2026
hugo@kjellsson.nu | {{ditt-telefonnummer}}
byathlon.se
```

---

## MAIL: Påminnelse (efter ~5 vardagar utan svar)

**Ämne:** `Re: {{ursprungsämne}}`

**Body (klartext):**

```
Hej {{förnamn}},

Jag hörde av mig förra veckan om sponsorsamarbete kring Byathlon
den 25 juli — bara en vänlig knuff ifall mailet hamnat fel.

Säg till om det är något ni vill veta mer om, eller om vi ska prata
kort i telefon.

Vänliga hälsningar
Hugo Kjellsson
hugo@kjellsson.nu
```

---

## Tips för effektiv hantering

1. **Spårning** — använd ett kalkylblad med kolumner:
   `Företag | Kategori | Kontakt | E-post | Status | Skickat | Påminnelse | Svar | Logga mottagen?`
2. **Vattenfall** — fråga förstaval i varje produktkategori först, vänta
   5–7 vardagar, sen andraval. Undviker att konkurrenter hamnar samtidigt.
3. **Påminnelse** — max två. Sen släpp.
4. **Logga** — be om logga i samma svar där de tackar ja, så slipper du
   en separat mailrunda. PNG med transparent bakgrund är bäst.
5. **Deadline** — sätt 1 juni 2026 som sista svarsdag i mailet. Då vet
   företaget att det brådskar och du får planeringsbara svar.

