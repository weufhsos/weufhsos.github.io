import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://weufhsos.github.io',
  output: 'static',
  trailingSlash: 'always',
  integrations: [
    mdx(),
    sitemap({
      // 旧地址跳转页声明了 noindex，不应出现在 sitemap 里
      filter: (page) => !page.includes('/2026/01/20/hello-world/'),
    }),
  ],
});
