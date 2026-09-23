/* A tananyag közös segédfüggvényei: szemeszter-címek és a leckék csoportosítása. */
import { getCollection } from 'astro:content';
import { szemeszterek } from '../site.config';

/** Egy szemeszter saját oldalának címe, pl. /tananyag/1-szemeszter/ */
export const szemeszterUrl = (szam: number) => `/tananyag/${szam}-szemeszter/`;

/** Szemeszter → modulok → leckék (csak a megjelent, `megirva` leckék). */
export async function szemeszterCsoportok() {
  const leckek = (await getCollection('leckek'))
    .filter((l) => l.data.statusz === 'megirva')
    .sort((a, b) => a.data.kod.localeCompare(b.data.kod));

  return szemeszterek.map((sz) => {
    const sajat = leckek.filter((l) => l.data.szemeszter === sz.szam);
    const modulok = [...new Set(sajat.map((l) => l.data.modulSorszam))]
      .sort((a, b) => a - b)
      .map((msz) => {
        const benne = sajat
          .filter((l) => l.data.modulSorszam === msz)
          .sort((a, b) => a.data.sorszam - b.data.sorszam);
        return { szam: msz, cim: benne[0]?.data.modul ?? '', leckek: benne };
      });
    return { ...sz, url: szemeszterUrl(sz.szam), modulok, db: sajat.length };
  });
}
