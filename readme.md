# Bio Trainer — VWO 1, Trimester 3, week 26

Een kleine **statische webapp** waarmee Stijn (en zijn klasgenoten) zich kunnen voorbereiden op het proefwerk biologie.

> **Doel:** in 3 dagen klaar zijn voor het proefwerk via slimme herhaling, oefenvragen op VWO-niveau (inclusief inzicht- en kruisverbandvragen) en realistische proeftoetsen.

## Hoe werkt het

- **Leren** — flashcards van alle begrippen en feiten, met *spaced repetition* (SM-2-light). Markeer per kaart hoe goed je het wist; de app zorgt dat je de moeilijke vaker terugziet.
- **Begrippen** — alle begrippen op een rijtje per hoofdstuk, om snel iets op te zoeken.
- **Oefenen** — meerkeuze-, open- en inzichtvragen, te filteren op hoofdstuk, type en moeilijkheid. Met directe feedback en kernwoordcontrole bij open vragen.
- **Verbanden** — kruisverbanden (bv. *fotosynthese ↔ verbranding*) met uitleg en een oefenronde van pure inzichtvragen.
- **Proeftoets** — gemixte set met optionele tijdslimiet die het echte proefwerk simuleert. Eindscore + volledig nakijken.

Voortgang wordt opgeslagen in `localStorage`, dus per browser/apparaat.

## Stof toevoegen

1. Zet foto's van de boekpagina's in [`raw/`](raw/) (zie `raw/README.md`).
2. Voeg de begrippen, feiten, kruisverbanden en vragen toe in [`data/content.json`](data/content.json). Het schema staat in [`data/SCHEMA.md`](data/SCHEMA.md), tips voor goede VWO-vragen in [`tools/CONTENT_GUIDE.md`](tools/CONTENT_GUIDE.md).
3. De app valideert `content.json` bij laden en toont eventuele fouten bovenaan.

## Lokaal draaien

```bash
# vanuit de projectmap:
python3 -m http.server 8000
# open daarna http://localhost:8000
```

> Direct `index.html` openen in de browser werkt ook, maar veel browsers blokkeren `fetch` naar `data/content.json` op `file://`. Gebruik daarom de http-server hierboven.

## Hosten op GitHub Pages

1. Push de repository naar GitHub.
2. *Settings → Pages →* Source = `main`, folder = `/ (root)`.
3. De app is daarna te delen via `https://<gebruiker>.github.io/vwo1_t3_26_bio/`.

Het bestand `.nojekyll` staat er zodat Pages alle bestanden ongewijzigd publiceert.

## Mappen

```
.
├── index.html             # app-shell
├── css/styles.css         # styling
├── js/                    # vanilla JS (geen build)
│   ├── app.js             # routing + alle modi
│   ├── data.js            # laden + valideren van content.json
│   ├── quiz.js            # vraag-renderer (MC/open/inzicht)
│   ├── srs.js             # spaced repetition
│   └── storage.js         # localStorage helper
├── data/
│   ├── content.json       # de leerstof (begrippen/feiten/verbanden/vragen)
│   └── SCHEMA.md          # uitleg van het formaat
├── raw/                   # foto's van boekpagina's (bron)
└── tools/CONTENT_GUIDE.md # werkwijze: van foto → JSON
```

## Status

- [x] App-shell, navigatie en styling
- [x] Spaced-repetition flashcards (begrippen + feiten)
- [x] Oefenmodus met filter op hoofdstuk/type/moeilijkheid
- [x] Kruisverband-overzicht + inzichtvraag-ronde
- [x] Proeftoets met timer, mix en nakijken
- [x] Schema + voorbeeldcontent voor 4 hoofdstukken (cellen, planten, ecosystemen, ordening)
- [ ] Echte stof uit Stijn's boek invullen vanuit `raw/`-foto's
