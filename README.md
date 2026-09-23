# adand personal site

这是 `weufhsos.github.io` 的源工程，使用 Astro 构建并部署到 GitHub Pages。

## 本地预览

```bash
npm install
npm run dev
```

## 写文章

在 `src/content/posts/` 新建 `.md` 或 `.mdx` 文件，填写 frontmatter 后提交到 `main`。GitHub Actions 会自动检查、构建并发布网站。

## 写项目

在 `src/content/projects/` 新建 `.md` 或 `.mdx` 文件，按照已有项目文件填写标题、描述、状态、技术栈和仓库链接。

## 发布前需要替换的占位内容

- `src/data/site.ts` 中的个人简介和联系方式。
- `src/pages/about.astro` 中的自我介绍。
- `src/content/projects/` 中项目的真实描述、成果和截图。
- `public/favicon.svg` 和站点分享图。

旧版 Hexo 静态站点的恢复点为本地 Git tag：`legacy-hexo-2026-09`。
