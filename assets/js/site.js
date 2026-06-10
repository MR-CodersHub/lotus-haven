document.addEventListener('DOMContentLoaded', () => {
  const themeToggles = document.querySelectorAll('[data-action="toggle-theme"]');
  const directionToggles = document.querySelectorAll('[data-action="toggle-rtl"]');
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

  themeToggles.forEach(toggle => {
    toggle.addEventListener('click', () => {
      const nextTheme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      setTheme(nextTheme);
    });
  });

  directionToggles.forEach(toggle => {
    toggle.addEventListener('click', () => {
      const nextDirection = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl';
      setDirection(nextDirection);
    });
  });

  const profileToggle = document.querySelector('[data-action="profile-menu-toggle"]');
  const profileMenu = document.querySelector('[data-profile-menu]');

  profileToggle?.addEventListener('click', (e) => {
    e.stopPropagation();
    profileMenu?.classList.toggle('hidden');
    mobileMenu?.classList.add('hidden'); // Close mobile menu if profile is opened
  });

  const mobileToggle = document.querySelector('[data-action="mobile-menu-toggle"]');
  const mobileMenu = document.querySelector('[data-mobile-menu]');

  mobileToggle?.addEventListener('click', (e) => {
    e.stopPropagation();
    mobileMenu?.classList.toggle('hidden');
    profileMenu?.classList.add('hidden'); // Close profile menu if mobile menu is opened
  });

  document.addEventListener('click', (e) => {
    if (!profileToggle?.contains(e.target) && !profileMenu?.contains(e.target)) {
      profileMenu?.classList.add('hidden');
    }
    if (!mobileToggle?.contains(e.target) && !mobileMenu?.contains(e.target)) {
      mobileMenu?.classList.add('hidden');
    }
  });

  // Active Nav Links logic
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href) {
      try {
        const linkPath = new URL(href, window.location.href).pathname;
        const currentPathname = window.location.pathname;
        
        // Handle cases like / and /index.html
        const normalize = (p) => p.endsWith('/') ? p + 'index.html' : p;
        
        if (normalize(linkPath) === normalize(currentPathname)) {
          link.classList.add('active');
        }
      } catch (e) {
        console.error('Error parsing nav link:', e);
      }
    }
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

  // Services filter functionality
  const serviceFilterButtons = document.querySelectorAll('[data-action="services-filter"]');
  const serviceCards = document.querySelectorAll('article[data-category]');

  function setActiveFilterButton(activeBtn) {
    serviceFilterButtons.forEach(btn => {
      if (btn === activeBtn) {
        btn.classList.remove('bg-white','border','border-slate-200','text-slate-600');
        btn.classList.add('bg-primary-600','text-white','shadow-lg','shadow-primary-500/20');
      } else {
        btn.classList.add('bg-white','border','border-slate-200','text-slate-600');
        btn.classList.remove('bg-primary-600','text-white','shadow-lg','shadow-primary-500/20');
      }
    });
  }

  function filterServices(category) {
    serviceCards.forEach(card => {
      const cat = card.dataset.category;
      if (category === 'all' || cat === category) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  }

  serviceFilterButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const filter = btn.dataset.filter || 'all';
      setActiveFilterButton(btn);
      filterServices(filter);
    });
  });
});
