import type { APIRoute } from 'astro';
import { site } from '../site.config';

/* A robots.txt magától követi az astro.config.mjs-ben megadott domaint. */
export const GET: APIRoute = ({ site: astroSite }) => {
  const url = (astroSite ?? new URL(site.url)).href.replace(/\/$/, '');
  return new Response(
    `User-agent: *\nAllow: /\n\nSitemap: ${url}/sitemap-index.xml\n`,
    { headers: { 'Content-Type': 'text/plain; charset=utf-8' } }
  );
};
