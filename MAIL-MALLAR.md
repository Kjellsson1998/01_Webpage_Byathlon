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
          <td style="padding:4px 0; color:#25231e; font-size:14px; font-weight:600;">Onsdag 29 juli 2026</td>
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
          <td style="padding:4px 0; color:#25231e; font-size:14px; font-weight:600;">Onsdag 29 juli 2026</td>
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
