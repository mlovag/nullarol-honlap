// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// A honlap végleges címe. Ha másik domaint veszel, ITT kell átírni.
export default defineConfig({
  site: 'https://www.nullarol.hu',
  integrations: [sitemap()],
  build: { format: 'directory' },
});
