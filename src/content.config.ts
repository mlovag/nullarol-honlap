import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/* A leckék: src/content/leckek/*.md  — a fájl neve adja a webcímet */
const leckek = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/leckek' }),
  schema: z.object({
    kod: z.string(),
    cim: z.string(),
    szemeszter: z.number(),
    modul: z.string(),
    modulSorszam: z.number(),
    sorszam: z.number(),
    hossz: z.number().default(30),
    kulcsuzenet: z.string(),
    valosEset: z.string().optional(),
    hetiMegfigyeles: z.string().optional(),
    vitaLecke: z.boolean().default(false),
    statusz: z.enum(['megirva', 'vazlat', 'tervezett']).default('megirva'),
    szuloiKartya: z
      .object({
        mitViszHaza: z.string().optional(),
        elofeltetel: z.string().optional(),
        felreertes: z.string().optional(),
        amitNeMondj: z.string().optional(),
        aSzamokrol: z.string().optional(),
        amireKeszulj: z.string().optional(),
      })
      .optional(),
    fogalmak: z
      .array(z.object({ hu: z.string(), en: z.string(), mit: z.string() }))
      .default([]),
  }),
});

/* A szabad szöveges oldalak: src/content/oldalak/*.md */
const oldalak = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/oldalak' }),
  schema: z.object({
    cim: z.string(),
    leiras: z.string().optional(),
  }),
});

export const collections = { leckek, oldalak };
