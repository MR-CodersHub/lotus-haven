document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.querySelector('[data-action="toggle-theme"]');
  const directionToggle = document.querySelector('[data-action="toggle-rtl"]');
  const blogSearch = document.querySelector('#blog-search');
  const blogFilter = document.querySelector('#blog-filter');

  function setTheme(theme) {
    document.documentElement.dataset.theme = theme;
    localStorage.setItem('theme', theme);
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }

  function setDirection(direction) {
    document.documentElement.dir = direction;
    localStorage.setItem('direction', direction);
    if (direction === 'rtl') {
      document.documentElement.classList.add('rtl');
    } else {
      document.documentElement.classList.remove('rtl');
    }
  }

  const savedTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  const savedDirection = localStorage.getItem('direction') || 'ltr';
  setTheme(savedTheme);
  setDirection(savedDirection);

  themeToggle?.addEventListener('click', () => {
    const nextTheme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(nextTheme);
  });

  directionToggle?.addEventListener('click', () => {
    const nextDirection = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl';
    setDirection(nextDirection);
  });

  function updateBlogCards() {
    const query = blogSearch?.value.toLowerCase().trim() || '';
    const category = blogFilter?.value || 'all';
    document.querySelectorAll('.blog-card').forEach((card) => {
      const title = card.dataset.title.toLowerCase();
      const tags = card.dataset.tags.toLowerCase();
      const matchesQuery = title.includes(query) || tags.includes(query);
      const matchesCategory = category === 'all' || card.dataset.category === category;
      card.classList.toggle('hidden', !(matchesQuery && matchesCategory));
    });
  }

  blogSearch?.addEventListener('input', updateBlogCards);
  blogFilter?.addEventListener('change', updateBlogCards);
});
