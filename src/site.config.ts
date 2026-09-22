/* ============================================================
   A HONLAP BEÁLLÍTÁSAI  —  ezt a fájlt szabad bátran szerkeszteni
   ============================================================ */

export const site = {
  nev: 'Nulláról',
  alcim: 'Közgazdaságtan és pénzügyek — érthetően',
  leiras:
    'Ingyenes, magyar nyelvű közgazdaságtan- és pénzügyi tananyag tizenéveseknek, ' +
    'szülőknek és tanároknak. Öt szemeszter, leckéről leckére, valós példákkal.',
  url: 'https://www.nullarol.hu',
  nyelv: 'hu',
  email: '',            // ha ide beírsz egy címet, megjelenik a lábléc kapcsolat sorában
  youtube: '',          // pl. 'https://youtube.com/@nullarol' — ha üres, nem jelenik meg
};

/* ------------------------------------------------------------
   A MENÜ
   ------------------------------------------------------------
   ÚJ MENÜPONT HOZZÁADÁSA = egyetlen új sor ebbe a listába.

   Például egy új "Befektetés" menüpont:
     { cim: 'Befektetés', url: '/befektetes/' },
   ...és mellé egy új fájl ide: src/content/oldalak/befektetes.md

   A sorrend itt felülről lefelé = a menü sorrendje balról jobbra.
------------------------------------------------------------ */

export type MenuElem = {
  cim: string;
  url: string;
  leiras?: string;
};

export const menu: MenuElem[] = [
  { cim: 'Előszó',   url: '/eloszo/',   leiras: 'Miről szól ez az oldal, és kinek készült' },
  { cim: 'Tananyag', url: '/tananyag/', leiras: 'A teljes tanterv, leckéről leckére' },
];

/* A szemeszterek neve és leírása. Új szemeszter = új sor. */
export const szemeszterek = [
  { szam: 1, cim: 'Mikroökonómia és a vállalat működése', korosztaly: '14–15 év',
    fokusz: 'Döntés, piac, ár, egy cég belülről' },
  { szam: 2, cim: 'Makroökonómia — magyar szemmel', korosztaly: '16 év',
    fokusz: 'GDP, infláció, MNB, állam, forint, EU' },
  { szam: 3, cim: 'Személyes pénzügyek, hitel, befektetés', korosztaly: '17–18 év',
    fokusz: 'Költségvetés, bank, hitel, befektetés, kockázat' },
  { szam: 4, cim: 'Vállalkozásindítás a gyakorlatban', korosztaly: '18+',
    fokusz: 'Ötlettől a működő cégig, magyar keretek' },
  { szam: 5, cim: 'Tőkepiacok és befektetés mélységben', korosztaly: '18+',
    fokusz: 'Beszámolóolvasás, értékelés, portfólió' },
];
