export const site = {
  name: 'adand',
  handle: 'weufhsos',
  url: 'https://weufhsos.github.io',
  description: '记录 AI Agent、自动化工具与工程实践的个人工作台。',
  intro:
    '我在这里记录实验、项目和那些值得留下来的工程判断。',
  github: 'https://github.com/weufhsos',
};

export const statusLabels = {
  active: '持续维护',
  exploring: '探索中',
  archived: '已归档',
} as const;

export function formatDate(date: Date) {
  return new Intl.DateTimeFormat('zh-CN', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  }).format(date);
}
