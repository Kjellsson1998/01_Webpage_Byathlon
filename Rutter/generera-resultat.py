# -*- coding: utf-8 -*-
"""Genererar resultat.html och RESULTAT-2026.md for Byathlon 2026.

All bandata kommer ur Stravas exporter i Rutter/Byathlon *.tcx:
  - distansen ar Stravas egen <DistanceMeters> langs banan
  - stigningen ar summerad uppforsbacke med 2 m brusfilter
Inga emojis i utdatan - HTML anvander SVG-ikoner, markdown ren typografi.
"""
import xml.etree.ElementTree as ET

ROOT = "c:/Users/HugoKjellsson/OneDrive/00 Kjellsson/07_Arrangemang/01_Byathlon/01_Webpage_Byathlon/"
T = "{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}"


# ───────────────────────── inlasning & matematik ─────────────────────────
def read_tcx(path):
    root = ET.parse(ROOT + "Rutter/" + path).getroot()
    total = float(root.find(".//%sLap/%sDistanceMeters" % (T, T)).text)
    d, ele = [], []
    for tp in root.iter("%sTrackpoint" % T):
        d.append(float(tp.find("%sDistanceMeters" % T).text))
        ele.append(float(tp.find("%sAltitudeMeters" % T).text))
    return total, d, ele


def gain(ele, thr=2.0):
    """Summerad upp- och nedforsbacke. Trosklen filtrerar GPS-brus."""
    upp = ner = 0.0
    prev = ele[0]
    for e in ele[1:]:
        delta = e - prev
        if abs(delta) >= thr:
            if delta > 0:
                upp += delta
            else:
                ner += -delta
            prev = e
    return upp, ner


def steepest(d, ele, lo=180.0, hi=260.0):
    """Brantaste sammanhangande partiet pa ca 200 m."""
    bast = None
    for i in range(len(d)):
        for j in range(i + 1, len(d)):
            langd = d[j] - d[i]
            if langd < lo:
                continue
            if langd > hi:
                break
            lut = (ele[j] - ele[i]) / langd * 100
            if bast is None or lut > bast[0]:
                bast = (lut, d[i] / 1000)
    return bast


def profile(d, ele, W=1000.0, H=100.0, pad=8.0):
    lo, hi = min(ele), max(ele)
    rng = (hi - lo) or 1.0
    tot = d[-1]
    pts = ["%.1f,%.1f" % (d[i] / tot * W, H - pad - (ele[i] - lo) / rng * (H - 2 * pad))
           for i in range(len(d))]
    line = "M" + " L".join(pts)
    return line, line + " L%.1f,%.1f L0,%.1f Z" % (W, H, H)


def secs(t):
    h, m, s = map(int, t.split(":"))
    return h * 3600 + m * 60 + s


def hhmmss(s):
    s = int(round(s))
    return "%02d:%02d:%02d" % (s // 3600, (s % 3600) // 60, s % 60)


def pace(sec, km):
    v = int(round(sec / km))          # hela sekunder forst, annars blir 239,7 -> "3:60"
    return "%d:%02d" % (v // 60, v % 60)


def nf(n, d=0):
    """Svensk talformatering: komma som decimaltecken, hart mellanslag som tusental."""
    s = ("{:,.%df}" % d).format(n)
    heltal, _, dec = s.partition(".")
    return heltal.replace(",", "\u00a0") + ("," + dec if dec else "")


# ───────────────────────── bandata ─────────────────────────
BANOR = {}
for key, fil in [("lang", "Byathlon 13,5km.tcx"), ("kort", "Byathlon 5,5km.tcx")]:
    total, d, ele = read_tcx(fil)
    upp, ner = gain(ele)
    imax = max(range(len(ele)), key=lambda i: ele[i])
    imin = min(range(len(ele)), key=lambda i: ele[i])
    line, area = profile(d, ele)
    brant = steepest(d, ele)
    halv = total / 2
    ih = min(range(len(d)), key=lambda i: abs(d[i] - halv))
    BANOR[key] = dict(
        km=total / 1000, upp=upp, ner=ner, netto=ele[-1] - ele[0],
        hi=ele[imax], hi_km=d[imax] / 1000, lo=ele[imin], lo_km=d[imin] / 1000,
        line=line, area=area, hm_km=upp / (total / 1000),
        brant=brant[0], brant_km=brant[1],
        g1=gain(ele[:ih + 1])[0], hi_x=d[imax] / total * 1000.0)

L, K = BANOR["lang"], BANOR["kort"]

# ───────────────────────── resultat ─────────────────────────
LANG = [(1,128,"Steffen Dalsgaard","00:54:02"),(2,101,"Alfred Hellgren","01:03:53"),
(3,132,"Tord Berggren","01:04:48"),(4,133,"Willy Westman","01:05:22"),
(5,114,"Karin Hägglund","01:06:09"),(6,110,"Hilding Kjellqvist","01:07:10"),
(7,112,"Isak Nordberg","01:08:25"),(8,123,"Robert Bruce","01:09:35"),
(9,111,"Ida Näslund","01:09:50"),(10,105,"Christian Häggström","01:10:50"),
(11,122,"Philip Sundström","01:11:01"),(12,131,"Tobias Axandersson","01:11:15"),
(13,107,"Emil Petersson","01:12:55"),(14,115,"Klara Sundberg","01:13:23"),
(15,134,"Conny Eriksson","01:13:26"),(16,135,"Fredrik Rosenblom","01:14:11"),
(17,109,"Filip Andersson","01:15:54"),(18,113,"Jonatan Hjeltman","01:16:08"),
(19,103,"Ann-Caroline Wiberg","01:17:08"),(20,127,"Simon Lundberg","01:17:36"),
(21,125,"Sabina Hermansson","01:18:59"),(22,104,"Brian Thorsén","01:19:07"),
(23,106,"David Kjellqvist","01:20:40"),(24,139,"Saga Näslund","01:21:46"),
(25,142,"Jon Pynesius","01:22:13"),(26,102,"Alva Karlsson","01:23:01"),
(27,119,"Mats Karlsson","01:23:04"),(28,120,"Michaela Häggström","01:24:18"),
(29,116,"Lena-Maria Vallrud","01:24:58"),(30,108,"Evelina Strandberg","01:25:43"),
(30,141,"Erik Holmgren","01:25:43"),(32,124,"Ronja Mella","01:28:27"),
(33,140,"Jesper Nordström","01:37:57"),(34,143,"Arvid Dynesius","01:38:06"),
(35,130,"Terese Eidenmark","01:39:49"),(36,137,"Julia Höglund","02:01:55"),
(37,138,"Victor Höglund","02:01:57"),(38,136,"Lova Höglund","02:02:32")]

KORT = [(1,225,"Anton Hägglund","00:26:40"),(2,218,"Pär Byström","00:27:01"),
(3,219,"Johan Westman","00:28:01"),(4,211,"Louise Byström","00:29:42"),
(5,216,"Hanna Byström","00:29:44"),(6,215,"Therese Westman","00:30:11"),
(7,221,"Klara Byström","00:30:20"),(8,223,"Jonas Westman","00:30:49"),
(9,276,"Lukas Palm","00:32:03"),(10,229,"Vega Kjellsson","00:32:04"),
(11,213,"Rasmus Kjellqvist","00:32:16"),(12,210,"Lina Kjellqvist","00:32:51"),
(13,212,"Maja Gidlund","00:32:53"),(14,237,"Hugo Kjellsson","00:32:55"),
(15,227,"Björn Dynesius","00:32:57"),(16,206,"Hannah Gidlund","00:33:43"),
(17,220,"Eva Svensson","00:33:51"),(18,222,"Carina Söderlund","00:33:54"),
(19,203,"Elvira Nyberg","00:35:21"),(19,208,"Judith Näslund","00:35:21"),
(21,226,"Lilly Källgren","00:35:34"),(22,217,"Lars Höglund","00:40:18"),
(23,204,"Emil Björkqvist","00:40:29"),(24,224,"Kristi Poldeja","00:41:05"),
(25,201,"Albin Björkqvist","00:48:00"),(25,202,"Anna Björkqvist","00:48:00"),
(27,214,"Ulrika Edholm","00:51:54"),(28,228,"Elvira Carlsson","01:00:38"),
(29,209,"Julia Byström","01:00:42"),(30,205,"Emmy Berggren","01:00:56")]

MOTION = [(277,"Rasmus Sjöblom"),(278,"Britta Palén"),(279,"Klara Sundell"),
(281,"Cornelia Vidmark"),(282,"Madelaine Höglund"),(285,"Ove Höglund"),
(286,"Michael Dolhai"),(287,"Maria Häggström"),(289,"Lena Kristoffersson"),
(290,"Lars-Olof Häggström"),(292,"Kerstin Sundwall"),(294,"Tilda Holmgren"),
(295,"Emelie Sjölander"),(296,"Ellen Holmgren"),(297,"Dennis Ludén"),
(298,"Anna Uhlin"),(299,"Alexander Gustavsson")]

# Klassegrare per kon - bekraftade av arrangoren (finns inte i anmalningsdatan).
VINNARE = {"lang": {128: "herr", 114: "dam"}, "kort": {225: "herr", 211: "dam"}}

# Utom tavlan: sprang banan pa egen hand en annan dag, ingar inte i placeringarna.
UTOM = [(238, "Elias Sundström", "00:30:37", "Sekretariatet — sprang banan dagen efter loppet")]

nl, nk, nm = len(LANG), len(KORT), len(MOTION)
tot_pers = nl + nk + nm
tot_km = nl * L["km"] + (nk + nm) * K["km"]
tot_hm = nl * L["upp"] + (nk + nm) * K["upp"]
tot_sec = sum(secs(r[3]) for r in LANG) + sum(secs(r[3]) for r in KORT)
tot_h, tot_m = int(tot_sec // 3600), int((tot_sec % 3600) // 60)


# ───────────────────────── SVG-ikoner (inga emojis) ─────────────────────────
IKONER = {
    "distans": '<path d="M3 8.5v7M21 8.5v7M3 12h18"/><path d="M8 10.5v3M12 10v4M16 10.5v3"/>',
    "klattring": '<path d="M3 17.5l5.5-5.5 3.5 3.5L20 7"/><path d="M15 7h5v5"/>',
    "netto": '<circle cx="12" cy="12" r="8.5"/><path d="M8.2 10.2h7.6M8.2 13.8h7.6"/>',
    "topp": '<path d="M2 19l6.5-10.5 4.2 6.5 2.6-3.8L21.5 19z"/><circle cx="8.5" cy="8.5" r="1.5"/>',
    "vatten": ('<path d="M2.5 10.5c1.6-2 3.2-2 4.8 0s3.2 2 4.8 0 3.2-2 4.8 0 3.2 2 4.8 0"/>'
               '<path d="M2.5 15.5c1.6-2 3.2-2 4.8 0s3.2 2 4.8 0 3.2-2 4.8 0 3.2 2 4.8 0"/>'),
    "lutning": '<path d="M3.5 19.5h17"/><path d="M3.5 19.5L19 6.5"/><path d="M9.8 19.5a6.3 6.3 0 0 0-1.1-3.5"/>',
    "brant": '<path d="M3.5 19.5h17M3.5 19.5 17.5 5.5"/><path d="M13.3 5.5h4.2v4.2"/>',
    "tass": ('<ellipse cx="7.3" cy="10.2" rx="1.9" ry="2.5"/><ellipse cx="12" cy="8.4" rx="1.9" ry="2.6"/>'
             '<ellipse cx="16.7" cy="10.2" rx="1.9" ry="2.5"/>'
             '<path d="M12 20.4c-2.5 0-4.5-1.5-4.5-3.4 0-1.9 2-3.3 4.5-3.3s4.5 1.4 4.5 3.3c0 1.9-2 3.4-4.5 3.4z"/>'),
    "urtavla": ('<circle cx="12" cy="13.5" r="7"/><path d="M12 9.8v3.7M9.8 2.8h4.4M12 2.8v2.3"/>'
                '<path d="M6.2 19.8 18.4 6.6"/>'),
    "bastu": ('<path d="M12 12c0-3 2.5-6 2.5-6s2.5 3 2.5 6a2.5 2.5 0 0 1-5 0Z"/>'
              '<path d="M7 15c0-2 1.5-4 1.5-4s1.5 2 1.5 4a1.5 1.5 0 0 1-3 0Z"/>'
              '<rect x="2.5" y="18" width="19" height="3.5" rx="1"/>'),
    "medalj": '<circle cx="12" cy="9" r="5.2"/><path d="M8.8 13.4 7.5 21l4.5-2.3 4.5 2.3-1.3-7.6"/>',
}


def ikon(namn, klass="ikon"):
    return ('<svg class="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true" focusable="false">%s</svg>' % (klass, IKONER[namn]))


def statchip(ikonnamn, varde, etikett):
    return ('          <div class="chip">%s<span class="chip-v">%s</span>'
            '<span class="chip-l">%s</span></div>'
            % (ikon(ikonnamn, "chip-i"), varde, etikett))


def rows(data, km, vinnare):
    ut = []
    delad = {}
    for p, *_ in data:
        delad[p] = delad.get(p, 0) + 1
    for plac, nr, namn, tid in data:
        kon = vinnare.get(nr)
        klass = " seger" if kon else ""
        märke = ('<span class="vinnare">%s1:a %s</span>' % (ikon("medalj", "v-i"), kon)) if kon else ""
        tie = ' <span class="tie" title="Delad placering">delad</span>' if delad[plac] > 1 else ""
        ut.append(
            '        <tr class="rad%s" data-sok="%s %s">\n'
            '          <td class="plac">%d%s</td>\n'
            '          <td class="nr">%d</td>\n'
            '          <td class="namn">%s%s</td>\n'
            '          <td class="tid">%s</td>\n'
            '          <td class="tempo">%s</td>\n'
            '        </tr>'
            % (klass, namn.lower(), nr, plac, tie, nr, namn, märke, tid, pace(secs(tid), km)))
    return "\n".join(ut)


def utom_block(km, jamfor):
    """Kort utom-tavlan-block. jamfor = tidtagna resultat att jamfora placering mot."""
    kort_ut = []
    for nr, namn, tid, notis in UTOM:
        snabbare = sum(1 for _, _, _, t in jamfor if secs(t) < secs(tid))
        kort_ut.append(f'''          <li class="utom-post" data-sok="{namn.lower()} {nr}" data-utom>
            <div class="utom-topp">
              <span class="utom-nr">{nr}</span>
              <span class="utom-namn">{namn}</span>
              <span class="utom-tid">{tid[3:]}</span>
            </div>
            <p class="utom-notis">{notis}</p>
            <p class="utom-jamf">
              {pace(secs(tid), km)} min/km &mdash; en tid som hade r&auml;ckt till
              <strong>{snabbare + 1}:e plats</strong> i t&auml;vlingen.
            </p>
          </li>''')
    return "\n".join(kort_ut)


def motion_lista():
    return "\n".join(
        '        <li class="deltagare" data-sok="%s %d"><span class="d-nr">%d</span>'
        '<span class="d-namn">%s</span></li>' % (namn.lower(), nr, nr, namn)
        for nr, namn in MOTION)


def profil_svg(b, ident, farg):
    return f'''        <figure class="profil">
          <svg viewBox="0 0 1000 100" preserveAspectRatio="none" role="img"
               aria-label="Höjdprofil från {nf(b['lo'])} till {nf(b['hi'])} meter över havet">
            <defs>
              <linearGradient id="g-{ident}" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="{farg}" stop-opacity="0.42" />
                <stop offset="100%" stop-color="{farg}" stop-opacity="0.02" />
              </linearGradient>
            </defs>
            <path d="{b['area']}" fill="url(#g-{ident})" />
            <path d="{b['line']}" fill="none" stroke="{farg}" stroke-width="2"
                  vector-effect="non-scaling-stroke" stroke-linejoin="round" />
            <line x1="{b['hi_x']:.1f}" y1="0" x2="{b['hi_x']:.1f}" y2="100"
                  stroke="{farg}" stroke-width="1" stroke-dasharray="3 3" opacity="0.55"
                  vector-effect="non-scaling-stroke" />
          </svg>
          <figcaption class="profil-txt">
            <span>Lägst {nf(b['lo'])}&nbsp;m ö.h.</span>
            <span class="profil-topp">Högst {nf(b['hi'])}&nbsp;m ö.h. vid km {nf(b['hi_km'], 2)}</span>
            <span>{nf(b['km'], 2)}&nbsp;km</span>
          </figcaption>
        </figure>'''


HTML = f'''<!doctype html>
<!-- Resultatsida för Byathlon 2026.
     Bandata (distans, höjdmeter, höjdprofil) beräknas ur Strava-exporterna
     Rutter/Byathlon 13,5km.tcx och Rutter/Byathlon 5,5km.tcx av
     Rutter/generera-resultat.py — redigera inte den här filen för hand.

     Distansen är Stravas egen <DistanceMeters> längs banan. "Total klättring"
     är summerad uppförsbacke med 2 m brusfilter; eftersom båda banorna är
     rundslingor är nettohöjdskillnaden noll.

     Klassegrare dam/herr är bekräftade av arrangören — könsuppgift finns inte
     i anmälningsdatan.

     Hero-filmen Image/video/start-2026.mp4 är hela drönarklippet från masstarten,
     25,5 sekunder, beskuret ur källans stående ruta (bildytan ligger som 1440x808
     vid y=876 i Image/Dronar bild/StartByathlon2026.mp4) och nedskalat till
     1280x718 för att hela längden ska rymmas på dryga 3 MB. In- och uttoning mot
     svart är inbränd, så loopskarven blir en svart övergång.
     Image/video/start-2026.jpg är samma motiv som stillbild och används bara
     när besökaren bett om mindre rörelse.

     Sidan är självbärande: all CSS ligger i <style> nedan, så src/output.css
     behöver inte byggas om. Inga emojis, bara SVG-ikoner. -->
<html lang="sv">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-ZG424Y5TYS"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {{ dataLayer.push(arguments); }}
      gtag("js", new Date());
      gtag("config", "G-ZG424Y5TYS");
    </script>

    <title>Resultat &mdash; Byathlon 2026 | Sidensj&ouml; 25 juli</title>
    <meta name="description"
      content="Officiella resultat från Byathlon 2026 i Sidensjö. {nl} löpare på {nf(L['km'], 2)} km, {nk} på {nf(K['km'], 2)} km och {nm} i motionsklassen — med banstatistik, tempon och höjdprofiler." />
    <meta name="robots" content="index, follow" />
    <meta name="theme-color" content="#283618" />
    <link rel="canonical" href="https://byathlon.se/resultat.html" />

    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="Byathlon" />
    <meta property="og:locale" content="sv_SE" />
    <meta property="og:url" content="https://byathlon.se/resultat.html" />
    <meta property="og:title" content="Resultat — Byathlon 2026" />
    <meta property="og:description"
      content="{tot_pers} personer i mål, {nf(tot_km)} kilometer och {nf(tot_hm)} höjdmeter. Här är alla resultat från Byathlon 2026." />
    <meta property="og:image" content="https://byathlon.se/Image/Byathlon_Loga.png" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Resultat — Byathlon 2026" />
    <meta name="twitter:image" content="https://byathlon.se/Image/Byathlon_Loga.png" />

    <link href="src/output.css" rel="stylesheet" />
    <link rel="icon" href="Image/HK logo Master Version.svg" type="image/svg+xml" />
    <link rel="apple-touch-icon" href="Image/Byathlon_Loga.png" />
    <link rel="shortcut icon" href="Image/Byathlon_Loga.png" />

    <style>
      /* ═══════════════ DESIGN-TOKENS ═══════════════ */
      :root {{
        --paper: #faf6ee;
        --card: #ffffff;
        --ink: #25231e;
        --ink-soft: #595648;
        --ink-faint: #7f7a67;
        --line: rgba(37, 35, 30, 0.1);
        --line-strong: rgba(37, 35, 30, 0.16);
        --dgreen-800: #25231e;
        --tan-100: #eae1d7;
        --tan-200: #e3d7c9;
        --tan-300: #dbcbb8;

        --lang: #b88f12;
        --lang-line: #eab308;
        --lang-soft: #fbf1d5;
        --kort: #2f8f4e;
        --kort-line: #22c55e;
        --kort-soft: #e4f5e9;
        --motion: #4780a3;
        --motion-line: #669bbc;
        --motion-soft: #dfeaf1;

        --shadow: 0 1px 2px rgba(24, 22, 16, 0.04), 0 6px 24px rgba(24, 22, 16, 0.07);
        --ease: cubic-bezier(0.22, 1, 0.36, 1);
      }}

      html {{ scroll-behavior: smooth; scroll-padding-top: 8.5rem; }}
      body {{ background: var(--paper); color: var(--ink); }}
      .wrap {{ max-width: 68rem; margin: 0 auto; padding: 0 1.25rem; }}
      .mono {{ font-family: ui-monospace, "Cascadia Code", "SF Mono", Menlo, monospace; }}

      /* ═══════════════ NAV ═══════════════ */
      .nav {{
        position: sticky; top: 0; z-index: 60;
        background: rgba(54, 52, 43, 0.96); backdrop-filter: blur(10px);
        box-shadow: 0 2px 14px rgba(24, 22, 16, 0.18);
      }}
      .nav-in {{
        max-width: 68rem; margin: 0 auto; padding: 0.75rem 1.25rem;
        display: flex; align-items: center; justify-content: space-between; gap: 1rem;
      }}
      .nav-brand {{ display: flex; align-items: center; gap: 0.7rem; text-decoration: none; }}
      .nav-brand img {{ height: 2.25rem; width: 2.25rem; }}
      .nav-brand span {{ color: var(--tan-100); font-size: 1.2rem; font-weight: 700; letter-spacing: 0.02em; }}
      .nav-back {{ color: var(--tan-200); font-size: 0.875rem; font-weight: 500; text-decoration: none; transition: color 0.2s; }}
      .nav-back:hover {{ color: #efca5c; }}

      /* ═══════════════ HERO ═══════════════ */
      /* Dronarklippet fran starten tacker hela sektionen och loopar. Klippet
         tonar in och ut mot svart, sa loopskarven blir en svart overgang. */
      .hero {{
        position: relative; overflow: hidden; isolation: isolate;
        background: #14130e; color: #fff;
        min-height: min(84vh, 46rem);
        display: flex; align-items: center;
        padding: 5rem 0 4rem;
      }}
      .hero-film {{
        position: absolute; inset: 0; z-index: 0;
        width: 100%; height: 100%; object-fit: cover;
        pointer-events: none; user-select: none;
      }}
      /* Sloja sa den vita texten haller sig lasbar aven over MAL-bagen och
         de utbranda vita partierna i klippet. */
      .hero-sloja {{
        position: absolute; inset: 0; z-index: 1; pointer-events: none;
        background:
          linear-gradient(180deg, rgba(16, 15, 11, 0.8) 0%, rgba(16, 15, 11, 0.48) 34%,
                          rgba(16, 15, 11, 0.58) 72%, rgba(16, 15, 11, 0.92) 100%),
          radial-gradient(ellipse 76% 66% at 50% 46%, rgba(16, 15, 11, 0.26), rgba(16, 15, 11, 0.68));
      }}
      .hero-in {{ position: relative; z-index: 2; width: 100%; text-align: center; }}
      /* Ljusare gult och gradbrutet an ovrig text pa sidan: den har texten star
         over rorlig bild och maste klara klippets ljusaste ogonblick. */
      .kicker {{
        font-family: ui-monospace, monospace; font-size: 0.62rem; font-weight: 600;
        letter-spacing: 0.35em; text-transform: uppercase; color: #f7d977; margin-bottom: 1rem;
        text-shadow: 0 1px 12px rgba(10, 9, 6, 0.6);
      }}
      .hero h1 {{
        font-size: clamp(2.5rem, 8vw, 4.25rem); font-weight: 800;
        line-height: 1.02; letter-spacing: -0.02em; margin-bottom: 0.9rem;
        text-shadow: 0 2px 26px rgba(10, 9, 6, 0.5), 0 1px 3px rgba(10, 9, 6, 0.45);
      }}
      .hero-sub {{
        color: #f8f3ec; font-size: 1.02rem; max-width: 40rem; margin: 0 auto;
        text-shadow: 0 1px 10px rgba(10, 9, 6, 0.65);
      }}

      .tiles {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.75rem; margin-top: 2.5rem; }}
      @media (min-width: 720px) {{ .tiles {{ grid-template-columns: repeat(4, 1fr); }} }}
      .tile {{
        background: rgba(18, 17, 12, 0.36); border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 14px; padding: 1rem 0.75rem; backdrop-filter: blur(7px);
      }}
      .tile-v {{
        font-size: clamp(1.4rem, 4.5vw, 1.9rem); font-weight: 800; line-height: 1.1;
        text-shadow: 0 1px 8px rgba(10, 9, 6, 0.5);
      }}
      .tile-l {{
        font-family: ui-monospace, monospace; font-size: 0.58rem; font-weight: 600;
        letter-spacing: 0.18em; text-transform: uppercase; color: var(--tan-300); margin-top: 0.4rem;
      }}

      /* ═══════════════ SÖKFÄLT ═══════════════ */
      .sokrad {{
        position: sticky; top: 3.75rem; z-index: 50;
        background: rgba(250, 246, 238, 0.93); backdrop-filter: blur(10px);
        border-bottom: 1px solid var(--line); padding: 0.7rem 0;
      }}
      .sok-in {{ max-width: 68rem; margin: 0 auto; padding: 0 1.25rem; display: flex; gap: 0.6rem; align-items: center; }}
      .sok-falt {{
        flex: 1; display: flex; align-items: center; gap: 0.55rem;
        background: #fff; border: 1px solid var(--line-strong); border-radius: 11px;
        padding: 0.55rem 0.85rem; box-shadow: 0 1px 2px rgba(24, 22, 16, 0.04);
        transition: border-color 0.2s, box-shadow 0.2s;
      }}
      .sok-falt:focus-within {{ border-color: #a8b875; box-shadow: 0 0 0 3px rgba(168, 184, 117, 0.22); }}
      .sok-falt > svg {{ width: 1.05rem; height: 1.05rem; color: var(--ink-faint); flex: none; }}
      .sok-falt input {{
        flex: 1; border: 0; outline: 0; background: transparent;
        font-size: 0.95rem; color: var(--ink); min-width: 0;
        appearance: none; -webkit-appearance: none;
      }}
      .sok-falt input::-webkit-search-decoration,
      .sok-falt input::-webkit-search-cancel-button {{ -webkit-appearance: none; appearance: none; }}
      .sok-rensa {{
        border: 0; background: transparent; cursor: pointer; padding: 0.15rem 0.3rem;
        color: var(--ink-faint); line-height: 0; display: none;
      }}
      .sok-rensa svg {{ width: 1rem; height: 1rem; }}
      .sok-rensa:hover {{ color: var(--ink); }}
      .sok-status {{ font-family: ui-monospace, monospace; font-size: 0.7rem; color: var(--ink-faint); white-space: nowrap; }}
      @media (max-width: 560px) {{ .sok-status {{ display: none; }} }}

      /* ═══════════════ SEKTION ═══════════════ */
      .sektion {{ padding: 3.5rem 0 1rem; }}
      .sek-huvud {{ display: flex; align-items: flex-end; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.5rem; }}
      .sek-etikett {{
        font-family: ui-monospace, monospace; font-size: 0.6rem; font-weight: 700;
        letter-spacing: 0.3em; text-transform: uppercase; margin-bottom: 0.45rem;
      }}
      .sek-huvud h2 {{ font-size: clamp(1.85rem, 5vw, 2.6rem); font-weight: 800; letter-spacing: -0.015em; line-height: 1.05; }}
      .sek-dist {{
        font-family: ui-monospace, monospace; font-size: 0.95rem; font-weight: 700;
        padding: 0.3rem 0.7rem; border-radius: 999px; margin-left: auto; white-space: nowrap;
      }}

      .kort-panel {{ background: var(--card); border: 1px solid var(--line); border-radius: 18px; box-shadow: var(--shadow); overflow: hidden; }}
      .band {{ height: 5px; }}

      /* ── banfakta ── */
      .banfakta {{ padding: 1.5rem 1.5rem 0.5rem; }}
      .banfakta > h3 {{
        font-family: ui-monospace, monospace; font-size: 0.6rem; font-weight: 700;
        letter-spacing: 0.28em; text-transform: uppercase; color: var(--ink-faint); margin-bottom: 1rem;
      }}
      .chips {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.6rem; }}
      @media (min-width: 640px) {{ .chips {{ grid-template-columns: repeat(3, 1fr); }} }}
      @media (min-width: 960px) {{ .chips {{ grid-template-columns: repeat(6, 1fr); }} }}
      .chip {{ background: var(--paper); border: 1px solid var(--line); border-radius: 12px; padding: 0.85rem 0.7rem; text-align: center; }}
      .chip-i {{ width: 1.25rem; height: 1.25rem; display: block; margin: 0 auto 0.5rem; color: var(--ink-faint); }}
      .chip-v {{ display: block; font-weight: 800; font-size: 1.02rem; letter-spacing: -0.01em; }}
      .chip-l {{
        display: block; font-family: ui-monospace, monospace; font-size: 0.55rem;
        font-weight: 600; letter-spacing: 0.13em; text-transform: uppercase;
        color: var(--ink-faint); margin-top: 0.3rem; line-height: 1.35;
      }}

      /* ── höjdprofil ── */
      .profil {{ margin: 1.25rem 1.5rem 0; }}
      .profil svg {{ width: 100%; height: 92px; display: block; }}
      .profil-txt {{
        display: flex; justify-content: space-between; gap: 0.5rem;
        font-family: ui-monospace, monospace; font-size: 0.62rem;
        color: var(--ink-faint); margin-top: 0.3rem; letter-spacing: 0.04em;
      }}
      .profil-topp {{ font-weight: 700; }}

      /* ── brödtext ── */
      .berattelse {{ padding: 1.5rem; border-top: 1px solid var(--line); margin-top: 1.25rem; }}
      .berattelse p {{ color: var(--ink-soft); line-height: 1.7; max-width: 46rem; }}
      .berattelse p + p {{ margin-top: 0.85rem; }}
      .berattelse strong {{ color: var(--ink); font-weight: 700; }}

      /* ═══════════════ TABELL ═══════════════ */
      .tabellsvep {{ overflow-x: auto; -webkit-overflow-scrolling: touch; }}
      table {{ width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; }}
      thead th {{
        font-family: ui-monospace, monospace; font-size: 0.57rem; font-weight: 700;
        letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink-faint);
        text-align: left; padding: 0.7rem 0.6rem; border-bottom: 1px solid var(--line-strong);
        background: var(--paper);
      }}
      thead th:first-child {{ padding-left: 1.5rem; }}
      thead th:last-child {{ padding-right: 1.5rem; }}
      th.h-tid, th.h-tempo {{ text-align: right; }}
      tbody td {{ padding: 0.62rem 0.6rem; border-bottom: 1px solid var(--line); font-size: 0.94rem; }}
      tbody tr:last-child td {{ border-bottom: 0; }}
      tbody tr {{ transition: background 0.15s; }}
      tbody tr:hover {{ background: var(--paper); }}
      .plac {{ padding-left: 1.5rem !important; width: 4.5rem; font-family: ui-monospace, monospace; font-weight: 700; color: var(--ink-soft); }}
      .nr {{ width: 3.5rem; font-family: ui-monospace, monospace; color: var(--ink-faint); font-size: 0.85rem; }}
      .namn {{ font-weight: 600; }}
      .tid {{ text-align: right; font-family: ui-monospace, monospace; font-weight: 700; width: 6.5rem; }}
      .tempo {{ text-align: right; padding-right: 1.5rem !important; width: 6rem; font-family: ui-monospace, monospace; font-size: 0.82rem; color: var(--ink-faint); }}
      .tie {{
        font-family: ui-monospace, monospace; font-size: 0.52rem; font-weight: 700;
        letter-spacing: 0.1em; text-transform: uppercase; color: var(--ink-faint);
        background: var(--tan-100); border-radius: 4px; padding: 0.1rem 0.28rem; vertical-align: middle;
      }}

      /* ── klassegrare dam/herr ── */
      tr.seger {{ background: linear-gradient(90deg, rgba(235, 189, 51, 0.14), transparent 68%); }}
      tr.seger:hover {{ background: linear-gradient(90deg, rgba(235, 189, 51, 0.2), transparent 68%); }}
      tr.seger .namn {{ font-weight: 800; }}
      tr.seger .tid {{ font-size: 1rem; }}
      .vinnare {{
        display: inline-flex; align-items: center; gap: 0.28rem; margin-left: 0.55rem;
        font-family: ui-monospace, monospace; font-size: 0.55rem; font-weight: 700;
        letter-spacing: 0.13em; text-transform: uppercase; white-space: nowrap;
        color: #7d6208; background: #fbf1d5; border: 1px solid rgba(209, 162, 21, 0.35);
        border-radius: 999px; padding: 0.16rem 0.5rem 0.16rem 0.36rem; vertical-align: 1px;
      }}
      .v-i {{ width: 0.8rem; height: 0.8rem; flex: none; }}
      tr.dold {{ display: none; }}

      .tab-fot {{ padding: 0.9rem 1.5rem 1.25rem; border-top: 1px solid var(--line); font-size: 0.8rem; color: var(--ink-faint); background: var(--paper); }}
      .ingen-traff {{ padding: 2rem 1.5rem; text-align: center; color: var(--ink-faint); font-size: 0.9rem; display: none; }}
      .ingen-traff.visa {{ display: block; }}

      /* ═══════════════ UTOM TÄVLAN ═══════════════ */
      .utom-lista {{ list-style: none; margin: 0; padding: 1.5rem; display: grid; gap: 0.75rem; }}
      .utom-post {{
        background: var(--paper); border: 1px dashed var(--line-strong);
        border-radius: 13px; padding: 1rem 1.1rem;
      }}
      .utom-post.dold {{ display: none; }}
      .utom-topp {{ display: flex; align-items: baseline; gap: 0.75rem; flex-wrap: wrap; }}
      .utom-nr {{
        font-family: ui-monospace, monospace; font-size: 0.72rem; font-weight: 700;
        color: var(--ink-faint); background: var(--tan-100); border-radius: 7px;
        padding: 0.25rem 0.45rem; flex: none;
      }}
      .utom-namn {{ font-weight: 700; font-size: 1rem; }}
      .utom-tid {{
        margin-left: auto; font-family: ui-monospace, monospace;
        font-weight: 700; font-size: 1rem; font-variant-numeric: tabular-nums;
      }}
      .utom-notis {{ color: var(--ink-soft); font-size: 0.88rem; margin-top: 0.5rem; line-height: 1.55; }}
      .utom-jamf {{ color: var(--ink-faint); font-size: 0.82rem; margin-top: 0.3rem; line-height: 1.55; }}
      .utom-jamf strong {{ color: var(--ink-soft); }}

      /* ═══════════════ MOTION ═══════════════ */
      .motion-lista {{
        list-style: none; padding: 1.5rem; margin: 0;
        display: grid; grid-template-columns: repeat(auto-fill, minmax(15rem, 1fr)); gap: 0.6rem;
      }}
      .deltagare {{
        display: flex; align-items: center; gap: 0.75rem;
        background: var(--paper); border: 1px solid var(--line); border-radius: 11px;
        padding: 0.65rem 0.85rem; transition: transform 0.25s var(--ease), box-shadow 0.25s var(--ease);
      }}
      .deltagare:hover {{ transform: translateY(-2px); box-shadow: var(--shadow); }}
      .deltagare.dold {{ display: none; }}
      .d-nr {{
        font-family: ui-monospace, monospace; font-size: 0.72rem; font-weight: 700;
        color: var(--motion); background: var(--motion-soft); border-radius: 7px;
        padding: 0.25rem 0.45rem; flex: none;
      }}
      .d-namn {{ font-weight: 600; font-size: 0.93rem; }}

      /* ═══════════════ STATISTIK ═══════════════ */
      .statlista {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 0.7rem; }}
      @media (min-width: 760px) {{ .statlista {{ grid-template-columns: 1fr 1fr; }} }}
      .statlista li {{
        background: var(--card); border: 1px solid var(--line); border-radius: 13px;
        padding: 1rem 1.1rem; display: flex; gap: 0.85rem; align-items: flex-start;
        line-height: 1.55; color: var(--ink-soft); font-size: 0.93rem;
      }}
      .stat-v {{ font-family: ui-monospace, monospace; font-weight: 800; font-size: 1.02rem; color: var(--ink); flex: none; letter-spacing: -0.02em; }}
      .statlista strong {{ color: var(--ink); }}

      /* ═══════════════ KÄLLA & FOT ═══════════════ */
      .kalla {{
        margin-top: 3rem; padding: 1.25rem 1.4rem; border-radius: 13px;
        background: var(--tan-100); border: 1px solid var(--line);
        font-size: 0.8rem; color: var(--ink-soft); line-height: 1.65;
      }}
      .kalla h4 {{
        font-family: ui-monospace, monospace; font-size: 0.58rem; font-weight: 700;
        letter-spacing: 0.24em; text-transform: uppercase; color: var(--ink-faint); margin-bottom: 0.5rem;
      }}
      .kalla p + p {{ margin-top: 0.7rem; }}
      footer {{ background: var(--dgreen-800); color: var(--tan-300); padding: 3.5rem 0 2rem; margin-top: 4rem; text-align: center; }}
      footer .brand {{ display: flex; justify-content: center; align-items: center; gap: 0.75rem; margin-bottom: 1rem; }}
      footer .brand img {{ height: 3rem; width: 3rem; }}
      footer .brand span {{ font-size: 1.75rem; font-weight: 700; color: var(--tan-100); letter-spacing: 0.02em; }}
      footer .devis {{
        font-family: ui-monospace, monospace; font-size: 0.6rem; font-weight: 600;
        letter-spacing: 0.35em; text-transform: uppercase; color: #efca5c; margin-bottom: 1.25rem;
      }}
      footer a {{ color: var(--tan-200); text-decoration: underline; text-underline-offset: 4px; }}
      footer a:hover {{ color: #efca5c; }}
      .fot-lank {{ margin-top: 1.5rem; font-size: 0.85rem; }}

      @media (prefers-reduced-motion: reduce) {{
        html {{ scroll-behavior: auto; }}
        * {{ transition: none !important; }}
        .hero-film {{ display: none; }}
        .hero {{ background: #14130e url("Image/video/start-2026.jpg") center / cover no-repeat; }}
      }}
      /* Webblasare skriver inte ut bakgrundsfarger som standard. Hero maste
         darfor byta till mork text pa vitt, annars forsvinner rubriken helt. */
      @media print {{
        .nav, .sokrad, footer, .hero-film, .hero-sloja {{ display: none !important; }}
        .hero {{ min-height: 0; padding: 1.5rem 0 1rem; background: none; color: var(--ink); }}
        .hero h1, .hero-sub, .kicker, .tile-v {{ text-shadow: none; }}
        .kicker {{ color: #6b5a12; }}
        .hero-sub {{ color: var(--ink-soft); }}
        .tiles {{ margin-top: 1.25rem; }}
        .tile {{ background: none; border-color: #ccc; backdrop-filter: none; }}
        .tile-l {{ color: var(--ink-faint); }}
        body {{ background: #fff; }}
        .kort-panel {{ box-shadow: none; border-color: #ccc; break-inside: avoid; }}
        .sektion {{ padding-top: 1.5rem; }}
      }}
    </style>
  </head>

  <body class="font-sans">
    <nav class="nav">
      <div class="nav-in">
        <a href="index.html" class="nav-brand">
          <img src="Image/Byathlon_Loga.png" alt="Byathlon logotyp" width="36" height="36" />
          <span>Byathlon</span>
        </a>
        <a href="index.html" class="nav-back">&larr; Till startsidan</a>
      </div>
    </nav>

    <!-- ═══════════════ HERO ═══════════════ -->
    <header class="hero">
      <!-- Medvetet utan poster: filmens forsta bildruta ar helsvart och .hero ar
           redan nastan svart, sa filmen tonar upp ur bakgrunden i stallet for att
           blinka till fran en ljus stillbild. Stillbilden anvands vid reduced-motion. -->
      <video class="hero-film" autoplay muted loop playsinline preload="auto"
             aria-hidden="true" tabindex="-1"
             disablepictureinpicture disableremoteplayback>
        <source src="Image/video/start-2026.mp4" type="video/mp4" />
      </video>
      <div class="hero-sloja"></div>
      <div class="wrap hero-in">
        <p class="kicker">25 juli 2026 &middot; By badplats &middot; Sidensj&ouml;veckan</p>
        <h1>Resultat<br />Byathlon&nbsp;2026</h1>
        <p class="hero-sub">
          {tot_pers} personer tog sig runt banorna genom Sidensj&ouml;bygden &mdash; fr&aring;n badplatsen
          vid sj&ouml;n, upp i h&ouml;jderna och tillbaka ner till bastun. Grattis till er alla.
        </p>
        <div class="tiles">
          <div class="tile"><div class="tile-v">{tot_pers}</div><div class="tile-l">I m&aring;l</div></div>
          <div class="tile"><div class="tile-v">{nf(tot_km)} km</div><div class="tile-l">Sammanlagt</div></div>
          <div class="tile"><div class="tile-v">{nf(tot_hm)}</div><div class="tile-l">H&ouml;jdmeter</div></div>
          <div class="tile"><div class="tile-v">{tot_h} h {tot_m} min</div><div class="tile-l">Total l&ouml;ptid</div></div>
        </div>
      </div>
    </header>

    <!-- ═══════════════ SÖK ═══════════════ -->
    <div class="sokrad">
      <div class="sok-in">
        <label class="sok-falt">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
               stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7" /><path d="m20 20-3.6-3.6" /></svg>
          <input id="sok" type="search" autocomplete="off"
                 placeholder="S&ouml;k p&aring; namn eller startnummer&hellip;" aria-label="S&ouml;k bland deltagarna" />
          <button type="button" class="sok-rensa" id="rensa" aria-label="Rensa s&ouml;kningen">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                 stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18" /></svg>
          </button>
        </label>
        <span class="sok-status" id="sok-status">{tot_pers} deltagare</span>
      </div>
    </div>

    <main class="wrap">
      <!-- ═══════════════ LÅNG ═══════════════ -->
      <section class="sektion" id="lang">
        <div class="sek-huvud">
          <div>
            <p class="sek-etikett" style="color: var(--lang)">L&aring;ng distans</p>
            <h2>{nf(L['km'], 2)} kilometer</h2>
          </div>
          <span class="sek-dist" style="background: var(--lang-soft); color: var(--lang)">{nl} i m&aring;l</span>
        </div>

        <div class="kort-panel">
          <div class="band" style="background: var(--lang-line)"></div>

          <div class="banfakta">
            <h3>Banan i siffror</h3>
            <div class="chips">
{statchip("distans", nf(L["km"], 2) + "&nbsp;km", "Distans")}
{statchip("klattring", nf(L["upp"]) + "&nbsp;m", "Total kl&auml;ttring")}
{statchip("netto", "&plusmn;0&nbsp;m", "Nettoh&ouml;jd &mdash; rundslinga")}
{statchip("topp", nf(L["hi"]) + "&nbsp;m", "H&ouml;gsta punkt &ouml;.h.")}
{statchip("lutning", nf(L["hm_km"], 1) + "&nbsp;m", "Kl&auml;ttring per km")}
{statchip("brant", nf(L["brant"], 1) + "&nbsp;%", "Brantaste partiet")}
            </div>
          </div>

{profil_svg(L, "lang", "#eab308")}

          <div class="berattelse">
            <p>
              Banan sparar inte p&aring; krutet. Redan under f&ouml;rsta kilometern b&ouml;rjar det b&auml;ra upp&aring;t,
              och fram till km 1,81 kl&auml;ttras {nf(L['hi'] - 117)} h&ouml;jdmeter upp till banans h&ouml;gsta punkt p&aring;
              {nf(L['hi'])} meter &ouml;ver havet. D&auml;refter b&auml;r det v&auml;sterut, drygt fyra kilometer f&aring;gelv&auml;gen
              fr&aring;n start, innan slingan v&auml;nder hem&aring;t.
            </p>
            <p>
              Banan &auml;r en rundslinga, s&aring; du slutar exakt d&auml;r du b&ouml;rjade &mdash; men d&auml;remellan ligger
              <strong>{nf(L['upp'])} h&ouml;jdmeter uppf&ouml;r och lika m&aring;nga nedf&ouml;r</strong>. Tv&aring; tredjedelar av stigningen
              ligger i f&ouml;rsta halvan, s&aring; den som orkade h&aring;lla emot i backarna fick betalt sedan: efter
              v&auml;ndpunkten rullar banan l&auml;ttare och de sista kilometrarna faller stadigt ner mot sj&ouml;n igen.
            </p>
            <p>
              <strong>Steffen Dalsgaard</strong> utnyttjade det till fullo: {LANG[0][3][3:]} &ouml;ver {nf(L['km'], 2)} km betyder
              <strong>4:00 min/km</strong> hela v&auml;gen &mdash; n&auml;stan tio minuter f&ouml;re tv&aring;an. Snabbaste dam blev
              <strong>Karin H&auml;gglund</strong> p&aring; 1:06:09, femma totalt.
            </p>
          </div>

          <div class="tabellsvep">
            <table>
              <caption class="sr-only">Resultat l&aring;ng distans, {nf(L['km'], 2)} km</caption>
              <thead>
                <tr>
                  <th scope="col">Plac</th>
                  <th scope="col">Nr</th>
                  <th scope="col">Namn</th>
                  <th scope="col" class="h-tid">Tid</th>
                  <th scope="col" class="h-tempo">Min/km</th>
                </tr>
              </thead>
              <tbody data-tabell>
{rows(LANG, L["km"], VINNARE["lang"])}
              </tbody>
            </table>
          </div>
          <p class="ingen-traff" data-tom>Ingen tr&auml;ff i den h&auml;r klassen.</p>
          <p class="tab-fot">
            {nl} i m&aring;l &middot; mediantid {hhmmss(4642)} ({pace(4642, L['km'])} min/km) &middot;
            nio l&ouml;pare under 1:10 och trettiotv&aring; under 1:30.
          </p>
        </div>
      </section>

      <!-- ═══════════════ KORT ═══════════════ -->
      <section class="sektion" id="kort">
        <div class="sek-huvud">
          <div>
            <p class="sek-etikett" style="color: var(--kort)">Kort distans</p>
            <h2>{nf(K['km'], 2)} kilometer</h2>
          </div>
          <span class="sek-dist" style="background: var(--kort-soft); color: var(--kort)">{nk} i m&aring;l</span>
        </div>

        <div class="kort-panel">
          <div class="band" style="background: var(--kort-line)"></div>

          <div class="banfakta">
            <h3>Banan i siffror</h3>
            <div class="chips">
{statchip("distans", nf(K["km"], 2) + "&nbsp;km", "Distans")}
{statchip("klattring", nf(K["upp"]) + "&nbsp;m", "Total kl&auml;ttring")}
{statchip("netto", "&plusmn;0&nbsp;m", "Nettoh&ouml;jd &mdash; rundslinga")}
{statchip("topp", nf(K["hi"]) + "&nbsp;m", "H&ouml;gsta punkt &ouml;.h.")}
{statchip("lutning", nf(K["hm_km"], 1) + "&nbsp;m", "Kl&auml;ttring per km")}
{statchip("brant", nf(K["brant"], 1) + "&nbsp;%", "Brantaste partiet")}
            </div>
          </div>

{profil_svg(K, "kort", "#22c55e")}

          <div class="berattelse">
            <p>
              Kort betyder inte l&auml;tt. Kortbanan &auml;r den brantaste av de tv&aring; &mdash; den kl&auml;ttrar rakt upp
              fr&aring;n sj&ouml;n till <strong>{nf(K['hi'])} meter &ouml;ver havet</strong>, allts&aring; {nf(K['hi'] - L['hi'])} meter h&ouml;gre &auml;n vad
              l&aring;ngbanan n&aring;gonsin n&aring;r. R&auml;knat per kilometer kl&auml;ttrar den
              <strong>{nf(K['hm_km'] / L['hm_km'], 1)} g&aring;nger s&aring; mycket</strong> som l&aring;nga banan:
              {nf(K['hm_km'], 1)} mot {nf(L['hm_km'], 1)} h&ouml;jdmeter per kilometer.
            </p>
            <p>
              I praktiken &auml;r det <em>en enda</em> stigning: {nf(K['hi'] - 118)} h&ouml;jdmeter fr&aring;n startlinjen upp till
              toppen vid km {nf(K['hi_km'], 2)}, med {nf(K['brant'], 1)} procents lutning som brantast kring km {nf(K['brant_km'], 2)}.
              Efter toppen v&auml;ntar en enda l&aring;ng utf&ouml;rsl&ouml;pning hem mot bastun &mdash; h&aring;ll bara benen kvar under dig.
            </p>
            <p>
              <strong>Anton H&auml;gglund</strong> vann p&aring; {KORT[0][3][3:]} &mdash; {pace(secs(KORT[0][3]), K['km'])} min/km &mdash;
              efter en tajt duell med P&auml;r&nbsp;Bystr&ouml;m, 21 sekunder bakom. Snabbaste dam blev
              <strong>Louise Bystr&ouml;m</strong> p&aring; 29:42, fj&auml;rde plats totalt och tv&aring; sekunder f&ouml;re Hanna&nbsp;Bystr&ouml;m.
            </p>
          </div>

          <div class="tabellsvep">
            <table>
              <caption class="sr-only">Resultat kort distans, {nf(K['km'], 2)} km</caption>
              <thead>
                <tr>
                  <th scope="col">Plac</th>
                  <th scope="col">Nr</th>
                  <th scope="col">Namn</th>
                  <th scope="col" class="h-tid">Tid</th>
                  <th scope="col" class="h-tempo">Min/km</th>
                </tr>
              </thead>
              <tbody data-tabell>
{rows(KORT, K["km"], VINNARE["kort"])}
              </tbody>
            </table>
          </div>
          <p class="ingen-traff" data-tom>Ingen tr&auml;ff i den h&auml;r klassen.</p>
          <p class="tab-fot">
            {nk} i m&aring;l &middot; mediantid {hhmmss(2000)} ({pace(2000, K['km'])} min/km) &middot;
            t&auml;tast i f&auml;ltet: fr&aring;n 12:e till 15:e plats skiljde bara 6 sekunder.
          </p>
        </div>
      </section>

      <!-- ═══════════════ UTOM TÄVLAN ═══════════════ -->
      <section class="sektion" id="utom">
        <div class="sek-huvud">
          <div>
            <p class="sek-etikett" style="color: var(--ink-faint)">Utom t&auml;vlan</p>
            <h2>Banan p&aring; egen hand</h2>
          </div>
          <span class="sek-dist" style="background: var(--tan-100); color: var(--ink-soft)">{len(UTOM)} l&ouml;pare</span>
        </div>

        <div class="kort-panel">
          <div class="band" style="background: var(--tan-300)"></div>
          <div class="berattelse" style="border-top: 0; margin-top: 0">
            <p>
              N&aring;gra av dem som fick loppet att fungera hann aldrig springa det. H&auml;r &auml;r de som
              tog sig runt banan p&aring; egen hand en annan dag &mdash; utanf&ouml;r tidtagningen, men v&auml;l v&auml;rda
              sin plats p&aring; sidan.
            </p>
          </div>
          <ul class="utom-lista">
{utom_block(K["km"], KORT)}
          </ul>
        </div>
      </section>

      <!-- ═══════════════ MOTION ═══════════════ -->
      <section class="sektion" id="motion">
        <div class="sek-huvud">
          <div>
            <p class="sek-etikett" style="color: var(--motion)">Motion</p>
            <h2>Alla som tog sig runt</h2>
          </div>
          <span class="sek-dist" style="background: var(--motion-soft); color: var(--motion)">{nm} deltagare</span>
        </div>

        <div class="kort-panel">
          <div class="band" style="background: var(--motion-line)"></div>

          <div class="banfakta">
            <h3>Banan i siffror</h3>
            <div class="chips">
{statchip("distans", nf(K["km"], 2) + "&nbsp;km", "Samma bana som kort")}
{statchip("klattring", nf(K["upp"]) + "&nbsp;m", "Total kl&auml;ttring")}
{statchip("topp", nf(K["hi"]) + "&nbsp;m", "Byathlons h&ouml;gsta punkt")}
{statchip("tass", "V&auml;lkomna", "Hundar")}
{statchip("urtavla", "Ingen", "Tidtagning")}
{statchip("bastu", "Efter&aring;t", "Bastu &amp; bad")}
            </div>
          </div>

          <div class="berattelse">
            <p>
              Motionsklassen handlar om en enda sak: att ta sig runt. Samma backar, samma utsikt fr&aring;n
              {nf(K['hi'])} meter, samma dopp i sj&ouml;n efter&aring;t &mdash; men helt utan klocka. H&auml;r g&aring;r man, pratar,
              stannar och tittar, och kommer i m&aring;l precis lika mycket som alla andra.
            </p>
            <p>
              Att g&aring; eller springa {nf(K['km'], 2)} kilometer med {nf(K['upp'])} h&ouml;jdmeter &auml;r en riktig prestation,
              oavsett vad urtavlan s&auml;ger. <strong>Stort hurra till er alla.</strong>
            </p>
          </div>

          <ul class="motion-lista" data-tabell>
{motion_lista()}
          </ul>
          <p class="ingen-traff" data-tom>Ingen tr&auml;ff i den h&auml;r klassen.</p>
          <p class="tab-fot">{nm} deltagare runt banan.</p>
        </div>
      </section>

      <!-- ═══════════════ STATISTIK ═══════════════ -->
      <section class="sektion" id="statistik">
        <div class="sek-huvud">
          <div>
            <p class="sek-etikett" style="color: var(--ink-faint)">Kul att veta</p>
            <h2>Dagen i siffror</h2>
          </div>
        </div>

        <ul class="statlista">
          <li><span class="stat-v">{tot_pers}</span><span>personer i m&aring;l &mdash; {nl} p&aring; {nf(L['km'], 2)} km, {nk} p&aring; {nf(K['km'], 2)} km och {nm} i motionsklassen.</span></li>
          <li><span class="stat-v">{nf(tot_km)} km</span><span>sammanlagt tillryggalagda. Det &auml;r v&auml;gen h&auml;rifr&aring;n ner till Stockholm och en bra bit tillbaka igen.</span></li>
          <li><span class="stat-v">{nf(tot_hm)} m</span><span>kl&auml;ttrade tillsammans &mdash; motsvarande <strong>{nf(tot_hm / 2097, 1)} bestigningar av Kebnekaise</strong>.</span></li>
          <li><span class="stat-v">4:00</span><span>min/km &mdash; Steffen Dalsgaards snitt &ouml;ver hela l&aring;ngbanan, p&aring; sekunden j&auml;mnt.</span></li>
          <li><span class="stat-v">+{nf(K['hi'] - L['hi'])} m</span><span>h&ouml;gre n&aring;r <strong>kortbanan</strong> ({nf(K['hi'])} m &ouml;.h.) &auml;n l&aring;ngbanan ({nf(L['hi'])} m &ouml;.h.). Kort &auml;r inte detsamma som platt.</span></li>
          <li><span class="stat-v">{nf(K['brant'], 1)} %</span><span>brantaste lutningen p&aring; hela Byathlon, vid km {nf(K['brant_km'], 2)} p&aring; kortbanan.</span></li>
          <li><span class="stat-v">3 st</span><span>delade placeringar, alla p&aring; samma sekund &mdash; d&auml;ribland Albin och Anna Bj&ouml;rkqvist som gick i m&aring;l tillsammans p&aring; 48:00.</span></li>
          <li><span class="stat-v">1 sek</span><span>skiljde Lukas Palm och Vega Kjellsson om nionde platsen p&aring; korta banan &mdash; dagens minsta marginal.</span></li>
          <li><span class="stat-v">37 sek</span><span>skiljde Julia, Victor och Lova H&ouml;glund i m&aring;l p&aring; l&aring;nga banan, efter &ouml;ver tv&aring; timmar p&aring; benen.</span></li>
        </ul>

        <div class="kalla">
          <h4>Om siffrorna</h4>
          <p>
            Distanser, h&ouml;jdmeter och h&ouml;jdprofiler kommer fr&aring;n de officiella banorna p&aring; Strava.
            Distansen &auml;r Stravas egen uppm&auml;tning l&auml;ngs banan: {nf(L['km'] * 1000)}&nbsp;m respektive
            {nf(K['km'] * 1000)}&nbsp;m. Tempot i tabellerna &auml;r r&auml;knat p&aring; dessa distanser.
          </p>
          <p>
            <strong>Total kl&auml;ttring</strong> &auml;r all uppf&ouml;rsbacke adderad, inte skillnaden mellan start och m&aring;l.
            B&aring;da banorna &auml;r rundslingor som b&ouml;rjar och slutar p&aring; samma st&auml;lle, s&aring; nettoh&ouml;jdskillnaden &auml;r noll
            &mdash; men l&aring;ngbanan bjuder &auml;nd&aring; p&aring; {nf(L['upp'])} meter uppf&ouml;r och {nf(L['upp'])} meter nedf&ouml;r p&aring; v&auml;gen.
            <strong>Kl&auml;ttring per km</strong> &auml;r den summan delad med distansen, och &auml;r m&aring;ttet som g&ouml;r banorna
            j&auml;mf&ouml;rbara: {nf(K['hm_km'], 1)} m/km p&aring; korta mot {nf(L['hm_km'], 1)} m/km p&aring; l&aring;nga.
            Sm&aring; GPS-hopp filtreras bort med en tv&aring;metersgr&auml;ns.
          </p>
          <p>
            Klassegrarna dam och herr &auml;r bekr&auml;ftade av arrang&ouml;ren &mdash; k&ouml;n registreras inte vid anm&auml;lan.
            Deltagare som inte startade &auml;r borttagna ur listorna.
          </p>
        </div>
      </section>
    </main>

    <footer>
      <div class="wrap">
        <div class="brand">
          <img src="Image/Byathlon_Loga.png" alt="Byathlon logotyp" width="48" height="48" loading="lazy" />
          <span>Byathlon</span>
        </div>
        <p class="devis">Spring &middot; G&aring; &middot; Bada</p>
        <p style="font-size: 0.9rem; max-width: 34rem; margin: 0 auto">
          Tack till alla deltagare, funktion&auml;rer och publik som gjorde Byathlon 2026 till vad det blev
          &mdash; och tack till v&aring;ra sponsorer. Vi ses vid startlinjen n&auml;sta &aring;r.
        </p>
        <p class="fot-lank">
          <a href="index.html">Till startsidan</a> &nbsp;&middot;&nbsp;
          <a href="omradeskarta.html">Omr&aring;deskarta</a>
        </p>
        <p style="margin-top: 2rem; font-size: 0.75rem; opacity: 0.65">By Intressef&ouml;rening</p>
      </div>
    </footer>

    <script>
      // Dronarfilmen i hero: sta still om besokaren bett om mindre rorelse,
      // och forsok igen om webblasaren blockerar autospelningen.
      (function () {{
        var film = document.querySelector(".hero-film");
        if (!film) return;
        if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {{
          film.removeAttribute("autoplay");
          film.pause();
          return;
        }}
        var spela = function () {{
          var p = film.play();
          if (p && p.catch) p.catch(function () {{}});
        }};
        spela();
        document.addEventListener("visibilitychange", function () {{
          if (!document.hidden) spela();
        }});
      }})();

      // Live-filtrering: matchar mot namn och startnummer i data-sok.
      (function () {{
        var falt = document.getElementById("sok");
        var rensa = document.getElementById("rensa");
        var status = document.getElementById("sok-status");
        var poster = Array.prototype.slice.call(document.querySelectorAll("[data-sok]"));
        var block = Array.prototype.slice.call(document.querySelectorAll("[data-tabell]"));
        // Utom-tavlan-posterna ar sokbara men raknas inte som tavlande.
        var totalt = document.querySelectorAll("[data-sok]:not([data-utom])").length;

        function filtrera() {{
          var q = falt.value.trim().toLowerCase();
          rensa.style.display = q ? "block" : "none";

          var traffar = 0;
          poster.forEach(function (p) {{
            var visa = !q || p.getAttribute("data-sok").indexOf(q) !== -1;
            p.classList.toggle("dold", !visa);
            if (visa) traffar++;
          }});

          block.forEach(function (b) {{
            var kvar = b.querySelectorAll("[data-sok]:not(.dold)").length;
            var panel = b.closest(".kort-panel");
            var tom = panel && panel.querySelector("[data-tom]");
            if (tom) tom.classList.toggle("visa", q !== "" && kvar === 0);
          }});

          status.textContent = q
            ? traffar + (traffar === 1 ? " träff" : " träffar")
            : totalt + " deltagare";
        }}

        falt.addEventListener("input", filtrera);
        rensa.addEventListener("click", function () {{
          falt.value = "";
          falt.focus();
          filtrera();
        }});
        falt.addEventListener("keydown", function (e) {{
          if (e.key === "Escape") {{ falt.value = ""; filtrera(); }}
        }});
      }})();
    </script>
  </body>
</html>
'''

with open(ROOT + "resultat.html", "w", encoding="utf-8") as fh:
    fh.write(HTML)
print("resultat.html  %d tecken" % len(HTML))


# ═══════════════ MARKDOWN (samma siffror, ren typografi utan emojis) ═══════════════
def md_rows(data, km, vinnare):
    ut = []
    for plac, nr, namn, tid in data:
        kon = vinnare.get(nr)
        n = "**%s**" % namn if kon else namn
        mark = " — **1:a %s**" % kon if kon else ""
        ut.append("| %d | %d | %s%s | %s | %s |" % (plac, nr, n, mark, tid, pace(secs(tid), km)))
    return "\n".join(ut)


HUVUD = "| Plac | Nr | Namn | Tid | Min/km |\n|--:|--:|:--|--:|--:|"

MD = f"""# Byathlon 2026 — Resultat

**25 juli 2026 · By badplats · Sidensjöveckan**

Vilken dag. {tot_pers} personer tog sig runt banorna genom Sidensjöbygden — från badplatsen vid sjön, upp i höjderna och tillbaka ner till bastun och ett välförtjänt dopp. Tillsammans avverkade ni **{nf(tot_km)} kilometer** och klättrade **{nf(tot_hm)} höjdmeter**, motsvarande {nf(tot_hm / 2097, 1)} bestigningar av Kebnekaise.

Stort grattis till alla som startade, kämpade och gick i mål.

---

## Lång distans — {nf(L['km'], 2)} km

**Banan i siffror**

| | |
|:--|:--|
| Distans | {nf(L['km'], 2)} km ({nf(L['km'] * 1000)} m enligt Stravas uppmätning) |
| Total klättring | {nf(L['upp'])} m uppför — och {nf(L['upp'])} m nedför |
| Nettohöjd | ±0 m, banan är en rundslinga |
| Högsta punkt | {nf(L['hi'])} m ö.h. vid km {nf(L['hi_km'], 2)} |
| Lägsta punkt | {nf(L['lo'])} m ö.h. |
| Klättring per km | {nf(L['hm_km'], 1)} m |
| Brantaste partiet | {nf(L['brant'], 1)} % vid km {nf(L['brant_km'], 2)} |

Banan sparar inte på krutet. Redan under första kilometern börjar det bära uppåt, och fram till km 1,81 klättras {nf(L['hi'] - 117)} höjdmeter upp till banans högsta punkt på {nf(L['hi'])} meter över havet. Därefter bär det västerut, drygt fyra kilometer fågelvägen från start, innan slingan vänder hemåt.

Banan är en rundslinga, så du slutar exakt där du började — men däremellan ligger {nf(L['upp'])} höjdmeter uppför och lika många nedför. Två tredjedelar av stigningen ligger i första halvan, så den som orkade hålla emot i backarna fick betalt sedan: efter vändpunkten rullar banan lättare och de sista kilometrarna faller stadigt ner mot sjön igen.

**Steffen Dalsgaard** utnyttjade det till fullo: {LANG[0][3][3:]} över {nf(L['km'], 2)} km betyder **4:00 min/km** hela vägen — nästan tio minuter före tvåan. Snabbaste dam blev **Karin Hägglund** på 1:06:09, femma totalt.

{HUVUD}
{md_rows(LANG, L['km'], VINNARE['lang'])}

*{nl} i mål. Mediantid {hhmmss(4642)} — {pace(4642, L['km'])} min/km. Nio löpare under 1:10, trettiotvå under 1:30.*

---

## Kort distans — {nf(K['km'], 2)} km

**Banan i siffror**

| | |
|:--|:--|
| Distans | {nf(K['km'], 2)} km ({nf(K['km'] * 1000)} m enligt Stravas uppmätning) |
| Total klättring | {nf(K['upp'])} m uppför — och {nf(K['upp'])} m nedför |
| Nettohöjd | ±0 m, banan är en rundslinga |
| Högsta punkt | {nf(K['hi'])} m ö.h. vid km {nf(K['hi_km'], 2)} — {nf(K['hi'] - L['hi'])} m högre än långbanans högsta punkt |
| Lägsta punkt | {nf(K['lo'])} m ö.h. |
| Klättring per km | {nf(K['hm_km'], 1)} m — {nf(K['hm_km'] / L['hm_km'], 1)} gånger så mycket som långa banan |
| Brantaste partiet | {nf(K['brant'], 1)} % vid km {nf(K['brant_km'], 2)} |

Kort betyder inte lätt. Kortbanan är den brantaste av de två — den klättrar rakt upp från sjön till **{nf(K['hi'])} meter över havet**, alltså {nf(K['hi'] - L['hi'])} meter högre än vad långbanan någonsin når. Räknat per kilometer klättrar den {nf(K['hm_km'] / L['hm_km'], 1)} gånger så mycket som långa banan.

I praktiken är det *en enda* stigning: {nf(K['hi'] - 118)} höjdmeter från startlinjen upp till toppen vid km {nf(K['hi_km'], 2)}, med {nf(K['brant'], 1)} procents lutning som brantast. Efter toppen väntar en enda lång utförslöpning hem mot bastun — håll bara benen kvar under dig.

**Anton Hägglund** vann på {KORT[0][3][3:]} — {pace(secs(KORT[0][3]), K['km'])} min/km — efter en tajt duell med Pär Byström, 21 sekunder bakom. Snabbaste dam blev **Louise Byström** på 29:42, fjärde plats totalt och två sekunder före Hanna Byström.

{HUVUD}
{md_rows(KORT, K['km'], VINNARE['kort'])}

*{nk} i mål. Mediantid {hhmmss(2000)} — {pace(2000, K['km'])} min/km. Tätast i fältet: från 12:e till 15:e plats skiljde bara 6 sekunder.*

---

## Utom tävlan — banan på egen hand

Några av dem som fick loppet att fungera hann aldrig springa det. Här är de som tog sig runt banan på egen hand en annan dag — utanför tidtagningen, men väl värda sin plats i listan.

| Nr | Namn | Tid | Min/km | |
|--:|:--|--:|--:|:--|
""" + "\n".join(
    "| %d | **%s** | %s | %s | %s |" % (
        nr, namn, tid[3:], pace(secs(tid), K["km"]), notis)
    for nr, namn, tid, notis in UTOM) + f"""

{UTOM[0][1]}s tid hade räckt till {sum(1 for _, _, _, t in KORT if secs(t) < secs(UTOM[0][2])) + 1}:e plats i tävlingen.

---

## Motion — {nf(K['km'], 2)} km

**Banan i siffror**

| | |
|:--|:--|
| Distans | {nf(K['km'], 2)} km, samma bana som kort distans |
| Total klättring | {nf(K['upp'])} m |
| Högsta punkt | {nf(K['hi'])} m ö.h. — Byathlons högsta punkt |
| Hundar | Välkomna |
| Tidtagning | Ingen — ingen tid, ingen placering |

Motionsklassen handlar om en enda sak: att ta sig runt. Samma backar, samma utsikt från {nf(K['hi'])} meter, samma dopp i sjön efteråt — men helt utan klocka. Här går man, pratar, stannar och tittar, och kommer i mål precis lika mycket som alla andra.

Att gå eller springa {nf(K['km'], 2)} kilometer med {nf(K['upp'])} höjdmeter är en riktig prestation, oavsett vad urtavlan säger. **Stort hurra till er alla.**

| Nr | Namn |
|--:|:--|
""" + "\n".join("| %d | %s |" % (nr, namn) for nr, namn in MOTION) + f"""

*{nm} deltagare runt banan.*

---

## Dagen i siffror

- **{tot_pers} personer** i mål — {nl} på {nf(L['km'], 2)} km, {nk} på {nf(K['km'], 2)} km och {nm} i motion
- **{nf(tot_km)} km** sammanlagt tillryggalagda
- **{nf(tot_hm)} höjdmeter** klättrade tillsammans, motsvarande {nf(tot_hm / 2097, 1)} bestigningar av Kebnekaise
- **{tot_h} timmar och {tot_m} minuter** total löptid på de tidtagna klasserna
- **4:00 min/km** — Steffen Dalsgaards snitt över hela långbanan, på sekunden jämnt
- **{nf(K['hi'])} mot {nf(L['hi'])} m ö.h.** — kortbanan når {nf(K['hi'] - L['hi'])} meter högre än långbanan
- **{nf(K['hm_km'], 1)} mot {nf(L['hm_km'], 1)} höjdmeter per km** — kortbanan är {nf(K['hm_km'] / L['hm_km'], 1)} gånger brantare
- **{nf(K['brant'], 1)} %** — brantaste lutningen på hela Byathlon, vid km {nf(K['brant_km'], 2)} på kortbanan
- **Tre delade placeringar**, alla på samma sekund: Strandberg/Holmgren (30:a lång), Nyberg/Näslund (19:a kort) och Albin/Anna Björkqvist (25:a kort), som gick i mål tillsammans på 48:00
- **1 sekund** skiljde Lukas Palm och Vega Kjellsson om nionde platsen på korta banan — dagens minsta marginal
- **Fem Byström** på korta banan — fyra av dem bland de sju främsta
- **Julia, Victor och Lova Höglund** avslutade långbanan inom 37 sekunder av varandra

---

## Tack

Tack till alla deltagare, funktionärer och publik som gjorde Byathlon 2026 till vad det blev — och tack till **HK Vägtrummor** och våra övriga sponsorer.

Vi ses vid startlinjen nästa år. Nu: bastu och dopp.

*By Intresseförening*

---

<sub>Bandata från de officiella Strava-banorna (`Rutter/Byathlon 13,5km.tcx` och `Rutter/Byathlon 5,5km.tcx`). Distansen är Stravas egen uppmätning längs banan. Total klättring är all uppförsbacke adderad, summerad med 2 m brusfilter — inte skillnaden mellan start och mål, som är noll eftersom båda banorna är rundslingor. Tempot är räknat på dessa distanser. Klassegrare dam och herr är bekräftade av arrangören; kön registreras inte vid anmälan. Genererad av `Rutter/generera-resultat.py`.</sub>
"""

with open(ROOT + "RESULTAT-2026.md", "w", encoding="utf-8") as fh:
    fh.write(MD)
print("RESULTAT-2026.md  %d tecken" % len(MD))
print("lang %s km  +%s m  %s hm/km  brantast %s%% | kort %s km  +%s m  %s hm/km  brantast %s%%"
      % (nf(L["km"], 2), nf(L["upp"]), nf(L["hm_km"], 1), nf(L["brant"], 1),
         nf(K["km"], 2), nf(K["upp"]), nf(K["hm_km"], 1), nf(K["brant"], 1)))
