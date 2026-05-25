"""Build data/content.json from structured Python definitions.

Run from the repo root:
    python3 tools/build_content.py

This script keeps content authoring readable; the resulting content.json
is what the app loads.
"""

from __future__ import annotations
import json, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT  = ROOT / "data" / "content.json"

PAGE = "img/pages/PXL_20260524_{}.jpg"
def p(s): return PAGE.format(s)

# ---------------------------------------------------------------------------
# Hoofdstukken
# ---------------------------------------------------------------------------
HOOFDSTUKKEN = [
    {"id": "h51", "titel": "5.1 Het skelet",            "bron": p("101657948")},
    {"id": "h52", "titel": "5.2 De bouw van botten",    "bron": p("101757207")},
    {"id": "h53", "titel": "5.3 Beenverbindingen (gewrichten)", "bron": p("101920404")},
    {"id": "h54", "titel": "5.4 Spieren",               "bron": p("102026478")},
]

# ---------------------------------------------------------------------------
# Begrippen (term -> definitie)
# ---------------------------------------------------------------------------
B = []
def b(_id, h, term, definitie, afbeelding=None, bron=None, tags=None):
    item = {"id": _id, "hoofdstuk": h, "term": term, "definitie": definitie}
    if afbeelding: item["afbeelding"] = afbeelding
    if bron:       item["bron"] = bron
    if tags:       item["tags"] = tags
    B.append(item)

# --- 5.1 Het skelet ---------------------------------------------------------
SKEL_OVER  = p("101705255")  # volledig skelet diagram
SKEL_INTRO = p("101657948")
FUNC_SKEL  = p("101713805")
SKEL_ILL   = p("101718373")

b("b-skelet",       "h51", "Skelet (geraamte)", "Het geheel van ongeveer 200 botten in het lichaam; samen ook wel het beenderstelsel genoemd.", SKEL_OVER, "Boek 5.1: skeletoverzicht", ["overzicht"])
b("b-bot",          "h51", "Bot (been, beender)", "Een stevig, hard onderdeel van het skelet; mensen hebben er ongeveer 200.", tags=["overzicht"])
b("b-hoofd-romp-led","h51","Hoofd, romp en ledematen", "De drie hoofddelen waarin je het menselijk lichaam kunt indelen. Ledematen zijn de armen en benen.", SKEL_ILL, tags=["indeling"])
b("b-achterhoofdsbeen","h51","Achterhoofdsbeen", "Bot achter aan de schedel; daar zit het gat waar het ruggenmerg naar binnen komt.", tags=["hoofd"])
b("b-borstwervels", "h51", "Borstwervels", "Wervels waaraan de ribben vastzitten; samen met ribben en borstbeen vormen ze de borstkas.", tags=["romp"])
b("b-lendenwervels","h51", "Lendenwervels", "De grote, sterke wervels in je onderrug; dragen het meeste gewicht.", tags=["romp"])
b("b-heiligbeen",   "h51", "Heiligbeen", "Driehoekig bot onderaan de wervelkolom, vastgegroeid aan het bekken.", tags=["romp"])
b("b-staartbeen",   "h51", "Staartbeen (stuitje)", "Het kleine bot helemaal onderaan de wervelkolom.", tags=["romp"])
b("b-borstkas",     "h51", "Borstkas", "Wordt gevormd door de borstwervels, de ribben en het borstbeen. Beschermt longen en hart.", tags=["romp", "bescherming"])
b("b-schoudergordel","h51","Schoudergordel", "De sleutelbeenderen en schouderbladen samen; verbinden de armen met de romp.", tags=["ledematen"])
b("b-uitsteeksels", "h51", "Uitsteeksels (van botten)", "Stukjes bot die uitsteken; daaraan zitten spieren vast.", tags=["spieraanhechting"])
b("b-stevigheid",   "h51", "Functie: stevigheid", "Het skelet houdt het lichaam rechtop en geeft het zijn vorm.", FUNC_SKEL, tags=["functie"])
b("b-bescherming",  "h51", "Functie: bescherming", "Het skelet beschermt kwetsbare organen: schedel→hersenen, borstkas→hart en longen, wervelkolom→ruggenmerg.", FUNC_SKEL, tags=["functie"])
b("b-beweging",     "h51", "Functie: beweging", "Aan de botten zitten spieren vast die het skelet bewegen via gewrichten.", FUNC_SKEL, tags=["functie"])
b("b-vormfunctie",  "h51", "Functie: vorm", "Het skelet geeft het lichaam zijn vorm — bv. de schedel maakt het hoofd rond.", FUNC_SKEL, tags=["functie"])

# --- 5.2 De bouw van botten -------------------------------------------------
BOUW_BOT     = p("101757207")
BOT_KRAAK    = p("101806392")
TEKENING_BOT = p("101823729")
GROEI_FOTO   = p("101831251")
OSTEO        = p("101908856")

b("b-botweefsel",   "h52", "Botweefsel", "Hard weefsel waaruit botten bestaan; cellen liggen in kringen om kleine kanaaltjes en zijn met uitlopers verbonden.", BOT_KRAAK, tags=["weefsel"])
b("b-kraakbeen",    "h52", "Kraakbeenweefsel", "Stevig, maar buigzaam weefsel; cellen liggen in groepjes in een soepele tussencelstof. Zit o.a. in de neus, oren en tussen de wervels.", BOT_KRAAK, tags=["weefsel"])
b("b-tussencelstof","h52", "Tussencelstof", "De stof tussen de cellen in een weefsel. In bot bestaat die uit collageen + kalkzouten.", tags=["weefsel"])
b("b-kalkzouten",   "h52", "Kalkzouten (calciumzouten)", "Maken de tussencelstof van bot hard en stevig. Hoe meer kalkzouten, hoe steviger en minder buigbaar het bot.", tags=["bot"])
b("b-collageen",    "h52", "Collageen", "Eiwit in de tussencelstof van bot dat het bot taai/sterk maakt (samen met de kalkzouten).", tags=["bot"])
b("b-beenmerg",     "h52", "Beenmerg", "Zachte stof binnen in botten. Er zijn twee soorten: rood en geel.", tags=["bot"])
b("b-rood-merg",    "h52", "Rood beenmerg", "Beenmerg waarin nieuwe bloedcellen worden aangemaakt; zit in de koppen van pijpbeenderen en in platte beenderen (zoals schouderblad en heupbeen).", tags=["bot"])
b("b-geel-merg",    "h52", "Geel beenmerg", "Vetrijk beenmerg in de mergholte van pijpbeenderen; dient als energievoorraad.", tags=["bot"])
b("b-botvlies",     "h52", "Botvlies", "Dun, taai vlies om de buitenkant van een bot; bevat bloedvaten en zenuwen en speelt een rol bij groei en herstel.", TEKENING_BOT, tags=["bot"])
b("b-fontanellen",  "h52", "Fontanellen", "Open plekken op de schedel van een baby waar de schedelbotten nog niet aan elkaar zitten; gevuld met bindweefsel. Maken het hoofd vervormbaar bij de geboorte en geven de hersenen ruimte om te groeien. Sluiten zich na ongeveer anderhalf jaar tot een naad.", tags=["groei"])
b("b-vitamine-d",   "h52", "Vitamine D", "Vitamine die je lichaam zelf aanmaakt onder invloed van zonlicht; nodig om kalk (calcium) op te nemen voor sterke botten.", tags=["voeding"])
b("b-calcium",      "h52", "Calcium (kalk)", "Mineraal dat nodig is voor de kalkzouten in botten; zit vooral in zuivelproducten.", tags=["voeding"])
b("b-mergholte",    "h52", "Mergholte", "De holte in het midden van een pijpbeen waarin beenmerg zit.", TEKENING_BOT, tags=["bot"])
b("b-sponsachtig",  "h52", "Sponsachtig bot", "Lichter bottype met holtes, te vinden in de koppen van pijpbeenderen en in platte beenderen; hierin zit het rode beenmerg.", tags=["bot"])
b("b-pijpbeen",     "h52", "Pijpbeen", "Lang bot met een mergholte in het midden en sponsachtig bot aan de uiteinden. Voorbeelden: dijbeen, opperarmbeen.", TEKENING_BOT, tags=["bot"])
b("b-plat-beender", "h52", "Plat beender", "Vrijwel volledig sponsachtig bot, zoals het schedeldak, schouderblad en het borstbeen.", tags=["bot"])
b("b-groeischijven","h52", "Groeischijven", "Schijfvormige stukjes kraakbeen in de uiteinden van botten van kinderen; hier wordt nieuw bot gevormd, waardoor het bot in de lengte groeit.", GROEI_FOTO, tags=["groei"])
b("b-skeletleeftijd","h52","Skeletleeftijd", "De leeftijd die het skelet aangeeft (gebaseerd op hoeveel groeischijven nog open zijn). Kan verschillen van de kalenderleeftijd.", GROEI_FOTO, tags=["groei"])
b("b-osteoporose",  "h52", "Osteoporose (botontkalking)", "Aandoening waarbij botten te weinig kalkzouten bevatten en daardoor zwakker zijn en sneller breken.", OSTEO, tags=["aandoening"])

# --- 5.3 Beenverbindingen / gewrichten -------------------------------------
GEW_INTRO  = p("101920404")
GEW_DIAG   = p("101924475")
GEW_TYPES  = p("101935795")
GEW_VRAGEN = p("101950157")
GEW_NUM    = p("102001394")
KNIE_DIST  = p("102018397")
SCHUIF     = p("102013669")

b("b-verb-vergroeid","h53","Vergroeide botten", "Botten die zo aan elkaar zijn vastgegroeid dat er geen beweging tussen mogelijk is. Voorbeeld: de wervels van het heiligbeen en het staartbeen.", tags=["verbinding"])
b("b-verb-naad",    "h53", "Naad", "Onbeweegbare verbinding waarbij botten als puzzelstukjes in elkaar passen. Voorbeeld: de schedelbotten van een volwassene.", tags=["verbinding"])
b("b-verb-kraak",   "h53", "Verbinding met kraakbeen", "Botten verbonden door een laagje kraakbeen waardoor een klein beetje beweging mogelijk is. Voorbeeld: ribben aan het borstbeen, schijven tussen de wervels.", tags=["verbinding"])
b("b-gewricht",     "h53", "Gewricht (beenverbinding met beweging)", "Beweegbare verbinding tussen twee botten. De vierde manier waarop botten verbonden kunnen zijn (naast vergroeid, naad en kraakbeen).", GEW_DIAG, tags=["verbinding","gewricht"])
b("b-gew-kogel",     "h53", "Kogelgewricht", "Gewrichtskogel van het ene bot draait in de gewrichtskom van het andere — beweging in véle richtingen. Voorbeeld: schouder, heup.", GEW_TYPES, tags=["type"])
b("b-gew-scharnier", "h53", "Scharniergewricht", "Beweegt heen en weer in één vlak, zoals een deurscharnier. Voorbeeld: elleboog, knie, vingerkootjes.", GEW_TYPES, tags=["type"])
b("b-gew-rol",       "h53", "Rolgewricht", "Twee botten rollen om elkaar, waardoor draaiende beweging mogelijk is. Voorbeeld: tussen ellepijp en spaakbeen (onderarm draaien).", GEW_TYPES, tags=["type"])
b("b-gew-schuif",    "h53", "Schuifgewricht", "Vlakke botoppervlakken schuiven langs elkaar; weinig beweging. Voorbeeld: tussen sleutelbeen en schoudertop (acromion).", SCHUIF, tags=["type"])
b("b-gew-zadel",     "h53", "Zadelgewricht", "Twee bot-oppervlakken die als ruiter en zadel in elkaar passen. Maakt beweging in twee richtingen mogelijk. Voorbeeld: in de duim, waardoor je je duim alle andere vingers kunt laten aanraken (opponeren).", tags=["type"])
b("b-gew-kogel-kom", "h53", "Gewrichtskogel en -kom", "De bolle kop van het ene bot (kogel) past in de holte (kom) van het andere bot in een kogelgewricht.", GEW_TYPES, tags=["bouw"])
b("b-gew-kapsel",    "h53", "Gewrichtskapsel", "Stevig zakje om een gewricht heen; houdt de gewrichtsvloeistof binnen.", tags=["bouw"])
b("b-gew-vloeistof", "h53", "Gewrichtsvloeistof", "Stroperige vloeistof in het gewricht die wrijving vermindert en de botten soepel laat bewegen.", tags=["bouw"])
b("b-gew-kraak",     "h53", "Gewrichtskraakbeen", "Laagje kraakbeen op de uiteinden van botten in een gewricht; vermindert wrijving en vangt schokken op.", tags=["bouw"])
b("b-banden",        "h53", "Banden (ligamenten)", "Stevige bindweefselbandjes die botten op hun plaats houden bij een gewricht.", tags=["bouw"])
b("b-kapselbanden",  "h53", "Kapselbanden", "Extra stevige banden ín het gewrichtskapsel die het kapsel verstevigen, vooral bij zwaar belaste gewrichten zoals de heup.", tags=["bouw"])
b("b-artrose",       "h53", "Artrose", "Slijtage van het gewrichtskraakbeen waardoor botten niet meer soepel over elkaar bewegen; geeft pijn en stijfheid in het gewricht.", tags=["aandoening"])
b("b-prothese",      "h53", "Prothese (kunstgewricht)", "Kunstmatige vervanging van een (deel van een) gewricht, bijvoorbeeld een kunstheup of kunstknie. Gaat ongeveer 20 jaar mee.", tags=["aandoening"])
b("b-hypermob",      "h53", "Hypermobiliteit", "Gewrichten zijn soepeler en minder stevig dan normaal; vergroot kans op gewrichtsslijtage.", tags=["aandoening"])
b("b-stamcellen",    "h53", "Stamcellen", "Cellen die zich nog kunnen ontwikkelen tot allerlei andere celtypen; spelen een rol bij herstel van bot- en kraakbeenweefsel.", tags=["herstel"])
b("b-kniedistractie","h53","Kniedistractie", "Behandeling waarbij de botten van het kniegewricht enige tijd uit elkaar worden getrokken zodat het gewricht zich kan herstellen.", KNIE_DIST, tags=["herstel"])

# --- 5.4 Spieren ------------------------------------------------------------
SPIER_INTRO  = p("102026478")
SPIER_BOUW   = p("102030802")
SPIER_WEEFS  = p("102037810")
SPIER_TYPES  = p("102042676")
SPIER_TAB    = p("102056072")
ANTAG        = p("102051386")
INZ_KOGEL    = p("102104432")
FSHD_PG      = p("102109211")

b("b-skeletspier", "h54", "Skeletspier", "Spier die aan botten vastzit en die je bewust kunt aansturen om botten te bewegen.", SPIER_BOUW, tags=["bouw"])
b("b-spierstelsel","h54", "Spierstelsel", "Alle skeletspieren in het lichaam samen. Bevat oppervlakkige (zichtbare) spieren en daaronder de diepe spieren.", SPIER_INTRO, tags=["overzicht"])
b("b-bewust",      "h54", "Bewuste beweging", "Beweging die je zelf kunt starten en sturen (zoals lopen of zwaaien). Wordt gedaan door skeletspieren (dwarsgestreept).", tags=["werking"])
b("b-onbewust",    "h54", "Onbewuste beweging", "Beweging die je lichaam zelf regelt zonder dat je erbij hoeft na te denken (zoals darmen, hart, bloedvaten). Wordt gedaan door orgaanspieren (glad) en de hartspier.", tags=["werking"])
b("b-buigspier",   "h54", "Buigspier", "Een spier die een gewricht buigt (bijv. de biceps buigt je elleboog).", tags=["werking"])
b("b-strekspier",  "h54", "Strekspier", "Een spier die een gewricht strekt (bijv. de triceps strekt je elleboog).", tags=["werking"])
b("b-spierschede", "h54", "Spierschede", "Laag bindweefsel om een hele skeletspier heen.", SPIER_BOUW, tags=["bouw"])
b("b-spierbundel", "h54", "Spierbundel", "Een bundel spiervezels, omgeven door een eigen laagje bindweefsel. Meerdere bundels vormen een hele spier.", SPIER_BOUW, tags=["bouw"])
b("b-spiervezel",  "h54", "Spiervezel", "Een spiercel: lang, dun, met meerdere kernen en vol spierfibrillen. Trekt samen door de fibrillen.", SPIER_BOUW, tags=["bouw"])
b("b-spierfibril", "h54", "Spierfibril", "Dun draadje binnenin een spiervezel; de fibrillen schuiven in elkaar en daardoor wordt de spier korter (samentrekken).", tags=["werking"])
b("b-aanhechting", "h54", "Aanhechtingsplaats", "De plaats (vaak op een uitsteeksel van een bot) waar een spier (via een pees) aan het bot vastzit.", SPIER_BOUW, tags=["bouw"])
b("b-pees",        "h54", "Pees (spierpees)", "Stevig, niet-rekbaar bindweefsel waarmee een spier aan een bot vastzit.", tags=["bouw"])
b("b-actine-myo",  "h54", "Actine en myosine", "Twee soorten eiwitten waaruit de spierfibrillen bestaan. Bij het samentrekken schuiven actine- en myosinedraden in elkaar, waardoor de spier korter wordt.", SPIER_WEEFS, tags=["werking"])
b("b-dwarsgestr",  "h54", "Dwarsgestreept spierweefsel", "Spierweefsel van skeletspieren; vezels met afwisselend lichte en donkere banden. Kun je bewust aansturen, raakt snel vermoeid.", SPIER_WEEFS, tags=["type"])
b("b-glad",        "h54", "Glad spierweefsel", "Spierweefsel in orgaanwanden (slokdarm, maag, darmen). Werkt onbewust en raakt minder snel vermoeid; cellen zijn langwerpig zonder strepen.", SPIER_WEEFS, tags=["type"])
b("b-hartspier",   "h54", "Hartspierweefsel", "Speciaal dwarsgestreept spierweefsel dat alleen in het hart voorkomt; werkt onbewust en raakt nooit vermoeid.", SPIER_TYPES, tags=["type"])
b("b-orgaanspier", "h54", "Orgaanspieren", "Spieren in de wand van organen, gemaakt van glad spierweefsel.", tags=["type"])
b("b-snelle-vez",  "h54", "Snelle spiervezels", "Vezels die snel en krachtig samentrekken, maar snel vermoeid raken. Belangrijk voor sprinten, springen, kogelstoten.", tags=["vezel"])
b("b-langz-vez",   "h54", "Langzame spiervezels", "Vezels die minder krachtig zijn, maar lang kunnen doorgaan zonder vermoeid te raken. Belangrijk voor uithoudingssport.", tags=["vezel"])
b("b-antagonist",  "h54", "Antagonistisch (spier)paar", "Twee spieren die het tegenovergestelde doen: als de ene aanspant (buigt), ontspant de ander (en omgekeerd). Een spier kan zelf alleen trekken, niet duwen.", ANTAG, tags=["werking"])

# ---------------------------------------------------------------------------
# Feiten (losse leerbare uitspraken)
# ---------------------------------------------------------------------------
F = []
def f(_id, h, feit, afbeelding=None, tags=None):
    item = {"id": _id, "hoofdstuk": h, "feit": feit}
    if afbeelding: item["afbeelding"] = afbeelding
    if tags: item["tags"] = tags
    F.append(item)

f("f-aantal",     "h51", "Het menselijk skelet bestaat uit ongeveer 200 botten.")
f("f-zoogdier",   "h51", "Mensen zijn zoogdieren; daarom hebben we (zoals alle zoogdieren) een inwendig skelet met een wervelkolom.")
f("f-vier-funct", "h51", "Het skelet heeft vier functies: stevigheid, bescherming, beweging en vorm.", FUNC_SKEL)
f("f-borstkas",   "h51", "De borstkas (ribben + borstbeen + borstwervels) beschermt vooral het hart en de longen.")
f("f-bouw-bot",   "h52", "De tussencelstof van bot bestaat uit kalkzouten (hard) en collageen (taai). Samen maken ze bot stevig én een beetje veerkrachtig.", BOT_KRAAK)
f("f-merg-loc",   "h52", "Rood beenmerg (waar bloedcellen worden gemaakt) zit in de koppen van pijpbeenderen en in platte beenderen.")
f("f-kraak-loc",  "h52", "Bij volwassenen blijft kraakbeen onder meer over op de uiteinden van botten (in gewrichten), tussen de wervels en in de neus en oren.")
f("f-groei-stop", "h52", "Zolang er groeischijven (kraakbeen) tussen de uiteinden van een bot zitten, kan een kind nog in de lengte groeien. Als alle groeischijven dichtgegroeid zijn, stopt de groei.")
f("f-osteo-bew",  "h52", "Bewegen tijdens de jeugd en puberteit maakt botten sterker en helpt osteoporose op latere leeftijd te voorkomen.", OSTEO)
f("f-vier-typen", "h53", "Vier veelvoorkomende typen gewrichten: kogel-, scharnier-, rol- en schuifgewricht.", GEW_TYPES)
f("f-knie-schar", "h53", "De knie is een scharniergewricht — je kunt hem dus alleen buigen en strekken in één vlak, niet draaien zoals de heup.")
f("f-band-stevig","h53", "Gewrichtsbanden houden de botten op hun plek; gewrichtsvloeistof zorgt dat de botten soepel langs elkaar bewegen.")
f("f-spier-trek", "h54", "Een spier kan alleen trekken, nooit duwen. Daarom is voor elke beweging een tegengestelde (antagonistische) spier nodig.", ANTAG)
f("f-spier-bouw", "h54", "Een skeletspier is opgebouwd uit: spierschede → spierbundels → spiervezels → spierfibrillen.", SPIER_BOUW)
f("f-drie-weefs", "h54", "Drie typen spierweefsel: dwarsgestreept (skeletspieren, bewust), glad (orgaanspieren, onbewust) en hartspier (alleen in het hart, onbewust, nooit moe).", SPIER_TYPES)
f("f-snel-langz", "h54", "Snelle spiervezels = veel kracht, korte tijd. Langzame spiervezels = minder kracht, lange tijd. Sprinters hebben meer snelle, marathonlopers meer langzame vezels.")
f("f-vier-verb",  "h53", "Botten kunnen op vier manieren verbonden zijn: vergroeid (geen beweging), naad (geen beweging), kraakbeen (weinig beweging) of gewricht (veel beweging).")
f("f-fontanel",   "h52", "Bij een baby zitten de schedelbotten nog niet aan elkaar vast — daartussen zitten fontanellen (bindweefsel-plekken). Die maken het hoofd vervormbaar bij de geboorte en geven de hersenen ruimte om te groeien. Na ±1,5 jaar zijn ze dichtgegroeid tot een naad.")
f("f-vit-d-calc", "h52", "Sterke botten heb je nodig: voldoende calcium (kalk, vooral uit zuivel) én voldoende vitamine D (uit zonlicht, of via voeding) zodat het lichaam dat calcium kan opnemen.")
f("f-actine-myo", "h54", "Een spier trekt samen doordat actine- en myosine-eiwitten in de spierfibrillen langs elkaar in elkaar schuiven. Daardoor wordt de spier korter en dikker.")
f("f-tussenrib",  "h54", "De tussenribspieren zijn skeletspier-weefsel (dwarsgestreept), maar werken meestal onbewust bij de ademhaling — een uitzondering op de regel 'dwarsgestreept = bewust'.")
f("f-achilles",   "h54", "De achillespees verbindt de kuitspier met de hiel. Bij volledige afscheuring kun je je voet niet meer naar beneden bewegen omdat de kuitspier dan losschiet.")

# ---------------------------------------------------------------------------
# Verbanden (kruisverbanden)
# ---------------------------------------------------------------------------
V = []
def v(_id, h, titel, uitleg, betreft, afbeelding=None):
    item = {"id": _id, "hoofdstuk": h, "titel": titel, "uitleg": uitleg, "betreft": betreft}
    if afbeelding: item["afbeelding"] = afbeelding
    V.append(item)

v("v-bot-spier-gew", "h54", "Botten + gewrichten + spieren: het bewegingsapparaat",
  "Een bot kan zelf niet bewegen. Daarvoor zijn spieren nodig (skeletspieren), die via pezen vastzitten aan de uitsteeksels van botten. De beweging zelf is alleen mogelijk doordat twee botten via een gewricht ten opzichte van elkaar kunnen bewegen. Drie hoofdstukken werken hier dus samen.",
  ["b-skeletspier", "b-gewricht", "b-uitsteeksels", "b-aanhechting", "b-pees"], SPIER_BOUW)

v("v-kalk-collageen", "h52", "Kalkzouten + collageen = stevig én taai bot",
  "Een bot moet hard zijn (anders breekt het door samengedrukt te worden) én een beetje meegevend (anders breekt het zodra je het buigt). Daarom bestaat de tussencelstof uit kalkzouten (hard) plus collageen (taai). Bij osteoporose zijn er te weinig kalkzouten, dus breken botten gemakkelijk.",
  ["b-kalkzouten", "b-collageen", "b-tussencelstof", "b-osteoporose"], BOT_KRAAK)

v("v-bouw-functie",   "h51", "Bouw → functie (skelet)",
  "Aan de vorm van een bot kun je vaak zien wat het doet. De schedel is gewelfd → beschermt de hersenen. De borstkas is gebogen → beschermt hart en longen. Pijpbeenderen zijn hol → licht maar sterk. Dezelfde logica zie je bij stuwdammen: gebogen = stevig onder druk.",
  ["b-borstkas", "b-pijpbeen", "b-stevigheid", "b-bescherming"])

v("v-gew-type-keuze", "h53", "Type gewricht past bij de beweging die nodig is",
  "Welk gewricht waar zit, hangt af van welke beweging je nodig hebt. In de schouder en heup heb je álle kanten op nodig → kogelgewricht. In de knie en elleboog wil je alleen buigen/strekken → scharniergewricht. Bij de onderarm wil je draaien → rolgewricht. Tussen sleutelbeen en schoudertop is weinig beweging nodig → schuifgewricht.",
  ["b-gew-kogel", "b-gew-scharnier", "b-gew-rol", "b-gew-schuif"], GEW_TYPES)

v("v-antagonist",     "h54", "Antagonistische spierparen",
  "Een spier kan alleen trekken, niet duwen. Daarom werken spieren in paren: terwijl de buigspier (bv. biceps) aanspant, ontspant de strekspier (triceps). Bij strekken keert dat om. Zonder antagonist zou een gebogen arm niet meer recht kunnen.",
  ["b-antagonist", "b-skeletspier"], ANTAG)

v("v-vezels-sport",   "h54", "Spiervezeltype past bij type sport",
  "Snelle vezels leveren veel kracht maar raken snel vermoeid → handig voor sprinters, kogelstoters, springers. Langzame vezels leveren minder kracht maar gaan lang door → handig voor marathonlopers, wielrenners. Elke sporter heeft een mix; de verhouding bepaalt waarin iemand uitblinkt.",
  ["b-snelle-vez", "b-langz-vez"], INZ_KOGEL)

v("v-groei-skel",     "h52", "Groeischijven bepalen je lengte",
  "Zolang de groeischijven (kraakbeen) tussen de botuiteinden open zijn, kan een kind groeien. Op een röntgenfoto zie je de groeischijven als donkere streepjes. Op basis daarvan kan een arts de skeletleeftijd bepalen, die kan verschillen van de kalenderleeftijd.",
  ["b-groeischijven", "b-skeletleeftijd", "b-kraakbeen"], GROEI_FOTO)

v("v-spiertypen-functies", "h54", "Drie typen spierweefsel passen bij hun functie",
  "Skeletspieren (dwarsgestreept) kun je bewust aansturen — handig om gericht te bewegen, maar ze raken vermoeid. Orgaanspieren (glad) moeten dag en nacht doorwerken zonder dat je erbij hoeft na te denken (maag, darmen). De hartspier moet je hele leven lang ritmisch blijven kloppen, zonder pauze of vermoeidheid — daarom een eigen weefseltype.",
  ["b-dwarsgestr", "b-glad", "b-hartspier", "b-orgaanspier"], SPIER_TYPES)

# ---------------------------------------------------------------------------
# Vragen
# ---------------------------------------------------------------------------
Q = []
def q_mc(_id, h, vraag, opties, antwoord_index, uitleg=None, moeilijkheid="gemiddeld", afbeelding=None, tags=None):
    item = {"id": _id, "hoofdstuk": h, "type": "mc", "moeilijkheid": moeilijkheid,
            "vraag": vraag, "opties": opties, "antwoord_index": antwoord_index}
    if uitleg: item["uitleg"] = uitleg
    if afbeelding: item["afbeelding"] = afbeelding
    if tags: item["tags"] = tags
    Q.append(item)

def q_open(_id, h, vraag, antwoord, kernwoorden, moeilijkheid="gemiddeld", afbeelding=None, tags=None):
    item = {"id": _id, "hoofdstuk": h, "type": "open", "moeilijkheid": moeilijkheid,
            "vraag": vraag, "antwoord": antwoord, "kernwoorden": kernwoorden}
    if afbeelding: item["afbeelding"] = afbeelding
    if tags: item["tags"] = tags
    Q.append(item)

def q_inz(_id, h, vraag, antwoord, kernwoorden, moeilijkheid="lastig", afbeelding=None, tags=None):
    item = {"id": _id, "hoofdstuk": h, "type": "inzicht", "moeilijkheid": moeilijkheid,
            "vraag": vraag, "antwoord": antwoord, "kernwoorden": kernwoorden}
    if afbeelding: item["afbeelding"] = afbeelding
    if tags: item["tags"] = tags
    Q.append(item)

# ===== 5.1 Het skelet =======================================================
q_mc("q511", "h51", "Hoeveel botten heeft een volwassen mens ongeveer?",
     ["50", "100", "200", "500"], 2,
     "Het skelet bestaat uit ongeveer 200 botten.", "makkelijk")

q_mc("q512", "h51", "In welke drie hoofddelen verdeel je het menselijk lichaam?",
     ["Schedel, romp, benen",
      "Hoofd, romp en ledematen",
      "Skelet, spieren, organen",
      "Hoofd, borstkas, bekken"], 1,
     "Hoofd + romp + ledematen (armen en benen).", "makkelijk", afbeelding=SKEL_ILL)

q_mc("q513", "h51", "Welke onderdelen vormen samen de borstkas?",
     ["Sleutelbeenderen, schouderbladen, ribben",
      "Borstwervels, ribben en borstbeen",
      "Borstwervels, schouderbladen en borstbeen",
      "Heiligbeen, ribben en borstbeen"], 1,
     "Borstwervels + ribben + borstbeen vormen samen de borstkas.")

q_mc("q514", "h51", "Welk skeletonderdeel hoort NIET tot de wervelkolom?",
     ["Halswervels", "Lendenwervels", "Heiligbeen", "Borstbeen"], 3,
     "Het borstbeen hoort bij de borstkas, niet bij de wervelkolom.")

q_open("q515", "h51",
       "Het skelet houdt het lichaam rechtop (stevigheid). Welke andere drie functies heeft het skelet?",
       "Het skelet beschermt kwetsbare organen (bv. hart en longen door de borstkas), maakt beweging mogelijk doordat spieren aan de botten zitten en gewrichten tussen botten zitten, en geeft het lichaam zijn vorm.",
       ["bescherming", "organen", "beweging", "spieren", "gewrichten", "vorm"],
       "makkelijk", afbeelding=FUNC_SKEL)

q_open("q516", "h51",
       "Aan veel botten zitten uitsteeksels. Wat is de belangrijkste functie van deze uitsteeksels?",
       "De uitsteeksels zijn de plaatsen waar spieren (via pezen) aan het bot vastzitten. Hoe groter het uitsteeksel, hoe steviger de spier kan aanhechten.",
       ["uitsteeksels", "spieren", "aanhechting", "pezen"], "gemiddeld")

q_inz("q517", "h51",
      "Een slang kan grote prooien in één keer doorslikken doordat één bot dat de mens wél heeft, bij de slang ontbreekt. Welk bot is dat? Leg uit waarom dit nodig is.",
      "Het borstbeen. Bij de mens verbindt het borstbeen alle ribben aan de voorkant, waardoor de borstkas vrij stevig en gesloten is. Een slang heeft géén borstbeen; daardoor kunnen zijn ribben aan de voorkant uit elkaar bewegen en kan zijn lichaam ver oprekken om een grote prooi door te slikken.",
      ["borstbeen", "ribben", "uit elkaar", "doorslikken"], "lastig")

q_inz("q518", "h51",
      "Stuwdammen hebben een gebogen vorm, omdat een boog grote druk goed kan opvangen. Welke drie delen van jouw lichaam hebben om dezelfde reden een gebogen vorm? Leg uit waarom dat past bij hun functie.",
      "De schedel (gebogen → beschermt hersenen tegen klappen), de borstkas (gebogen → beschermt hart en longen én biedt ruimte om uit te zetten bij ademhaling) en het bekken (gebogen → vangt het gewicht van de romp op en geeft stevigheid).",
      ["schedel", "borstkas", "bekken", "bescherming", "druk", "boog"],
      "lastig", afbeelding=p("101745196"))

q_inz("q519", "h51",
      "Een bambino sphynx is een gefokt kattenras met extreem korte poten. Welke functie(s) van het skelet werkt of werken bij dit kattenras anders dan bij gewone katten? Leg je antwoord uit.",
      "Vooral de functie BEWEGING en VORM zijn anders. Door de korte poten kan de kat niet goed lopen of springen (beweging beperkt). Daarnaast krijgt het skelet een onnatuurlijke vorm: extra spiermassa tussen de schouderbladen en een holle ruggengraat. De functies stevigheid en bescherming blijven ongeveer gelijk.",
      ["beweging", "vorm", "lopen", "springen", "ruggengraat"],
      "lastig", afbeelding=p("101752681"))

# ===== 5.2 De bouw van botten ==============================================
q_mc("q521", "h52", "Waar zit het rode beenmerg, waarin nieuwe bloedcellen worden gemaakt?",
     ["In de mergholte van pijpbeenderen",
      "In de koppen van pijpbeenderen en in platte beenderen",
      "Alleen in de schedelbeenderen",
      "In de tussencelstof van bot"], 1,
     "Rood beenmerg zit in sponsachtig bot — dat zit in de koppen van pijpbeenderen en in platte beenderen.")

q_mc("q522", "h52", "Wat is het verschil tussen kraakbeen en bot?",
     ["Kraakbeen bevat kalkzouten en is hard; bot niet.",
      "In kraakbeen liggen cellen in kringen; in bot in groepjes.",
      "In bot liggen cellen in kringen rond kanaaltjes en is de tussencelstof verhard met kalkzouten; bij kraakbeen liggen cellen in groepjes in soepele tussencelstof.",
      "Er is geen verschil; het zijn synoniemen."], 2,
     "In bot zit veel kalk en zijn de cellen verbonden met uitlopers; kraakbeen is buigzamer.",
     afbeelding=BOT_KRAAK)

q_mc("q523", "h52", "Waarvoor dient een groeischijf?",
     ["Beschermt de mergholte",
      "Maakt nieuw bot waardoor het bot in de lengte groeit",
      "Slaat kalkzouten op",
      "Maakt nieuwe bloedcellen aan"], 1,
     "In de groeischijven wordt nieuw kraakbeen gevormd dat later verhardt tot bot.",
     afbeelding=GROEI_FOTO)

q_open("q524", "h52",
       "Waaruit bestaat de tussencelstof van bot en wat doet elk onderdeel?",
       "Uit kalkzouten (calciumzouten) en collageen. Kalkzouten maken het bot hard/stevig, collageen maakt het taai (een beetje meegevend) zodat het niet meteen breekt.",
       ["kalkzouten", "collageen", "hard", "taai", "stevig"])

q_open("q525", "h52",
       "Leg uit wat het verschil is tussen skeletleeftijd en kalenderleeftijd.",
       "De kalenderleeftijd is je echte leeftijd in jaren. De skeletleeftijd is de leeftijd die je skelet aangeeft, gebaseerd op hoeveel groeischijven nog open zijn. Iemand van 14 met al gesloten groeischijven heeft een hogere skeletleeftijd dan kalenderleeftijd.",
       ["skeletleeftijd", "kalenderleeftijd", "groeischijven", "open"],
       afbeelding=GROEI_FOTO)

q_inz("q526", "h52",
      "Bekijk de tekening van een bot (zie afbeelding). a) Hoe heet dit type bot? b) Heeft dit bot een mergholte? Leg uit. c) Komt er sponsachtig bot in voor? Leg uit.",
      "a) Het is een pijpbeen (lang bot zoals een dijbeen of opperarmbeen). b) Ja, in het midden zit een mergholte met geel beenmerg — dat is typerend voor pijpbeenderen. c) Ja, in de koppen (de uiteinden) van het pijpbeen zit sponsachtig bot. Daarin zit het rode beenmerg.",
      ["pijpbeen", "mergholte", "sponsachtig", "koppen", "uiteinden"],
      afbeelding=TEKENING_BOT)

q_inz("q527", "h52",
      "Iemand met osteoporose breekt veel sneller een bot dan iemand zonder. Leg uit waardoor dat komt, en geef twee dingen die je tijdens je jeugd en puberteit kunt doen om dit op latere leeftijd te voorkomen.",
      "Bij osteoporose bevatten de botten te weinig kalkzouten, waardoor de tussencelstof minder hard is en het bot zwakker. Een kleine val kan dan al een breuk geven. Veel buiten bewegen tijdens de jeugd én puberteit zorgt dat botcellen het skelet sterker maken. Daarnaast is voldoende calcium (kalk) en vitamine D in de voeding belangrijk om kalkzouten in te bouwen.",
      ["osteoporose", "kalkzouten", "minder", "bewegen", "calcium", "vitamine d"],
      afbeelding=OSTEO)

q_inz("q528", "h52",
      "Botten bestaan uit kalkzouten (hard) én collageen (taai/buigzaam). Wat zou er gebeuren als je botten alléén kalkzouten en geen collageen zouden bevatten? En als ze andersom alléén collageen hadden? Gebruik de begrippen 'taai' en 'breken' in je antwoord.",
      "Alleen kalkzouten: het bot is wel hard, maar heel bros — net als kalksteen. Het zou bij een kleine buiging meteen breken doordat het niet taai is. Alleen collageen: het bot zou zacht en rubberachtig zijn; je zou er niet op kunnen staan en het zou doorbuigen. De combinatie geeft een bot dat hard én taai is, en daarom bestand tegen druk én tegen buigen.",
      ["kalkzouten", "collageen", "taai", "breken", "buigen", "hard"])

# ===== 5.3 Beenverbindingen ================================================
q_mc("q531", "h53", "Welk type gewricht zit tussen het dijbeen en het scheenbeen (knie)?",
     ["Kogelgewricht", "Scharniergewricht", "Rolgewricht", "Schuifgewricht"], 1,
     "De knie buigt en strekt in één vlak → scharniergewricht.", afbeelding=GEW_VRAGEN)

q_mc("q532", "h53", "Welk type gewricht zit tussen het heupbeen en het dijbeen?",
     ["Kogelgewricht", "Scharniergewricht", "Rolgewricht", "Schuifgewricht"], 0,
     "De heup kan in véle richtingen draaien → kogelgewricht.")

q_mc("q533", "h53", "Welk type gewricht zit tussen ellepijp en spaakbeen waardoor je je onderarm kunt draaien?",
     ["Kogelgewricht", "Scharniergewricht", "Rolgewricht", "Schuifgewricht"], 2,
     "Twee botten rollen om elkaar = rolgewricht.")

q_mc("q534", "h53", "Wat is de functie van gewrichtsvloeistof?",
     ["De botten op hun plaats houden",
      "Schokken absorberen door verhardingen",
      "De wrijving tussen botten verminderen zodat ze soepel bewegen",
      "Nieuwe bloedcellen aanmaken"], 2,
     "Gewrichtsvloeistof is een soort smeerolie tussen de botten.")

q_open("q535", "h53",
       "Waarvoor dienen de banden bij een gewricht?",
       "Banden zijn stevige stukken bindweefsel die de twee botten op hun plaats houden, zodat het gewricht niet uit elkaar kan schieten.",
       ["banden", "botten", "plaats", "bindweefsel"])

q_inz("q536", "h53",
      "In je elleboog kun je je onderarm naar voren en naar achteren bewegen, en ook draaien zodat je hand met de palm omhoog of omlaag komt. Hoe kan dat? Welke gewrichtstypen zitten er in/bij je elleboog en wat is hun rol?",
      "Bij de elleboog werken twee gewrichten samen. Tussen het opperarmbeen en de ellepijp zit een scharniergewricht: dat zorgt voor het buigen en strekken (één vlak). Tussen de ellepijp en het spaakbeen zit een rolgewricht: daardoor kan de onderarm draaien. Samen krijg je beide bewegingen.",
      ["scharniergewricht", "buigen", "strekken", "rolgewricht", "draaien"],
      afbeelding=p("102001394"))

q_inz("q537", "h53",
      "Waarom kun je je onderbeen niét op dezelfde manier draaien als je onderarm? Leg uit met behulp van het type gewricht.",
      "In je onderarm zit een rolgewricht tussen ellepijp en spaakbeen, waardoor twee botten om elkaar kunnen rollen. In je onderbeen zit tussen scheenbeen en kuitbeen geen rolgewricht — die botten zitten vrijwel vast aan elkaar. Bovendien is de knie een scharniergewricht (alleen buigen/strekken). Daardoor kan het onderbeen niet draaien zoals de onderarm.",
      ["rolgewricht", "scharniergewricht", "ellepijp", "spaakbeen", "onderbeen"])

q_inz("q538", "h53",
      "Mensen met hypermobiliteit hebben soepeler gewrichten. Toch krijgen ze vaak juist eerder last van gewrichtsslijtage. Hoe kan dat? Gebruik de begrippen 'banden' en 'kraakbeen' in je antwoord.",
      "Bij hypermobiliteit zijn de banden te slap, waardoor de botten in een gewricht meer over elkaar kunnen schuiven dan normaal. Daardoor schuren de uiteinden van de botten — en dus het kraakbeen erop — vaker en op vreemde manieren langs elkaar. Het kraakbeen slijt sneller en daarmee ontstaat eerder gewrichtsslijtage, ook al voelt het gewricht juist 'losser'.",
      ["banden", "slap", "kraakbeen", "schuren", "slijtage"])

q_inz("q539", "h53",
      "Bij een kniedistractie worden de botten van de knie enige tijd uit elkaar getrokken. Welke botten zijn dat, en waarom werkt het herstellend? Noem 2 mogelijke oorzaken van het herstel.",
      "Bij de knie worden het dijbeen en het scheenbeen uit elkaar getrokken. Mogelijke oorzaken van herstel: 1) stamcellen krijgen ruimte om nieuw kraakbeen te vormen op de botuiteinden; 2) de samenstelling van de gewrichtsvloeistof verandert, waardoor het herstel beter verloopt; 3) mechanische veranderingen in het bot zelf zetten herstel in gang.",
      ["dijbeen", "scheenbeen", "stamcellen", "kraakbeen", "gewrichtsvloeistof"],
      afbeelding=KNIE_DIST)

# ===== 5.4 Spieren =========================================================
q_mc("q541", "h54", "Wat is de juiste volgorde van klein naar groot in een spier?",
     ["Spierbundel → spiervezel → spierfibril",
      "Spierfibril → spiervezel → spierbundel",
      "Spiervezel → spierfibril → spierbundel",
      "Spierfibril → spierbundel → spiervezel"], 1,
     "Spierfibrillen zitten in spiervezels, die zitten in spierbundels, die samen een hele spier vormen.",
     afbeelding=SPIER_BOUW)

q_mc("q542", "h54", "Welk type spierweefsel zit in de wand van je maag en darmen?",
     ["Dwarsgestreept spierweefsel",
      "Glad spierweefsel",
      "Hartspierweefsel",
      "Skeletspierweefsel"], 1,
     "Glad spierweefsel werkt onbewust en zit in orgaanwanden.",
     afbeelding=SPIER_TYPES)

q_mc("q543", "h54", "Een sprinter heeft in zijn beenspieren een groot aandeel:",
     ["langzame spiervezels",
      "snelle spiervezels",
      "gladde spiervezels",
      "hartspiervezels"], 1,
     "Snelle vezels = veel kracht, korte tijd → handig voor sprinten.")

q_mc("q544", "h54", "De antagonist (tegenwerker) van de biceps is de:",
     ["kuitspier", "triceps", "scheenbeenspier", "borstspier"], 1,
     "Biceps buigt de elleboog, triceps strekt hem.", afbeelding=INZ_KOGEL)

q_open("q545", "h54",
       "Een spier kan alleen trekken en niet duwen. Waarom heb je daarom voor elke beweging een antagonistisch paar nodig?",
       "Omdat een spier alleen kan trekken (samentrekken), kan hij een bot maar in één richting bewegen. Voor de tegenovergestelde beweging is een tweede spier nodig die het bot de andere kant op trekt. Daarom werken spieren in antagonistische paren: terwijl de ene trekt, ontspant de ander, en andersom.",
       ["trekken", "duwen", "antagonist", "tegengesteld", "paar"],
       afbeelding=ANTAG)

q_open("q546", "h54",
       "Waarom is de scheenbeenspier (antagonist van de kuitspier) dunner dan de kuitspier?",
       "De kuitspier moet bij elke stap het hele lichaamsgewicht omhoog tillen (op je tenen gaan staan, afzetten bij het lopen). Dat kost veel kracht, dus is hij dik. De scheenbeenspier hoeft alleen de voet omhoog te trekken zonder gewicht — dat kost veel minder kracht, dus hij hoeft niet zo dik te zijn.",
       ["kuitspier", "lichaamsgewicht", "afzetten", "kracht", "scheenbeen"])

q_inz("q547", "h54",
      "Een atlete maakt zich klaar om een kogel weg te stoten. Net vóór het wegstoten houdt ze haar arm gebogen. Welke spier (biceps of triceps) trekt op dát moment samen, en welke ontspant? En tijdens het wégstoten zelf?",
      "Voor het wegstoten houdt ze haar arm gebogen: dan trekt de biceps (buigspier) samen en ontspant de triceps (strekspier). Tijdens het wegstoten zelf moet de arm krachtig gestrekt worden: dan trekt juist de triceps samen en ontspant de biceps.",
      ["biceps", "triceps", "samentrekken", "ontspannen", "buigen", "strekken"],
      afbeelding=INZ_KOGEL)

q_inz("q548", "h54",
      "Een kogelstoter heeft in zijn arm meer snelle of meer langzame spiervezels nodig? Leg uit waarom.",
      "Meer snelle spiervezels. Het wegstoten duurt heel kort (één korte, krachtige beweging) en moet zo hard mogelijk gebeuren. Snelle vezels kunnen kort heel krachtig samentrekken — precies wat hier nodig is. Lang doorgaan is niet nodig, dus de zwakte van snelle vezels (snel vermoeid) is hier geen probleem.",
      ["snelle", "vezels", "kracht", "kort", "krachtig"])

q_inz("q549", "h54",
      "Bij FSHD verzwakt vooral het skeletspierweefsel. Daardoor kunnen mensen niet meer goed fietsen, traplopen of zich aankleden, maar ze overlijden er meestal niet aan. Verklaar dit verschil met een spierziekte die ook het hartspierweefsel zou aantasten. Welk type spierweefsel wordt aangetast bij FSHD?",
      "Bij FSHD wordt het dwarsgestreepte (skelet)spierweefsel zwakker. Skeletspieren stuur je bewust aan voor bewegingen als lopen en fietsen — dus die activiteiten worden moeilijker. Maar voor je hart zelf gebruik je hartspierweefsel, en dat blijft bij FSHD intact, dus je hart blijft kloppen. Een ziekte die ook het hartspierweefsel zou aantasten, zou levensbedreigend zijn omdat het hart zou stoppen.",
      ["dwarsgestreept", "skeletspier", "hartspier", "bewust", "hart"],
      afbeelding=FSHD_PG)

q_inz("q54a", "h54",
      "Orgaanspieren raken minder snel vermoeid dan skeletspieren. Leg uit waarom dat gunstig is voor de werking van organen als de maag en de darmen.",
      "De maag en darmen moeten dag en nacht doorwerken om voedsel te verteren en door te schuiven, zonder pauze. Als orgaanspieren snel vermoeid zouden raken zoals skeletspieren, zou de vertering elke paar minuten stilvallen. Doordat glad spierweefsel niet snel vermoeid raakt, kunnen organen continu blijven werken.",
      ["dag en nacht", "vermoeid", "continu", "vertering", "doorwerken"])

# ===== KRUISVERBAND-vragen tussen hoofdstukken =============================
q_inz("qX01", "h54",
      "Beschrijf in 3 stappen hoe het komt dat je je elleboog kunt buigen. Gebruik in je antwoord begrippen uit hoofdstuk 5.1 (skelet), 5.3 (gewrichten) én 5.4 (spieren).",
      "1) Skelet: in je arm zitten twee botten (opperarmbeen + onderarmbotten) met op het opperarmbeen een uitsteeksel waar spieren aan vastzitten. 2) Gewricht: tussen opperarmbeen en onderarm zit een scharniergewricht, waardoor de onderarm in één vlak kan bewegen. 3) Spier: de biceps (skeletspier) is via een pees aan de uitsteeksels van de botten verbonden; als zijn spiervezels samentrekken, wordt de spier korter en trekt hij de onderarm omhoog (buigen). De triceps ontspant intussen.",
      ["opperarmbeen", "scharniergewricht", "biceps", "samentrekken", "uitsteeksel", "pees"],
      "lastig", afbeelding=SPIER_BOUW)

q_inz("qX02", "h53",
      "Vergelijk de bouw van een schoudergewricht en een kniegewricht. Welk type gewricht is elk, welke beweging is mogelijk, en waarom past dat type goed bij die plek in het lichaam?",
      "De schouder is een kogelgewricht (gewrichtskogel van de bovenarm draait in de kom van het schouderblad). Daardoor kun je je arm in heel veel richtingen bewegen — handig om dingen vast te pakken op elke positie. De knie is een scharniergewricht: alleen buigen en strekken in één vlak. Dat is daar precies wat je nodig hebt om te lopen, en het is veel steviger dan een kogelgewricht — wat belangrijk is omdat de knie het gewicht van het bovenlichaam draagt.",
      ["kogelgewricht", "schouder", "scharniergewricht", "knie", "richtingen", "stevig", "gewicht"],
      "lastig")

q_inz("qX03", "h52",
      "Bij een breuk van een dijbeen geneest het bot weer. Welke twee onderdelen van het bot zijn vooral belangrijk voor dit herstel? En waarom is het belangrijk dat een arts het bot tijdens het herstel goed op elkaar zet?",
      "Belangrijk zijn: 1) de botcellen in de tussencelstof, die nieuw bot kunnen aanmaken door kalkzouten en collageen aan te leggen; 2) de bloedvaten in de kanaaltjes van botweefsel, die voedingsstoffen aanvoeren voor dat herstel. Als de arts het bot niet goed op elkaar zet, groeit het scheef vast — en dan past het niet meer goed bij de gewrichten, waardoor je niet meer normaal kunt bewegen.",
      ["botcellen", "kalkzouten", "collageen", "bloedvaten", "scheef", "gewricht"],
      "lastig")

q_inz("qX04", "h54",
      "Tijdens lange wandelingen krijgen mensen vaak eerder pijn in hun benen dan in hun rug, terwijl de rugspieren ook continu moeten werken om je rechtop te houden. Hoe kan dit verschil verklaard worden? Gebruik 'snelle' en 'langzame' spiervezels in je antwoord.",
      "De rugspieren bevatten in verhouding meer langzame spiervezels, omdat ze de hele dag het bovenlichaam rechtop moeten houden — een taak waarbij langdurig volhouden belangrijker is dan kracht. Langzame vezels raken nauwelijks vermoeid. De beenspieren hebben juist meer snelle vezels nodig voor stappen, springen en afzetten. Bij urenlang lopen raken die snelle vezels veel sneller vermoeid, dus krijg je pijn in de benen eerder dan in de rug.",
      ["langzame", "snelle", "rechtop", "vermoeid", "rug", "benen"],
      "lastig")

q_inz("qX05", "h53",
      "Een baby leert pas na maanden zelfstandig zitten en rechtop staan. Wat moet er in zijn skelet (bot/kraakbeen) en zijn spieren gebeuren voordat dat lukt?",
      "1) Veel kraakbeen in het skelet van een baby moet eerst verbenen (verharden tot bot met kalkzouten), zodat de wervelkolom en de beenderen genoeg stevigheid krijgen om het lichaamsgewicht te dragen. 2) De rug-, buik- en beenspieren moeten sterker worden: de spiervezels worden dikker door oefening, zodat ze de baby rechtop kunnen houden tegen de zwaartekracht in. Zonder allebei lukt zitten of staan niet.",
      ["kraakbeen", "verbenen", "kalkzouten", "spieren", "sterker", "zwaartekracht"],
      "lastig")

q_inz("qX06", "h51",
      "Een slang heeft geen borstbeen (5.1) en ook een ander type wervelkolom dan de mens. Hierdoor heeft een slang ook andere gewrichten (5.3) tussen zijn vele wervels nodig dan de mens. Welke functie kan het skelet van een MENS hierdoor beter uitvoeren dan dat van een slang, en welke kan een SLANG juist beter dan een mens?",
      "Een mens kan met zijn skelet veel beter STEVIGHEID en BESCHERMING leveren: de borstkas met borstbeen beschermt hart en longen goed, en de wervelkolom + ledematen geven stevigheid om rechtop te lopen en kracht te zetten. Een slang kan zonder borstbeen en met heel veel beweegbare wervels juist veel beter zijn lichaam in alle richtingen buigen en grote prooien doorslikken — dus BEWEGING (in een speciale vorm) gaat bij een slang beter.",
      ["stevigheid", "bescherming", "beweging", "borstbeen", "wervels", "doorslikken"],
      "lastig", afbeelding=p("101740664"))

# ===== Extra vragen over de nieuwe begrippen ================================

# --- Fontanellen ---
q_mc("qF01", "h52",
     "Wat zijn fontanellen?",
     ["Holtes in volwassen schedelbotten",
      "Open plekken op de schedel van een baby, gevuld met bindweefsel",
      "Kraakbeenschijfjes tussen de wervels",
      "Naden tussen de schedelbotten van een volwassene"],
     1,
     "Fontanellen zijn de plekken op de schedel van een baby waar de botten nog niet aan elkaar gegroeid zijn.")

q_inz("qF02", "h52",
      "Geef twee redenen waarom het handig is dat een baby fontanellen heeft.",
      "1) Bij de geboorte kan het hoofd een beetje vervormen doordat de schedelbotten over elkaar kunnen schuiven; daardoor past het hoofd door het geboortekanaal. 2) De hersenen groeien in het eerste levensjaar snel; doordat de schedelbotten nog niet aan elkaar zitten, kan de schedel meegroeien met de hersenen.",
      ["geboorte", "vervorm", "hersenen", "groeien", "ruimte"])

# --- Zadelgewricht / duim ---
q_mc("qZ01", "h53",
     "In de duim van een mens zit een gewricht waardoor je je duim álle andere vingers kunt laten aanraken (opponeren). Welk type gewricht is dit?",
     ["Kogelgewricht", "Scharniergewricht", "Rolgewricht", "Zadelgewricht"],
     3,
     "Het zadelgewricht maakt beweging in twee richtingen mogelijk — net genoeg om te opponeren.")

q_inz("qZ02", "h53",
      "In de duim zit een zadelgewricht en in de andere vingerkootjes scharniergewrichten. Welke beweging kan jouw duim daardoor wel maken, en de andere vingers niet?",
      "Doordat een zadelgewricht in twee richtingen kan bewegen, kan de duim niet alleen buigen/strekken, maar zich ook naar de handpalm toe draaien om de andere vingertoppen aan te raken (opponeren). De andere vingers hebben alleen scharniergewrichten en kunnen daardoor alléén buigen en strekken in één vlak.",
      ["zadelgewricht", "opponeren", "twee richtingen", "scharnier", "buigen", "strekken"])

# --- Achillespees & antagonisten ---
q_inz("qA01", "h54",
      "De achillespees verbindt de kuitspier met de hiel. Leg uit waarom je je voet niet meer naar beneden kunt bewegen als de achillespees helemaal afscheurt.",
      "De kuitspier trekt — via de achillespees — aan het hielbot om de voet naar beneden te bewegen (op je tenen staan). Als de achillespees afscheurt, is de verbinding tussen kuitspier en hiel weg: de kuitspier schiet omhoog en de kracht komt niet meer bij het bot. De spier kan dus wel samentrekken, maar dat heeft geen effect op de voet meer.",
      ["achillespees", "kuitspier", "hiel", "verbinding", "afscheuren", "kracht"])

q_mc("qA02", "h54",
     "De scheenbeenspier is duidelijk dunner dan de kuitspier, terwijl ze allebei deel zijn van hetzelfde antagonistische paar. Wat is de beste verklaring?",
     ["De scheenbeenspier hoeft minder kracht te leveren, want hij hoeft alleen tegen het gewicht van de voet in te werken; de kuitspier moet het hele lichaamsgewicht omhoog tillen bij op je tenen staan.",
      "De scheenbeenspier bestaat uit glad spierweefsel en is daardoor altijd dunner.",
      "De scheenbeenspier werkt onbewust en hoeft daarom minder spiervezels te hebben.",
      "De scheenbeenspier is geen antagonist en doet daarom geen krachtwerk."],
     0,
     "Hoeveel kracht een spier moet leveren bepaalt vooral hoe dik (hoeveel spiervezels) hij is.")

# --- Actine + myosine ---
q_open("qM01", "h54",
       "Leg in eigen woorden uit hoe een spier samentrekt op het niveau van de eiwitten actine en myosine.",
       "In een spierfibril zitten twee soorten eiwitdraden naast elkaar: actine en myosine. Bij het samentrekken schuiven deze draden langs elkaar in elkaar, waardoor de fibril (en dus de spier) korter en dikker wordt. Hoe meer spiervezels dit tegelijk doen, hoe meer kracht de spier zet.",
       ["actine", "myosine", "spierfibril", "schuiven", "in elkaar", "korter", "dikker"])

# --- Tussenribspieren ---
q_mc("qT01", "h54",
     "Tussenribspieren gebruik je bij het ademen. Uit welk type spierweefsel bestaan ze?",
     ["Glad spierweefsel", "Hartspierweefsel", "Dwarsgestreept spierweefsel", "Kraakbeenweefsel"],
     2,
     "Ze hebben dezelfde bouw als skeletspieren (dwarsgestreept), ook al werken ze meestal onbewust.")

q_inz("qT02", "h54",
      "Tussenribspieren bestaan uit dwarsgestreept spierweefsel, maar worden tóch ingedeeld bij de onwillekeurige (onbewuste) spieren. Leg dat uit.",
      "Dwarsgestreept spierweefsel kún je in principe bewust aansturen, maar ademhaling gebeurt het grootste deel van de tijd vanzelf, zonder dat je erbij nadenkt (anders zou je stoppen met ademen als je in slaap valt). Daarom worden de tussenribspieren bij de onwillekeurige spieren gerekend — vanwege wat ze doen, niet vanwege hun bouw.",
      ["dwarsgestreept", "ademhaling", "bewust", "onbewust", "slaap", "onwillekeurig"])

# --- Vier beenverbindingen + voorbeelden ---
q_mc("qV01", "h53",
     "Welke vier manieren zijn er om botten met elkaar te verbinden?",
     ["spier — pees — band — kraakbeen",
      "vergroeid — naad — kraakbeen — gewricht",
      "kogelgewricht — rolgewricht — scharniergewricht — schuifgewricht",
      "vergroeid — gewricht — spier — kraakbeen"],
     1,
     "Vier verbindings­typen: vergroeid, naad, kraakbeen, gewricht. Daarbinnen heb je nog de vier typen gewrichten.")

q_open("qV02", "h53",
       "Geef bij elk van de vier verbindings­typen één voorbeeld in het menselijk lichaam.",
       "Vergroeid: de wervels van het heiligbeen (of staartbeen). Naad: tussen de schedelbotten van een volwassene. Kraakbeen: tussen de ribben en het borstbeen (of tussen de wervels). Gewricht: de heup (kogelgewricht), de knie (scharniergewricht), de elleboog (scharnier + rolgewricht), enz.",
       ["heiligbeen", "schedel", "ribben", "borstbeen", "heup", "knie"])

# --- Botvlies + bouw bot ---
q_mc("qB01", "h52",
     "Wat is de functie van het botvlies?",
     ["Het vormt nieuwe bloedcellen.",
      "Het is een dun, taai vlies om de buitenkant van het bot dat onder andere zorgt voor groei en herstel; er lopen bloedvaten en zenuwen in.",
      "Het is een laag kraakbeen op de gewrichtskogel.",
      "Het is een soort smeervet binnenin de mergholte."],
     1)

# --- Bewust vs onbewust + drie spierweefsels ---
q_mc("qS01", "h54",
     "Welke combinatie klopt?",
     ["Glad spierweefsel — bewust — in skeletspieren",
      "Dwarsgestreept spierweefsel — bewust — in skeletspieren",
      "Hartspierweefsel — bewust — in het hart",
      "Glad spierweefsel — onbewust — in het hart"],
     1)

# --- Vitamine D + calcium + osteoporose (cross-connection) ---
q_inz("qC01", "h52",
      "Astronauten die lang in een ruimtestation verblijven, krijgen vaak zwakkere botten. Geef twee mogelijke oorzaken die je kunt verklaren met wat je hebt geleerd over botvorming.",
      "1) In de ruimte is er bijna geen zwaartekracht, waardoor de botten veel minder belast worden. Botcellen merken weinig beweging in de vloeistof om zich heen, waardoor er minder nieuw bot wordt aangemaakt en zelfs bot wordt afgebroken (vergelijkbaar met osteoporose). 2) Astronauten komen niet of nauwelijks aan zonlicht, dus maken ze minder vitamine D aan. Zonder vitamine D nemen ze ook minder calcium op, en zonder calcium kunnen de tussencelstof-kalkzouten in het bot niet goed worden aangevuld.",
      ["zwaartekracht", "botcellen", "afgebroken", "vitamine D", "zonlicht", "calcium", "osteoporose"])

# --- Cross-connection: skelet + spier + gewricht ---
q_inz("qC02", "h54",
      "Stijn wil één keer een kogel zo ver mogelijk wegstoten. Welke combinatie van bot, gewricht, type spier én type spiervezel kiest zijn lichaam voor deze beweging? Leg uit waarom.",
      "Voor de stoot gebruikt hij vooral het opperarmbeen + spaakbeen/ellepijp; het belangrijkste gewricht is het kogelgewricht in zijn schouder (alle kanten op, dus optimaal voor wegstoten) plus het scharniergewricht in zijn elleboog. De spier die het laatste duwt is de triceps (strekspier). Omdat het maar één korte, krachtige beweging is, gebruikt zijn lichaam vooral snelle spiervezels: die leveren veel kracht in korte tijd, ook al raken ze snel vermoeid.",
      ["kogelgewricht", "schouder", "scharnier", "elleboog", "triceps", "strekspier", "snelle spiervezels", "kracht"],
      afbeelding=p("102104432"))

# Extra verbanden (kruisverbanden) over de nieuwe stof
v("v-fontan-groei", "h52", "Fontanellen + groeischijven: ruimte om te groeien",
  "Een baby moet snel groeien — niet alleen in de lengte, maar ook in hoofdomvang. Daarom heeft het skelet van een kind twee 'open' constructies: fontanellen tussen de schedelbotten geven de hersenen ruimte om te groeien, en groeischijven van kraakbeen aan de uiteinden van pijpbeenderen laten botten in de lengte groeien. Bij een volwassene zijn beide gesloten/verbeend.",
  ["b-fontanellen", "b-groeischijven", "b-skeletleeftijd"], GROEI_FOTO)

v("v-tussenrib-paradox", "h54", "Tussenribspieren: bouw vs functie",
  "Normaal gesproken hoort dwarsgestreept spierweefsel bij bewuste bewegingen, en glad bij onbewuste. Tussenribspieren zijn een uitzondering: ze zijn dwarsgestreept (zoals skeletspieren) maar werken meestal onbewust, want anders zou je ademhaling stoppen als je in slaap valt. Dit laat zien dat indeling op functie (willekeurig vs onwillekeurig) niet altijd samenvalt met indeling op bouw (dwarsgestreept vs glad).",
  ["b-dwarsgestr", "b-glad", "b-bewust", "b-onbewust"], FSHD_PG)

v("v-actine-myosine-vezels", "h54", "Eiwitten → fibrillen → vezels → kracht",
  "Het samentrekken van een spier begint heel klein: actine- en myosine-eiwitten schuiven in elkaar in een spierfibril. Veel fibrillen zitten in één spiervezel, en hoe meer vezels tegelijk samentrekken, hoe meer kracht de hele spier zet. Of die kracht kort en hard (snelle vezels) of lang en gelijkmatig (langzame vezels) is, hangt af van het type vezel.",
  ["b-actine-myo", "b-spierfibril", "b-spiervezel", "b-snelle-vez", "b-langz-vez"], SPIER_WEEFS)


# ---------------------------------------------------------------------------
# Aanwijs-kaarten: klik de juiste bot/spier aan op de interactieve SVG
# ---------------------------------------------------------------------------
SKELET_SVG  = "img/anatomy/skelet.svg"
SPIEREN_SVG = "img/anatomy/spieren.svg"

# Lijst: (id, svg, region-id, naam, vraag, hoofdstuk, hint)
AANWIJZEN_RAW = [
    # --- Botten op het skelet (5.1 / 5.3) ---
    ("a-voorhoofd",    SKELET_SVG, "r-voorhoofdsbeen", "Voorhoofdsbeen", "Klik op het voorhoofdsbeen.", "h51", "Boven aan de schedel."),
    ("a-wandbeen",     SKELET_SVG, "r-wandbeen",       "Wandbeen",       "Klik op het wandbeen.", "h51", "Zijkant van de schedel."),
    ("a-schedel",      SKELET_SVG, "r-schedel",        "Schedel (overig)", "Klik op het overige deel van de schedel (rond de ogen).", "h51", None),
    ("a-bovenkaak",    SKELET_SVG, "r-bovenkaak",      "Bovenkaak",      "Klik op de bovenkaak.", "h51", "Het vaste kaakbot."),
    ("a-onderkaak",    SKELET_SVG, "r-onderkaak",      "Onderkaak",      "Klik op de onderkaak.", "h51", "Het beweegbare kaakbot."),
    ("a-halswervels",  SKELET_SVG, "r-halswervels",    "Halswervels",    "Klik op de halswervels.", "h51", "Bovenste deel van de wervelkolom."),
    ("a-sleutelbeen",  SKELET_SVG, "r-sleutelbeen",    "Sleutelbeen",    "Klik op het sleutelbeen.", "h51", "Onderdeel van de schoudergordel, vooraan."),
    ("a-schouderblad", SKELET_SVG, "r-schouderblad",   "Schouderblad",   "Klik op het schouderblad.", "h51", "Plat bot achter de schouder; deel van de schoudergordel."),
    ("a-borstbeen",    SKELET_SVG, "r-borstbeen",      "Borstbeen",      "Klik op het borstbeen.", "h51", "Plat bot midden in de borstkas."),
    ("a-ribben",       SKELET_SVG, "r-ribben",         "Ribben",         "Klik op de ribben.", "h51", None),
    ("a-wervelkolom",  SKELET_SVG, "r-wervelkolom",    "Wervelkolom",    "Klik op de wervelkolom (lendenwervels).", "h51", "De wervels onder de ribben."),
    ("a-opperarmbeen", SKELET_SVG, "r-opperarmbeen",   "Opperarmbeen",   "Klik op het opperarmbeen.", "h51", "Het bovenarmbot."),
    ("a-spaakbeen",    SKELET_SVG, "r-spaakbeen",      "Spaakbeen",      "Klik op het spaakbeen (onderarm, duim-kant).", "h53", "Buitenkant van de onderarm."),
    ("a-ellepijp",     SKELET_SVG, "r-ellepijp",       "Ellepijp",       "Klik op de ellepijp (onderarm, pink-kant).", "h53", "Binnenkant van de onderarm."),
    ("a-handwortel",   SKELET_SVG, "r-handwortel",     "Handwortelbeentjes", "Klik op de handwortelbeentjes (pols).", "h51", "Acht kleine botjes in de pols."),
    ("a-middenhand",   SKELET_SVG, "r-middenhand",     "Middenhandsbeentjes", "Klik op de middenhandsbeentjes.", "h51", "Tussen pols en vingers, in de handpalm."),
    ("a-vingerkootjes",SKELET_SVG, "r-vingerkootjes",  "Vingerkootjes",  "Klik op de vingerkootjes.", "h51", "De botjes ván de vingers zelf."),
    ("a-bekkengordel", SKELET_SVG, "r-bekkengordel",   "Bekkengordel",   "Klik op de bekkengordel (het bekken).", "h51", None),
    ("a-dijbeen",      SKELET_SVG, "r-dijbeen",        "Dijbeen",        "Klik op het dijbeen.", "h51", "Het bot van je bovenbeen — het langste bot."),
    ("a-kniebeen",     SKELET_SVG, "r-kniebeen",       "Kniebeen",       "Klik op het kniebeen (de knieschijf).", "h53", None),
    ("a-scheenbeen",   SKELET_SVG, "r-scheenbeen",     "Scheenbeen",     "Klik op het scheenbeen (binnenkant van het onderbeen).", "h53", "Het dikke onderbeenbot."),
    ("a-kuitbeen",     SKELET_SVG, "r-kuitbeen",       "Kuitbeen",       "Klik op het kuitbeen (buitenkant van het onderbeen).", "h53", "Het dunne onderbeenbot."),
    ("a-voetwortel",   SKELET_SVG, "r-voetwortel",     "Voetwortelbeentjes", "Klik op de voetwortelbeentjes (wreef).", "h51", "Bovenkant van de voet, vlak achter de tenen-botjes."),
    ("a-middenvoet",   SKELET_SVG, "r-middenvoet",     "Middenvoetsbeentjes", "Klik op de middenvoetsbeentjes.", "h51", "Tussen wreef en tenen."),
    ("a-teenkootjes",  SKELET_SVG, "r-teenkootjes",    "Teenkootjes",    "Klik op de teenkootjes.", "h51", "De botjes ván de tenen."),

    # --- Spieren op het lichaam (5.4) ---
    ("a-biceps",        SPIEREN_SVG, "m-biceps",                 "Biceps",                  "Klik op de biceps (buigspier van de bovenarm).", "h54", "Voorkant van de bovenarm."),
    ("a-triceps",       SPIEREN_SVG, "m-triceps",                "Triceps",                 "Klik op de triceps (strekspier van de bovenarm).", "h54", "Achterkant van de bovenarm."),
    ("a-kuitspier",     SPIEREN_SVG, "m-kuitspier",              "Kuitspier",               "Klik op de kuitspier.", "h54", "Achterkant van het onderbeen."),
    ("a-scheenspier",   SPIEREN_SVG, "m-scheenbeenspier",        "Scheenbeenspier",         "Klik op de scheenbeenspier (antagonist van de kuitspier).", "h54", "Voorkant van het onderbeen."),
    ("a-dijbeenspier",  SPIEREN_SVG, "m-dijbeenspier",           "Voorste dijbeenspier",    "Klik op de voorste dijbeenspier (quadriceps).", "h54", "Voorkant van het bovenbeen."),
    ("a-achterdij",     SPIEREN_SVG, "m-achterste-dijbeenspier", "Achterste dijbeenspier",  "Klik op de achterste dijbeenspier (hamstring).", "h54", "Achterkant van het bovenbeen."),
    ("a-borstspier",    SPIEREN_SVG, "m-borstspier",             "Borstspier",              "Klik op de borstspier.", "h54", None),
    ("a-buikspieren",   SPIEREN_SVG, "m-buikspieren",            "Buikspieren",             "Klik op de buikspieren.", "h54", None),
    ("a-rugspieren",    SPIEREN_SVG, "m-rugspieren",             "Rugspieren",              "Klik op de rugspieren (onderrug).", "h54", "Achteraanzicht — onder de monnikskapspier."),
    ("a-bilspier",      SPIEREN_SVG, "m-bilspier",               "Bilspier",                "Klik op de bilspier.", "h54", None),
    ("a-monnikskap",    SPIEREN_SVG, "m-monnikskap",             "Monnikskapspier",         "Klik op de monnikskapspier.", "h54", "Ruitvormige spier in nek en bovenrug."),
    ("a-tussenribspieren", SPIEREN_SVG, "m-tussenribspieren",    "Tussenribspieren",        "Klik op de tussenribspieren (helpen bij ademhalen).", "h54", "Smalle strookjes spier tússen de ribben."),
    ("a-achillespees",  SPIEREN_SVG, "m-achillespees",           "Achillespees",            "Klik op de achillespees (verbindt kuitspier met hiel).", "h54", "Onder de kuitspier, in geel weergegeven."),
]

AANWIJZEN = []
for _id, svg, region, naam, vraag, h, hint in AANWIJZEN_RAW:
    item = {"id": _id, "hoofdstuk": h, "svg": svg, "region": region, "naam": naam, "vraag": vraag}
    if hint: item["hint"] = hint
    AANWIJZEN.append(item)

# ---------------------------------------------------------------------------
# Bouw en schrijf
# ---------------------------------------------------------------------------
data = {
    "vak":       "Biologie",
    "niveau":    "VWO 1",
    "proefwerk": "Hoofdstuk 5 — Stevigheid en beweging (T3 wk 26)",
    "bron":      "Foto's van het boek staan in raw/; webvriendelijke kopieën in img/pages/.",
    "hoofdstukken": HOOFDSTUKKEN,
    "begrippen":    B,
    "feiten":       F,
    "verbanden":    V,
    "vragen":       Q,
    "aanwijzen":    AANWIJZEN,
}

OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {OUT.relative_to(ROOT)}")
print(f"  hoofdstukken: {len(HOOFDSTUKKEN)}")
print(f"  begrippen:    {len(B)}")
print(f"  feiten:       {len(F)}")
print(f"  verbanden:    {len(V)}")
print(f"  vragen:       {len(Q)}  "
      f"(mc={sum(1 for q in Q if q['type']=='mc')} "
      f"open={sum(1 for q in Q if q['type']=='open')} "
      f"inzicht={sum(1 for q in Q if q['type']=='inzicht')})")
print(f"  aanwijzen:    {len(AANWIJZEN)}")
