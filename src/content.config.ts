import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const posts = defineCollection({
  loader: glob({ base: './src/content/posts', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    featured: z.boolean().default(false),
    readingTime: z.number().int().positive().default(5),
    cover: z.string().optional(),
    coverAlt: z.string().optional(),
  }),
});

const projects = defineCollection({
  loader: glob({ base: './src/content/projects', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    status: z.enum(['active', 'exploring', 'archived']).default('active'),
    featured: z.boolean().default(false),
    languages: z.array(z.string()).default([]),
    repoUrl: z.url(),
    demoUrl: z.url().optional(),
    order: z.number().int().default(99),
  }),
});

export const collections = { posts, projects };
