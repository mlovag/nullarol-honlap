# Nulláról — honlap

Magyar nyelvű közgazdaságtan- és pénzügyi tananyag honlapja.
Astro-val készült, statikus oldal. Nincs adatbázis, nincs szerver, nincs havi díj.

## Mit hol találsz

| Mit akarsz csinálni | Melyik fájlt nyisd meg |
|---|---|
| Új menüpont felvétele | `src/site.config.ts` — a `menu` lista |
| A honlap nevének, alcímének módosítása | `src/site.config.ts` — a `site` blokk |
| Szemeszterek nevének módosítása | `src/site.config.ts` — a `szemeszterek` lista |
| Egy lecke szövegének javítása | `src/content/leckek/<lecke>.md` |
| Új lecke felvétele | új `.md` fájl a `src/content/leckek/` mappába |
| Az Előszó szövege | `src/content/oldalak/eloszo.md` |
| Új szöveges oldal | új `.md` fájl a `src/content/oldalak/` mappába |
| Színek, betűméretek | `src/styles/global.css` |
| A honlap címe (domain) | `astro.config.mjs` — a `site:` sor |

## Új menüpont felvétele — két lépés

1. `src/content/oldalak/befektetes.md` — új fájl:

```markdown
---
cim: "Befektetés"
leiras: "Rövid leírás, ez kerül a Google találati listájára is."
---

Ide jön az oldal szövege.
```

2. `src/site.config.ts` — egy új sor a `menu` listába:

```ts
{ cim: 'Befektetés', url: '/befektetes/' },
```

Ennyi. A fájl neve adja a webcímet: `befektetes.md` → `/befektetes/`.

## Új lecke felvétele

Másolj le egy meglévő leckét a `src/content/leckek/` mappából, és írd át.
A fájl elején lévő `---` közötti rész a lecke adatlapja; a `statusz: "megirva"`
sortól függ, hogy megjelenik-e a honlapon:

- `megirva` → megjelenik
- `vazlat` vagy `tervezett` → NEM jelenik meg (nyugodtan feltöltheted félkészen)

## Helyi kipróbálás (nem kötelező)

```bash
npm install
npm run dev     # http://localhost:4321
npm run build   # a kész honlap a dist/ mappába kerül
```

## Böngészős szerkesztő

A `.pages.yml` fájl a Pages CMS (pagescms.org) beállítása. Ha a szerkesztőben
a lecke szövegének formázása elromlik, írd át benne az utolsó sorban a
`type: rich-text` részt `type: text`-re — akkor sima szövegmezőt ad.
