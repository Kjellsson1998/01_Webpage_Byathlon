# E-postmallar för Power Automate

Klistra in HTML-koden i **Body**-fältet i "Send an email (V2)".
Välj **Is HTML: Yes** (klicka "Show advanced options" om du inte ser det).

Dynamiska fält (blixt-ikonen): ersätt `@{triggerBody()?['faltnamn']}` med motsvarande fält från triggern.

## Förutsättningar i flödet

Mailen nedan refererar till följande som måste finnas i Power Automate-flödet **före** "Send an email"-steget:

| Referens                              | Vad är det                                            | Hur skapas det                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `triggerBody()?['alder']`             | Användarens åldersval ("18 eller äldre" / "Under 18") | Ny `alder`-property i Parse JSON-schemat                                                                                                                                                                                                                                                                                                                                                              |
| `base64(body('HTTP'))`                | Base64-encoded PNG av Swish QR-koden                  | HTTP-action POST mot `https://mpc.getswish.net/qrg-swish/api/v1/prefilled` (action heter "HTTP" i flödet). **OBS:** `body('HTTP')` ensamt returnerar rå binär — alltid wrappa med `base64()` när det ska in i ett HTML img-tag eller en JSON-sträng.                                                                                                                                                  |
| `variables('System_SwishLink')`       | Klickbar Swish-länk (`swish://payment?data=...`)      | Initialize variable som bygger officiell Swish-deeplink: `swish://payment?data=@{encodeUriComponent(concat('{"version":1,"payee":{"value":"1235867544","editable":false},"amount":{"value":300,"editable":true},"message":{"value":"', variables('System_SwishMeddelande'), '","editable":false}}'))}`. **OBS:** `amount.value` är ett nummer (300), inte en sträng ("300") — Swish-appen kräver det. |
| `variables('System_SwishMeddelande')` | Förinskrivet meddelande i Swish                       | Initialize variable: `concat('Byathlon - ', fornamn, ' ', efternamn)`                                                                                                                                                                                                                                                                                                                                 |

Se `POWER-AUTOMATE-INSTRUKTION.md` för detaljerade steg.

---

## MAIL 1: Ny anmälan (False-sidan)

**Till:** `@{triggerBody()?['epost']}`
**Ämne:** `Bekräftelse — Anmälan till Byathlon 2026`

**Body (HTML):**

```html
<table
  cellpadding="0"
  cellspacing="0"
  border="0"
  style="mso-table-lspace: 0pt;
    mso-table-rspace: 0pt;
    font-family: Arial, Helvetica, sans-serif;"
>
  <tbody>
    <tr>
      <td style="background: #f5f4ef; padding: 24px 16px">
        <!-- Yttre mail-container (max 600px) -->
        <table
          cellpadding="0"
          cellspacing="0"
          border="0"
          style="mso-table-lspace: 0pt;
          mso-table-rspace: 0pt;
          max-width: 600px;
          width: 100%;
          background: #ffffff;
          border: 1px solid #c1bfb3;"
        >
          <!-- Header -->
          <tbody>
            <tr>
              <td
                style="background: #36342b; padding: 28px 32px; text-align: center"
              >
                <div
                  style="margin: 0 0 12px;
                color: #eae1d7;
                font-size: 22px;
                font-weight: bold;
                letter-spacing: 1px;"
                >
                  <a
                    href="https://byathlon.se"
                    style="color: #eae1d7; text-decoration: none"
                    >BYATHLON 2026</a
                  >
                </div>
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                margin: 0 auto;"
                >
                  <tbody>
                    <tr>
                      <td
                        style="background: #669bbc; font-size: 0; line-height: 0"
                      >
                        &nbsp;
                      </td>
                      <td
                        style="background: #efca5c; font-size: 0; line-height: 0"
                      >
                        &nbsp;
                      </td>
                      <td
                        style="background: #606c38; font-size: 0; line-height: 0"
                      >
                        &nbsp;
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>

            <!-- Body -->
            <tr>
              <td style="padding: 32px">
                <!-- Hälsning -->
                <div
                  style="margin: 0 0 8px;
                color: #25231e;
                font-size: 20px;
                font-weight: bold;"
                >
                  Hej @{triggerBody()?['fornamn']}!
                </div>
                <div
                  style="margin: 0 0 24px;
                color: #595648;
                font-size: 15px;
                line-height: 1.55;"
                >
                  Din anmälan till Byathlon 2026 är mottagen. Här är dina
                  uppgifter:
                </div>

                <!-- Uppgifter -->
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                margin: 0 0 24px;"
                >
                  <tbody>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        Namn
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;
                    font-weight: bold;"
                      >
                        @{triggerBody()?['fornamn']}
                        @{triggerBody()?['efternamn']}
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        Klass
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;
                    font-weight: bold;"
                      >
                        @{triggerBody()?['klass']}
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        Ålder
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;"
                      >
                        @{triggerBody()?['alder']}
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        E-post
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;"
                      >
                        @{triggerBody()?['epost']}
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        Telefon
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;"
                      >
                        @{triggerBody()?['telefon']}
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        Klubb
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;"
                      >
                        @{triggerBody()?['klubb']}
                      </td>
                    </tr>
                  </tbody>
                </table>

                <!-- Swish-betalning -->
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                margin: 0 0 24px;
                width: 100%;"
                >
                  <tbody>
                    <tr>
                      <td
                        style="background: #efeeeb; padding: 24px; text-align: center"
                      >
                        <div
                          style="margin: 0 0 6px;
                      color: #7f7a67;
                      font-size: 11px;
                      font-weight: bold;
                      letter-spacing: 2px;
                      text-transform: uppercase;"
                        >
                          Betala anmälningsavgift
                        </div>
                        <div
                          style="margin: 0 0 4px;
                      color: #25231e;
                      font-size: 26px;
                      font-weight: bold;"
                        >
                          300 kr
                        </div>
                        <div
                          style="margin: 0 0 16px;
                      color: #595648;
                      font-size: 13px;
                      line-height: 1.55;"
                        >
                          Gärna mer — överskott går till välgörenhet.
                        </div>

                        <!-- QR-kod -->
                        <table
                          cellpadding="0"
                          cellspacing="0"
                          border="0"
                          style="mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      margin: 0 auto 12px;"
                        >
                          <tbody>
                            <tr>
                              <td style="background: #ffffff; padding: 12px">
                                <img
                                  src="data:image/png;base64,@{base64(body('HTTP'))}"
                                  alt="Swish QR-kod"
                                  width="200"
                                  height="200"
                                  style="width: 200px;
                            height: 200px;
                            border: 0;
                            display: block;"
                                />
                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <div
                          style="margin: 0 0 16px;
                      color: #7f7a67;
                      font-size: 12px;"
                        >
                          Skanna med Swish-appen
                        </div>

                        <!-- Knapp -->
                        <table
                          cellpadding="0"
                          cellspacing="0"
                          border="0"
                          style="mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      margin: 0 auto;"
                        >
                          <tbody>
                            <tr>
                              <td
                                style="background: #EE2364;
                          padding: 12px 28px;
                          text-align: center;"
                              >
                                <a
                                  href="@{variables('System_SwishLink')}"
                                  style="color: #ffffff;
                            text-decoration: none;
                            font-family: Arial, Helvetica, sans-serif;
                            font-size: 14px;
                            font-weight: bold;"
                                >
                                  Öppna i Swish
                                </a>
                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <div
                          style="margin: 10px 0 0;
                      color: #7f7a67;
                      font-size: 11px;"
                        >
                          Knappen funkar på mobil med Swish-appen installerad.
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <!-- Eventinfo -->
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                margin: 0 0 24px;
                width: 100%;"
                >
                  <tbody>
                    <tr>
                      <td style="background: #efeeeb; padding: 20px">
                        <table
                          cellpadding="0"
                          cellspacing="0"
                          border="0"
                          style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
                        >
                          <tbody>
                            <tr>
                              <td
                                style="padding: 4px 0; color: #7f7a67; font-size: 13px"
                              >
                                Datum
                              </td>
                              <td
                                style="padding: 4px 0;
                          color: #25231e;
                          font-size: 14px;
                          font-weight: bold;"
                              >
                                Lördag 25 juli 2026
                              </td>
                            </tr>
                            <tr>
                              <td
                                style="padding: 4px 0; color: #7f7a67; font-size: 13px"
                              >
                                Start
                              </td>
                              <td
                                style="padding: 4px 0;
                          color: #25231e;
                          font-size: 14px;
                          font-weight: bold;"
                              >
                                @{if(equals(triggerBody()?['klass'],'Motion'),'Kl.
                                16:10','Kl. 16:00')}
                              </td>
                            </tr>
                            <tr>
                              <td
                                style="padding: 4px 0; color: #7f7a67; font-size: 13px"
                              >
                                Plats
                              </td>
                              <td
                                style="padding: 4px 0;
                          color: #25231e;
                          font-size: 14px;
                          font-weight: bold;"
                              >
                                Sidensjö
                              </td>
                            </tr>
                            <tr>
                              <td
                                style="padding: 4px 0; color: #7f7a67; font-size: 13px"
                              >
                                Samling
                              </td>
                              <td
                                style="padding: 4px 0;
                          color: #25231e;
                          font-size: 14px;"
                              >
                                Från kl. 15:00
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <!-- Checklista -->
                <div
                  style="margin: 0 0 8px;
                color: #36342b;
                font-size: 15px;
                font-weight: bold;"
                >
                  Ta med till tävlingen:
                </div>
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                margin: 0 0 24px;"
                >
                  <tbody>
                    <tr>
                      <td
                        style="padding: 3px 8px 3px 0;
                    color: #606c38;
                    font-size: 15px;
                    line-height: 1.5;
                    width: 18px;"
                      >
                        ✓
                      </td>
                      <td
                        style="padding: 3px 0;
                    color: #474439;
                    font-size: 14px;
                    line-height: 1.5;"
                      >
                        Cykel &amp; hjälm
                        <span
                          style="color: #a41e1e; font-size: 12px; font-weight: bold"
                          >(obligatoriskt)</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 3px 8px 3px 0;
                    color: #606c38;
                    font-size: 15px;
                    line-height: 1.5;"
                      >
                        ✓
                      </td>
                      <td
                        style="padding: 3px 0;
                    color: #474439;
                    font-size: 14px;
                    line-height: 1.5;"
                      >
                        Badkläder &amp; handduk
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 3px 8px 3px 0;
                    color: #606c38;
                    font-size: 15px;
                    line-height: 1.5;"
                      >
                        ✓
                      </td>
                      <td
                        style="padding: 3px 0;
                    color: #474439;
                    font-size: 14px;
                    line-height: 1.5;"
                      >
                        Löparskor
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 3px 8px 3px 0;
                    color: #606c38;
                    font-size: 15px;
                    line-height: 1.5;"
                      >
                        ✓
                      </td>
                      <td
                        style="padding: 3px 0;
                    color: #474439;
                    font-size: 14px;
                    line-height: 1.5;"
                      >
                        Vattenflaska
                      </td>
                    </tr>
                  </tbody>
                </table>

                <div
                  style="margin: 0 0 28px;
                color: #595648;
                font-size: 14px;
                line-height: 1.55;"
                >
                  Vi ses i Sidensjö!
                </div>

                <!-- Sponsorer -->
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                border-top: 1px solid #dfded8;
                width: 100%;"
                >
                  <tbody>
                    <tr>
                      <td style="padding: 24px 0 0">
                        <div
                          style="margin: 0 0 14px;
                      color: #7f7a67;
                      font-size: 10px;
                      font-weight: bold;
                      letter-spacing: 2px;
                      text-align: center;
                      text-transform: uppercase;"
                        >
                          Huvudsponsorer
                        </div>
                        <table
                          cellpadding="0"
                          cellspacing="0"
                          border="0"
                          style="mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      margin: 0 auto 18px;"
                        >
                          <tbody>
                            <tr>
                              <td style="padding: 8px 18px">
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/Vagtrummor.webp"
                                    alt="HK Vägtrummor"
                                    height="44"
                                    style="height: 44px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                              <td style="padding: 8px 18px">
                                <table
                                  cellpadding="0"
                                  cellspacing="0"
                                  border="0"
                                  style="mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              background-color: #11100e;
                              border-radius: 8px;"
                                >
                                  <tr>
                                    <td style="padding: 8px 14px;">
                                      <a
                                        href="https://byathlon.se/#sponsorer"
                                        style="text-decoration: none"
                                      >
                                        <img
                                          src="https://byathlon.se/Image/Sponsorer/sic-logo-mark-only.svg"
                                          alt="SI Construction"
                                          height="40"
                                          style="height: 40px;
                              width: auto;
                              border: 0;
                              display: block;"
                                        />
                                      </a>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <div
                          style="margin: 0 0 12px;
                      color: #7f7a67;
                      font-size: 10px;
                      font-weight: bold;
                      letter-spacing: 2px;
                      text-align: center;
                      text-transform: uppercase;"
                        >
                          Sponsorer
                        </div>
                        <table
                          cellpadding="0"
                          cellspacing="0"
                          border="0"
                          style="mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      margin: 0 auto;"
                        >
                          <tbody>
                            <tr>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/PolarbrodTB.png"
                                    alt="Polarbröd"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/norrmejerier-logo.png"
                                    alt="Norrmejerier"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/norrlands-guld-logo-jan-2021.png"
                                    alt="Norrlands Guld"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                            </tr>
                            <tr>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/LOGO%20OsteopatiByKjellsson.png"
                                    alt="Osteopati by Kjellsson"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/Anna-wellbeing.JPG"
                                    alt="Wellbeing by Anna"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/Vestins_EkoLantbrukTB.png"
                                    alt="Vestins Ekolantbruk"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>

            <!-- Footer -->
            <tr>
              <td
                style="background: #efeeeb;
              padding: 20px 32px;
              border-top: 1px solid #c1bfb3;
              text-align: center;"
              >
                <div style="margin: 0 0 10px; color: #7f7a67; font-size: 12px">
                  Arrangör: By Intresseförening
                </div>
                <div style="margin: 0 0 10px; color: #7f7a67; font-size: 12px">
                  <a
                    href="https://www.facebook.com/profile.php?id=61589342865676"
                    style="color: #595648; text-decoration: none"
                    >Facebook</a
                  >
                  <span style="color: #c1bfb3">&nbsp;·&nbsp;</span>
                  <a
                    href="https://www.instagram.com/byathlon/"
                    style="color: #595648; text-decoration: none"
                    >Instagram</a
                  >
                  <span style="color: #c1bfb3">&nbsp;·&nbsp;</span>
                  <a
                    href="https://byathlon.se"
                    style="color: #595648; text-decoration: none"
                    >byathlon.se</a
                  >
                </div>
                <div style="margin: 0; color: #a29d8b; font-size: 11px">
                  Vid frågor, skicka mail till daga@kjellsson.nu.
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>

<!-- Automatiserat meddelande - utanför mail-omslaget -->
<div
  style="font-family: Arial, Helvetica, sans-serif;
    color: #595959;
    font-size: 11px;
    line-height: 1.5;
    padding: 16px 0 8px;"
>
  <div style="margin: 0 0 4px; font-weight: bold">
    Automatiserat meddelande – svara inte
  </div>
  <div style="margin: 0 0 4px">
    This is an automated message. Replies are not monitored.
  </div>
  <div style="margin: 0">
    Eventuell signatur nedan tillhör företaget, inte avsändaren av detta
    automatutskick.
  </div>
</div>
```

---

## MAIL 2: Uppdaterad anmälan (True-sidan)

**Till:** `@{triggerBody()?['epost']}`
**Ämne:** `Anmälan uppdaterad — Byathlon 2026`

**Body (HTML):**

```html
<table
  cellpadding="0"
  cellspacing="0"
  border="0"
  style="mso-table-lspace: 0pt;
    mso-table-rspace: 0pt;
    font-family: Arial, Helvetica, sans-serif;"
>
  <tbody>
    <tr>
      <td style="background: #f5f4ef; padding: 24px 16px">
        <!-- Yttre mail-container (max 600px) -->
        <table
          cellpadding="0"
          cellspacing="0"
          border="0"
          style="mso-table-lspace: 0pt;
          mso-table-rspace: 0pt;
          max-width: 600px;
          width: 100%;
          background: #ffffff;
          border: 1px solid #c1bfb3;"
        >
          <!-- Header -->
          <tbody>
            <tr>
              <td
                style="background: #36342b; padding: 28px 32px; text-align: center"
              >
                <div
                  style="margin: 0 0 12px;
                color: #eae1d7;
                font-size: 22px;
                font-weight: bold;
                letter-spacing: 1px;"
                >
                  <a
                    href="https://byathlon.se"
                    style="color: #eae1d7; text-decoration: none"
                    >BYATHLON 2026</a
                  >
                </div>
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                margin: 0 auto;"
                >
                  <tbody>
                    <tr>
                      <td
                        style="background: #669bbc; font-size: 0; line-height: 0"
                      >
                        &nbsp;
                      </td>
                      <td
                        style="background: #efca5c; font-size: 0; line-height: 0"
                      >
                        &nbsp;
                      </td>
                      <td
                        style="background: #606c38; font-size: 0; line-height: 0"
                      >
                        &nbsp;
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>

            <!-- Body -->
            <tr>
              <td style="padding: 32px">
                <!-- Hälsning -->
                <div
                  style="margin: 0 0 8px;
                color: #25231e;
                font-size: 20px;
                font-weight: bold;"
                >
                  Hej @{triggerBody()?['fornamn']}!
                </div>
                <div
                  style="margin: 0 0 24px;
                color: #595648;
                font-size: 15px;
                line-height: 1.55;"
                >
                  Din anmälan har uppdaterats med dina senaste uppgifter:
                </div>

                <!-- Uppgifter -->
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                margin: 0 0 24px;"
                >
                  <tbody>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        Namn
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;
                    font-weight: bold;"
                      >
                        @{triggerBody()?['fornamn']}
                        @{triggerBody()?['efternamn']}
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        Klass
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;
                    font-weight: bold;"
                      >
                        @{triggerBody()?['klass']}
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        Ålder
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;"
                      >
                        @{triggerBody()?['alder']}
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        E-post
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;"
                      >
                        @{triggerBody()?['epost']}
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        Telefon
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;"
                      >
                        @{triggerBody()?['telefon']}
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #7f7a67;
                    font-size: 13px;"
                      >
                        Klubb
                      </td>
                      <td
                        style="padding: 10px 12px;
                    border-bottom: 1px solid #dfded8;
                    color: #25231e;
                    font-size: 14px;"
                      >
                        @{triggerBody()?['klubb']}
                      </td>
                    </tr>
                  </tbody>
                </table>

                <!-- Info-ruta (OBS) -->
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                margin: 0 0 24px;"
                >
                  <tbody>
                    <tr>
                      <td
                        style="background: #fdf9ec;
                    border-left: 3px solid #efca5c;
                    padding: 12px 16px;
                    color: #664f0a;
                    font-size: 13px;
                    line-height: 1.55;"
                      >
                        <strong>OBS:</strong> Denna anmälan ersätter din
                        tidigare registrering. Inga andra ändringar behövs.
                      </td>
                    </tr>
                  </tbody>
                </table>

                <!-- Swish-betalning -->
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                margin: 0 0 24px;
                width: 100%;"
                >
                  <tbody>
                    <tr>
                      <td
                        style="background: #efeeeb; padding: 24px; text-align: center"
                      >
                        <div
                          style="margin: 0 0 6px;
                      color: #7f7a67;
                      font-size: 11px;
                      font-weight: bold;
                      letter-spacing: 2px;
                      text-transform: uppercase;"
                        >
                          Betala anmälningsavgift
                        </div>
                        <div
                          style="margin: 0 0 4px;
                      color: #25231e;
                      font-size: 26px;
                      font-weight: bold;"
                        >
                          300 kr
                        </div>
                        <div
                          style="margin: 0 0 16px;
                      color: #595648;
                      font-size: 13px;
                      line-height: 1.55;"
                        >
                          Gärna mer — överskott går till välgörenhet. Bortse om
                          du redan betalat.
                        </div>

                        <!-- QR-kod -->
                        <table
                          cellpadding="0"
                          cellspacing="0"
                          border="0"
                          style="mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      margin: 0 auto 12px;"
                        >
                          <tbody>
                            <tr>
                              <td style="background: #ffffff; padding: 12px">
                                <img
                                  src="data:image/png;base64,@{base64(body('HTTP'))}"
                                  alt="Swish QR-kod"
                                  width="200"
                                  height="200"
                                  style="width: 200px;
                            height: 200px;
                            border: 0;
                            display: block;"
                                />
                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <div
                          style="margin: 0 0 16px;
                      color: #7f7a67;
                      font-size: 12px;"
                        >
                          Skanna med Swish-appen
                        </div>

                        <!-- Knapp -->
                        <table
                          cellpadding="0"
                          cellspacing="0"
                          border="0"
                          style="mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      margin: 0 auto;"
                        >
                          <tbody>
                            <tr>
                              <td
                                style="background: #EE2364;
                          padding: 12px 28px;
                          text-align: center;"
                              >
                                <a
                                  href="@{variables('System_SwishLink')}"
                                  style="color: #ffffff;
                            text-decoration: none;
                            font-family: Arial, Helvetica, sans-serif;
                            font-size: 14px;
                            font-weight: bold;"
                                >
                                  Öppna i Swish
                                </a>
                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <div
                          style="margin: 10px 0 0;
                      color: #7f7a67;
                      font-size: 11px;"
                        >
                          Knappen funkar på mobil med Swish-appen installerad.
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <!-- Eventinfo -->
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                margin: 0 0 24px;
                width: 100%;"
                >
                  <tbody>
                    <tr>
                      <td style="background: #efeeeb; padding: 20px">
                        <table
                          cellpadding="0"
                          cellspacing="0"
                          border="0"
                          style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
                        >
                          <tbody>
                            <tr>
                              <td
                                style="padding: 4px 0; color: #7f7a67; font-size: 13px"
                              >
                                Datum
                              </td>
                              <td
                                style="padding: 4px 0;
                          color: #25231e;
                          font-size: 14px;
                          font-weight: bold;"
                              >
                                Lördag 25 juli 2026
                              </td>
                            </tr>
                            <tr>
                              <td
                                style="padding: 4px 0; color: #7f7a67; font-size: 13px"
                              >
                                Start
                              </td>
                              <td
                                style="padding: 4px 0;
                          color: #25231e;
                          font-size: 14px;
                          font-weight: bold;"
                              >
                                @{if(equals(triggerBody()?['klass'],'Motion'),'Kl.
                                16:10','Kl. 16:00')}
                              </td>
                            </tr>
                            <tr>
                              <td
                                style="padding: 4px 0; color: #7f7a67; font-size: 13px"
                              >
                                Plats
                              </td>
                              <td
                                style="padding: 4px 0;
                          color: #25231e;
                          font-size: 14px;
                          font-weight: bold;"
                              >
                                Sidensjö
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <!-- Checklista -->
                <div
                  style="margin: 0 0 8px;
                color: #36342b;
                font-size: 15px;
                font-weight: bold;"
                >
                  Påminnelse — ta med:
                </div>
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                margin: 0 0 24px;"
                >
                  <tbody>
                    <tr>
                      <td
                        style="padding: 3px 8px 3px 0;
                    color: #606c38;
                    font-size: 15px;
                    line-height: 1.5;
                    width: 18px;"
                      >
                        ✓
                      </td>
                      <td
                        style="padding: 3px 0;
                    color: #474439;
                    font-size: 14px;
                    line-height: 1.5;"
                      >
                        Cykel &amp; hjälm
                        <span
                          style="color: #a41e1e; font-size: 12px; font-weight: bold"
                          >(obligatoriskt)</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 3px 8px 3px 0;
                    color: #606c38;
                    font-size: 15px;
                    line-height: 1.5;"
                      >
                        ✓
                      </td>
                      <td
                        style="padding: 3px 0;
                    color: #474439;
                    font-size: 14px;
                    line-height: 1.5;"
                      >
                        Badkläder &amp; handduk
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 3px 8px 3px 0;
                    color: #606c38;
                    font-size: 15px;
                    line-height: 1.5;"
                      >
                        ✓
                      </td>
                      <td
                        style="padding: 3px 0;
                    color: #474439;
                    font-size: 14px;
                    line-height: 1.5;"
                      >
                        Löparskor
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="padding: 3px 8px 3px 0;
                    color: #606c38;
                    font-size: 15px;
                    line-height: 1.5;"
                      >
                        ✓
                      </td>
                      <td
                        style="padding: 3px 0;
                    color: #474439;
                    font-size: 14px;
                    line-height: 1.5;"
                      >
                        Vattenflaska
                      </td>
                    </tr>
                  </tbody>
                </table>

                <div
                  style="margin: 0 0 28px;
                color: #595648;
                font-size: 14px;
                line-height: 1.55;"
                >
                  Vi ses i Sidensjö!
                </div>

                <!-- Sponsorer -->
                <table
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                  style="mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                border-top: 1px solid #dfded8;
                width: 100%;"
                >
                  <tbody>
                    <tr>
                      <td style="padding: 24px 0 0">
                        <div
                          style="margin: 0 0 14px;
                      color: #7f7a67;
                      font-size: 10px;
                      font-weight: bold;
                      letter-spacing: 2px;
                      text-align: center;
                      text-transform: uppercase;"
                        >
                          Huvudsponsorer
                        </div>
                        <table
                          cellpadding="0"
                          cellspacing="0"
                          border="0"
                          style="mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      margin: 0 auto 18px;"
                        >
                          <tbody>
                            <tr>
                              <td style="padding: 8px 18px">
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/Vagtrummor.webp"
                                    alt="HK Vägtrummor"
                                    height="44"
                                    style="height: 44px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                              <td style="padding: 8px 18px">
                                <table
                                  cellpadding="0"
                                  cellspacing="0"
                                  border="0"
                                  style="mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              background-color: #11100e;
                              border-radius: 8px;"
                                >
                                  <tr>
                                    <td style="padding: 8px 14px;">
                                      <a
                                        href="https://byathlon.se/#sponsorer"
                                        style="text-decoration: none"
                                      >
                                        <img
                                          src="https://byathlon.se/Image/Sponsorer/sic-logo-mark-only.svg"
                                          alt="SI Construction"
                                          height="40"
                                          style="height: 40px;
                              width: auto;
                              border: 0;
                              display: block;"
                                        />
                                      </a>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <div
                          style="margin: 0 0 12px;
                      color: #7f7a67;
                      font-size: 10px;
                      font-weight: bold;
                      letter-spacing: 2px;
                      text-align: center;
                      text-transform: uppercase;"
                        >
                          Sponsorer
                        </div>
                        <table
                          cellpadding="0"
                          cellspacing="0"
                          border="0"
                          style="mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      margin: 0 auto;"
                        >
                          <tbody>
                            <tr>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/PolarbrodTB.png"
                                    alt="Polarbröd"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/norrmejerier-logo.png"
                                    alt="Norrmejerier"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/norrlands-guld-logo-jan-2021.png"
                                    alt="Norrlands Guld"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                            </tr>
                            <tr>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/LOGO%20OsteopatiByKjellsson.png"
                                    alt="Osteopati by Kjellsson"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/Anna-wellbeing.JPG"
                                    alt="Wellbeing by Anna"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                              <td
                                style="padding: 6px 14px; vertical-align: middle"
                              >
                                <a
                                  href="https://byathlon.se/#sponsorer"
                                  style="text-decoration: none"
                                >
                                  <img
                                    src="https://byathlon.se/Image/Sponsorer/Vestins_EkoLantbrukTB.png"
                                    alt="Vestins Ekolantbruk"
                                    height="32"
                                    style="height: 32px;
                              width: auto;
                              border: 0;
                              display: block;"
                                  />
                                </a>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>

            <!-- Footer -->
            <tr>
              <td
                style="background: #efeeeb;
              padding: 20px 32px;
              border-top: 1px solid #c1bfb3;
              text-align: center;"
              >
                <div style="margin: 0 0 10px; color: #7f7a67; font-size: 12px">
                  Arrangör: By Intresseförening
                </div>
                <div style="margin: 0 0 10px; color: #7f7a67; font-size: 12px">
                  <a
                    href="https://www.facebook.com/profile.php?id=61589342865676"
                    style="color: #595648; text-decoration: none"
                    >Facebook</a
                  >
                  <span style="color: #c1bfb3">&nbsp;·&nbsp;</span>
                  <a
                    href="https://www.instagram.com/byathlon/"
                    style="color: #595648; text-decoration: none"
                    >Instagram</a
                  >
                  <span style="color: #c1bfb3">&nbsp;·&nbsp;</span>
                  <a
                    href="https://byathlon.se"
                    style="color: #595648; text-decoration: none"
                    >byathlon.se</a
                  >
                </div>
                <div style="margin: 0; color: #a29d8b; font-size: 11px">
                  Vid frågor, skicka mail till daga@kjellsson.nu.
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>

<!-- Automatiserat meddelande - utanför mail-omslaget -->
<div
  style="font-family: Arial, Helvetica, sans-serif;
    color: #595959;
    font-size: 11px;
    line-height: 1.5;
    padding: 16px 0 8px;"
>
  <div style="margin: 0 0 4px; font-weight: bold">
    Automatiserat meddelande – svara inte
  </div>
  <div style="margin: 0 0 4px">
    This is an automated message. Replies are not monitored.
  </div>
  <div style="margin: 0">
    Eventuell signatur nedan tillhör företaget, inte avsändaren av detta
    automatutskick.
  </div>
</div>
```

---

## Färgreferens (hemsidans palett)

| Användning          | Färg        | Hex       |
| ------------------- | ----------- | --------- |
| Header-bakgrund     | DGreenC-700 | `#36342b` |
| Header-text         | TanC-100    | `#eae1d7` |
| Brödtext            | DGreenC-800 | `#25231e` |
| Sekundärtext        | DGreenC-500 | `#595648` |
| Etikett/label       | DGreenC-400 | `#7f7a67` |
| Linje/border        | DGreenC-100 | `#dfded8` |
| Info-bakgrund       | DGreenC-50  | `#efeeeb` |
| Checkmark-grön      | GreenC-500  | `#606c38` |
| Varnings-gul (bg)   | YellowC-50  | `#fdf9ec` |
| Varnings-gul (text) | YellowC-800 | `#664f0a` |
| Varnings-gul (kant) | YellowC-400 | `#efca5c` |
| Hjälm-varning       | RedC-600    | `#a41e1e` |
| Tri-bar blå         | BlueC-500   | `#669bbc` |
| Tri-bar gul         | YellowC-400 | `#efca5c` |
| Tri-bar grön        | GreenC-500  | `#606c38` |

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
