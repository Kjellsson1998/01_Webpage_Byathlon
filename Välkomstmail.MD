# Välkomstmail — utskick till anmälda (veckan före eventet)

Klistra in HTML-koden i **Body**-fältet i "Send an email (V2)" (eller i
webbmailens källkodsläge, t.ex. Roundcube: verktygsknappen "Källkod").
Välj **Is HTML: Yes** i Power Automate.

**OBS:** Koden är medvetet skriven utan radbrytningar inuti taggarna —
bryt inte om den med en formatterare. Uppdelade taggar (t.ex. `</a` på en
rad och `>` på nästa) gör att webbmail-editorer skriver ut `a>` som text.

Mailet är ett massutskick till maillistan — inga dynamiska fält behövs.

**Ämne:** `Välkommen till Byathlon på lördag!`

**Body (HTML):**

```html
<table cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-family: Arial, Helvetica, sans-serif;">
  <tbody>
    <tr>
      <td style="background: #f5f4ef; padding: 24px 16px">
        <!-- Yttre mail-container (max 600px) -->
        <table cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; max-width: 600px; width: 100%; background: #ffffff; border: 1px solid #c1bfb3;">
          <tbody>
            <!-- Header -->
            <tr>
              <td style="background: #36342b; padding: 28px 32px; text-align: center">
                <div style="margin: 0 0 12px; color: #eae1d7; font-size: 22px; font-weight: bold; letter-spacing: 1px;">
                  <a href="https://byathlon.se" style="color: #eae1d7; text-decoration: none">BYATHLON 2026</a>
                </div>
                <table cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; margin: 0 auto;">
                  <tbody>
                    <tr>
                      <td style="background: #669bbc; font-size: 0; line-height: 0">&nbsp;</td>
                      <td style="background: #efca5c; font-size: 0; line-height: 0">&nbsp;</td>
                      <td style="background: #606c38; font-size: 0; line-height: 0">&nbsp;</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>

            <!-- Body -->
            <tr>
              <td style="padding: 32px">
                <!-- Hälsning -->
                <div style="margin: 0 0 8px; color: #25231e; font-size: 20px; font-weight: bold;">Hej!</div>
                <div style="margin: 0 0 24px; color: #595648; font-size: 15px; line-height: 1.55;">
                  Välkommen till Byathlon nu på lördag kl. 15:00! Uthämtning av nummerlappar sker mellan kl. 15:00&ndash;15:50, med gemensam start kl. 16:00. Hela tidsplanen för dagen hittar du nedan.
                </div>

                <!-- Tidsplan -->
                <table cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; margin: 0 0 24px; width: 100%;">
                  <tbody>
                    <tr>
                      <td style="background: #efeeeb; padding: 20px">
                        <div style="margin: 0 0 12px; color: #7f7a67; font-size: 11px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase;">Tidsplan &mdash; lördag 25 juli</div>
                        <table cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt">
                          <tbody>
                            <tr>
                              <td style="padding: 4px 16px 4px 0; color: #7f7a67; font-size: 13px; white-space: nowrap;">15:00</td>
                              <td style="padding: 4px 0; color: #25231e; font-size: 14px;">Välkommen</td>
                            </tr>
                            <tr>
                              <td style="padding: 4px 16px 4px 0; color: #7f7a67; font-size: 13px; white-space: nowrap;">15:00&ndash;15:50</td>
                              <td style="padding: 4px 0; color: #25231e; font-size: 14px;">Uthämtning av nummerlappar</td>
                            </tr>
                            <tr>
                              <td style="padding: 4px 16px 4px 0; color: #7f7a67; font-size: 13px; white-space: nowrap;">15:45</td>
                              <td style="padding: 4px 0; color: #25231e; font-size: 14px;">Gemensam genomgång</td>
                            </tr>
                            <tr>
                              <td style="padding: 4px 16px 4px 0; color: #25231e; font-size: 13px; font-weight: bold; white-space: nowrap;">16:00</td>
                              <td style="padding: 4px 0; color: #25231e; font-size: 14px; font-weight: bold;">START (gemensam start för alla klasser)</td>
                            </tr>
                            <tr>
                              <td style="padding: 4px 16px 4px 0; color: #7f7a67; font-size: 13px; white-space: nowrap;">17:00</td>
                              <td style="padding: 4px 0; color: #25231e; font-size: 14px;">Foodtruck &mdash; PMP strEATfood</td>
                            </tr>
                            <tr>
                              <td style="padding: 4px 16px 4px 0; color: #7f7a67; font-size: 13px; white-space: nowrap;">17:15</td>
                              <td style="padding: 4px 0; color: #25231e; font-size: 14px;">Varm bastu &amp; volleyboll</td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <!-- Områdeskarta -->
                <table cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; margin: 0 0 24px; width: 100%;">
                  <tbody>
                    <tr>
                      <td style="background: #efeeeb; padding: 24px; text-align: center">
                        <div style="margin: 0 0 6px; color: #7f7a67; font-size: 11px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase;">Områdeskarta</div>
                        <div style="margin: 0 0 16px; color: #595648; font-size: 13px; line-height: 1.55;">
                          Kika in tävlingsområdet i förväg &mdash; se var du kan parkera, byta om och var start och mål ligger.
                        </div>
                        <table cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; margin: 0 auto;">
                          <tbody>
                            <tr>
                              <td style="background: #36342b; padding: 12px 28px; text-align: center;">
                                <a href="https://byathlon.se/omradeskarta.html" style="color: #ffffff; text-decoration: none; font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-weight: bold;">Öppna områdeskartan</a>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                        <div style="margin: 10px 0 0; color: #7f7a67; font-size: 11px;">byathlon.se/omradeskarta.html</div>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <!-- Checklista -->
                <div style="margin: 0 0 8px; color: #36342b; font-size: 15px; font-weight: bold;">Det här tycker vi att du bör ha med dig:</div>
                <table cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; margin: 0 0 24px;">
                  <tbody>
                    <tr>
                      <td style="padding: 3px 8px 3px 0; color: #606c38; font-size: 15px; line-height: 1.5; width: 18px;">✓</td>
                      <td style="padding: 3px 0; color: #474439; font-size: 14px; line-height: 1.5;">Springkläder + löparskor</td>
                    </tr>
                    <tr>
                      <td style="padding: 3px 8px 3px 0; color: #606c38; font-size: 15px; line-height: 1.5;">✓</td>
                      <td style="padding: 3px 0; color: #474439; font-size: 14px; line-height: 1.5;">Ombyte (efter väder)</td>
                    </tr>
                    <tr>
                      <td style="padding: 3px 8px 3px 0; color: #606c38; font-size: 15px; line-height: 1.5;">✓</td>
                      <td style="padding: 3px 0; color: #474439; font-size: 14px; line-height: 1.5;">Badkläder</td>
                    </tr>
                    <tr>
                      <td style="padding: 3px 8px 3px 0; color: #606c38; font-size: 15px; line-height: 1.5;">✓</td>
                      <td style="padding: 3px 0; color: #474439; font-size: 14px; line-height: 1.5;">Handduk</td>
                    </tr>
                  </tbody>
                </table>

                <div style="margin: 0 0 28px; color: #595648; font-size: 14px; line-height: 1.55;">Vi ses på lördag i Sidensjö!</div>

                <!-- Sponsorer -->
                <table cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #dfded8; width: 100%;">
                  <tbody>
                    <tr>
                      <td style="padding: 24px 0 0">
                        <div style="margin: 0 0 14px; color: #7f7a67; font-size: 10px; font-weight: bold; letter-spacing: 2px; text-align: center; text-transform: uppercase;">Huvudsponsorer</div>
                        <table cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; margin: 0 auto 18px;">
                          <tbody>
                            <tr>
                              <td style="padding: 8px 18px">
                                <a href="https://byathlon.se/#sponsorer" style="text-decoration: none"><img src="https://byathlon.se/Image/Sponsorer/Vagtrummor.webp" alt="HK Vägtrummor" height="44" style="height: 44px; width: auto; border: 0; display: block;" /></a>
                              </td>
                              <td style="padding: 8px 18px">
                                <a href="https://byathlon.se/#sponsorer" style="text-decoration: none"><img src="https://byathlon.se/Image/Sponsorer/sic-logo-mark-only.png" alt="SI Construction" height="44" style="height: 44px; width: auto; border: 0; display: block;" /></a>
                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <div style="margin: 0 0 12px; color: #7f7a67; font-size: 10px; font-weight: bold; letter-spacing: 2px; text-align: center; text-transform: uppercase;">Sponsorer</div>
                        <table cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; margin: 0 auto;">
                          <tbody>
                            <tr>
                              <td style="padding: 6px 14px; vertical-align: middle">
                                <a href="https://byathlon.se/#sponsorer" style="text-decoration: none"><img src="https://byathlon.se/Image/Sponsorer/PolarbrodTB.png" alt="Polarbröd" height="32" style="height: 32px; width: auto; border: 0; display: block;" /></a>
                              </td>
                              <td style="padding: 6px 14px; vertical-align: middle">
                                <a href="https://byathlon.se/#sponsorer" style="text-decoration: none"><img src="https://byathlon.se/Image/Sponsorer/norrmejerier-logo.png" alt="Norrmejerier" height="32" style="height: 32px; width: auto; border: 0; display: block;" /></a>
                              </td>
                              <td style="padding: 6px 14px; vertical-align: middle">
                                <a href="https://byathlon.se/#sponsorer" style="text-decoration: none"><img src="https://byathlon.se/Image/Sponsorer/norrlands-guld-logo-jan-2021.png" alt="Norrlands Guld" height="32" style="height: 32px; width: auto; border: 0; display: block;" /></a>
                              </td>
                            </tr>
                            <tr>
                              <td style="padding: 6px 14px; vertical-align: middle">
                                <a href="https://byathlon.se/#sponsorer" style="text-decoration: none"><img src="https://byathlon.se/Image/Sponsorer/LOGO%20OsteopatiByKjellsson.png" alt="Osteopati by Kjellsson" height="32" style="height: 32px; width: auto; border: 0; display: block;" /></a>
                              </td>
                              <td style="padding: 6px 14px; vertical-align: middle">
                                <a href="https://www.facebook.com/profile.php?id=61581438246045" style="text-decoration: none"><img src="https://byathlon.se/Image/Sponsorer/Anna-wellbeing.JPG" alt="Wellbeing by Anna" height="32" style="height: 32px; width: auto; border: 0; display: block;" /></a>
                              </td>
                              <td style="padding: 6px 14px; vertical-align: middle">
                                <a href="https://www.facebook.com/profile.php?id=100054220372412" style="text-decoration: none"><img src="https://byathlon.se/Image/Sponsorer/Vestins_EkoLantbrukTB.png" alt="Vestins Ekolantbruk" height="32" style="height: 32px; width: auto; border: 0; display: block;" /></a>
                              </td>
                              <td style="padding: 6px 14px; vertical-align: middle">
                                <a href="https://byathlon.se/#sponsorer" style="text-decoration: none"><img src="https://byathlon.se/Image/Sponsorer/NICKS-logo-pink.png" alt="NICKS" height="32" style="height: 32px; width: auto; border: 0; display: block;" /></a>
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
              <td style="background: #efeeeb; padding: 20px 32px; border-top: 1px solid #c1bfb3; text-align: center;">
                <div style="margin: 0 0 10px; color: #7f7a67; font-size: 12px">Arrangör: By Intresseförening</div>
                <div style="margin: 0 0 10px; color: #7f7a67; font-size: 12px">
                  <a href="https://www.facebook.com/profile.php?id=61589342865676" style="color: #595648; text-decoration: none">Facebook</a>
                  <span style="color: #c1bfb3">&nbsp;·&nbsp;</span>
                  <a href="https://www.instagram.com/byathlon/" style="color: #595648; text-decoration: none">Instagram</a>
                  <span style="color: #c1bfb3">&nbsp;·&nbsp;</span>
                  <a href="https://byathlon.se" style="color: #595648; text-decoration: none">byathlon.se</a>
                </div>
                <div style="margin: 0; color: #a29d8b; font-size: 11px">Vid frågor, skicka mail till daga@kjellsson.nu.</div>
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>

<!-- Automatiserat meddelande - utanför mail-omslaget -->
<div style="font-family: Arial, Helvetica, sans-serif; color: #595959; font-size: 11px; line-height: 1.5; padding: 16px 0 8px;">
  <div style="margin: 0 0 4px; font-weight: bold">Automatiserat meddelande – svara inte</div>
  <div style="margin: 0 0 4px">This is an automated message. Replies are not monitored.</div>
  <div style="margin: 0">Eventuell signatur nedan tillhör företaget, inte avsändaren av detta automatutskick.</div>
</div>
```
