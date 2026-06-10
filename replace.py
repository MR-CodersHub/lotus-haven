import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_main = '''      <main class="relative overflow-hidden">
        <!-- Background Mesh -->
        <div class="absolute inset-0 bg-mesh opacity-40 -z-10"></div>

        <!-- 1. Hero Section -->
        <section class="relative mx-auto max-w-7xl px-6 pt-16 pb-24 md:px-8 lg:pt-24 lg:pb-32 overflow-hidden">
          <div class="grid gap-16 lg:grid-cols-2 lg:items-center">
            <div class="space-y-10 z-10">
              <div class="inline-flex items-center gap-3 rounded-full bg-primary-light px-6 py-2 text-sm font-medium text-primary-700 dark:bg-primary-900/40 dark:text-primary-200 shadow-sm border border-primary-100 dark:border-primary-800">
                <span class="flex h-2 w-2 rounded-full bg-primary-600 animate-pulse"></span>
                Discover inner peace
              </div>
              <div class="space-y-6">
                <p class="text-logo text-xs font-bold tracking-[0.5em] text-primary-600 uppercase">Sanctuary for the Soul</p>
                <h1 class="text-5xl font-semibold md:text-7xl tracking-tight leading-[1.1]">Find your center in a <span class="italic text-primary-600 font-display">chaotic</span> world.</h1>
                <p class="text-lg text-slate-600 dark:text-slate-300 font-light leading-relaxed max-w-lg">Experience premium yoga, guided meditation, and holistic wellness programs designed to elevate your mind, body, and spirit.</p>
              </div>
              <div class="flex flex-col gap-5 sm:flex-row pt-4">
                <a href="./pages/register.html" class="btn-primary !px-8 !py-4 text-base shadow-xl shadow-primary-500/20 group hover:shadow-primary-500/30 transition-all">Start Your Journey <svg class="inline-block w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg></a>
                <a href="#schedule" class="btn-secondary !px-8 !py-4 text-base bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 hover:border-primary-300 dark:hover:border-primary-700 transition-all">View Class Schedule</a>
              </div>
            </div>

            <div class="relative z-10 mt-10 lg:mt-0">
              <div class="absolute -top-20 -right-20 h-96 w-96 rounded-full bg-accent-200/40 dark:bg-accent-900/20 blur-[100px] -z-10"></div>
              <div class="absolute -bottom-20 -left-20 h-80 w-80 rounded-full bg-primary-200/40 dark:bg-primary-900/20 blur-[100px] -z-10"></div>
              <div class="glass-card relative overflow-hidden !p-3 group hover:border-primary-300/50 transition-colors duration-500">
                <div class="absolute top-6 left-6 z-20 flex items-center gap-3 bg-white/90 dark:bg-slate-900/90 backdrop-blur-md px-4 py-2 rounded-full shadow-lg">
                  <img src="./assets/images/brand-logo.png" alt="Lotus Haven Logo" class="h-6 w-6">
                  <span class="text-logo text-xs font-bold uppercase tracking-widest text-primary-700 dark:text-primary-300">Lotus Haven</span>
                </div>
                <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1200&q=80" alt="Meditation Practice" class="h-[550px] w-full rounded-[40px] object-cover transition-transform duration-1000 group-hover:scale-105" />
                <div class="absolute bottom-10 left-10 right-10 z-20">
                  <div class="bg-white/80 dark:bg-slate-900/80 backdrop-blur-xl p-6 rounded-[28px] flex items-center justify-between border border-white/20 dark:border-slate-700/50 shadow-2xl">
                    <div>
                      <p class="text-[10px] font-bold uppercase tracking-widest text-primary-600 dark:text-primary-400 mb-1">Live Now</p>
                      <h3 class="text-lg font-semibold text-slate-900 dark:text-white">Morning Vinyasa Flow</h3>
                    </div>
                    <a href="./pages/login.html" class="flex items-center justify-center h-10 w-10 rounded-full bg-primary-600 text-white hover:bg-primary-700 transition-colors">
                      <svg class="w-4 h-4 translate-x-0.5" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 2. Transform Your Mind & Body -->
        <section class="bg-white/60 dark:bg-slate-900/60 py-24 backdrop-blur-md border-y border-slate-200/50 dark:border-slate-800/50">
          <div class="mx-auto max-w-7xl px-6 md:px-8">
            <div class="grid gap-16 lg:grid-cols-2 items-center">
              <div>
                <p class="text-logo text-xs font-bold tracking-widest text-primary-600 uppercase mb-4">Our Mission</p>
                <h2 class="text-4xl font-semibold md:text-5xl leading-tight mb-8">Transform your <span class="font-display italic text-primary-600">mind</span> & body.</h2>
                <div class="space-y-6 text-lg text-slate-600 dark:text-slate-300 font-light leading-relaxed">
                  <p>At Lotus Haven, we believe that true wellness transcends physical exercise. It's a harmonious integration of mental clarity, emotional balance, and physical strength.</p>
                  <p>Our expert-led programs are meticulously crafted to help you detach from daily stressors, cultivate deep self-awareness, and build a sustainable practice that empowers every aspect of your life.</p>
                </div>
                <div class="mt-10">
                  <a href="./pages/about.html" class="inline-flex items-center gap-2 text-primary-600 font-semibold hover:text-primary-700 transition-colors group">
                    Discover our philosophy 
                    <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
                  </a>
                </div>
              </div>
              <div class="grid grid-cols-2 gap-6 relative">
                <div class="absolute inset-0 bg-primary-100/50 dark:bg-primary-900/20 blur-3xl rounded-full -z-10"></div>
                <img src="https://images.unsplash.com/photo-1599901860904-17e086fa2536?auto=format&fit=crop&w=600&q=80" alt="Yoga pose" class="w-full h-72 object-cover rounded-[32px] mt-12 shadow-lg hover:-translate-y-2 transition-transform duration-500">
                <img src="https://images.unsplash.com/photo-1512438248247-f0f2a5a8b7f0?auto=format&fit=crop&w=600&q=80" alt="Meditation" class="w-full h-80 object-cover rounded-[32px] shadow-xl hover:-translate-y-2 transition-transform duration-500">
              </div>
            </div>
          </div>
        </section>

        <!-- 3. Wellness Programs (Replaces Generic Services) -->
        <section class="mx-auto max-w-7xl px-6 py-32 md:px-8">
          <div class="text-center mb-20 max-w-3xl mx-auto space-y-6">
            <p class="text-logo text-xs font-bold tracking-widest text-primary-600 uppercase">Premium Offerings</p>
            <h2 class="text-4xl font-semibold md:text-5xl">Curated Wellness Programs</h2>
            <p class="text-lg text-slate-600 dark:text-slate-400 font-light">Explore our specialized sessions designed to meet you exactly where you are in your wellness journey, from restorative breathing to advanced vinyasa.</p>
          </div>
          
          <div class="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
            <!-- Yoga Sessions -->
            <article class="glass-card group hover:-translate-y-2 transition-all duration-500 !p-8 flex flex-col h-full border border-slate-200/60 dark:border-slate-700/50 hover:border-primary-300 dark:hover:border-primary-600 hover:shadow-2xl hover:shadow-primary-500/10">
              <div class="mb-8 overflow-hidden rounded-[24px]">
                <img src="https://images.unsplash.com/photo-1603988363607-e1e4a66962c6?auto=format&fit=crop&w=800&q=80" alt="Yoga Sessions" class="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-700">
              </div>
              <h3 class="text-2xl font-semibold mb-3">Yoga Sessions</h3>
              <p class="text-slate-600 dark:text-slate-400 font-light leading-relaxed mb-6 flex-grow">Dynamic and restorative flows focusing on alignment, strength, and flexibility. Suitable for all body types.</p>
              <div class="space-y-3 mb-8 pt-6 border-t border-slate-100 dark:border-slate-800">
                <div class="flex justify-between text-sm"><span class="text-slate-500">Skill Level:</span> <span class="font-medium">All Levels</span></div>
                <div class="flex justify-between text-sm"><span class="text-slate-500">Duration:</span> <span class="font-medium">60 - 90 Min</span></div>
                <div class="flex justify-between text-sm"><span class="text-slate-500">Format:</span> <span class="font-medium">Studio & Virtual</span></div>
              </div>
              <a href="./pages/services.html" class="w-full btn-secondary text-center">Explore Yoga</a>
            </article>

            <!-- Meditation Programs -->
            <article class="glass-card group hover:-translate-y-2 transition-all duration-500 !p-8 flex flex-col h-full border border-slate-200/60 dark:border-slate-700/50 hover:border-accent-300 dark:hover:border-accent-600 hover:shadow-2xl hover:shadow-accent-500/10">
              <div class="mb-8 overflow-hidden rounded-[24px]">
                <img src="https://images.unsplash.com/photo-1593811167562-9cef47bfc4d7?auto=format&fit=crop&w=800&q=80" alt="Meditation Programs" class="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-700">
              </div>
              <h3 class="text-2xl font-semibold mb-3">Meditation Programs</h3>
              <p class="text-slate-600 dark:text-slate-400 font-light leading-relaxed mb-6 flex-grow">Guided mindfulness practices to reduce anxiety, improve concentration, and cultivate profound inner stillness.</p>
              <div class="space-y-3 mb-8 pt-6 border-t border-slate-100 dark:border-slate-800">
                <div class="flex justify-between text-sm"><span class="text-slate-500">Skill Level:</span> <span class="font-medium">Beginner Friendly</span></div>
                <div class="flex justify-between text-sm"><span class="text-slate-500">Duration:</span> <span class="font-medium">30 - 45 Min</span></div>
                <div class="flex justify-between text-sm"><span class="text-slate-500">Format:</span> <span class="font-medium">Studio & Audio</span></div>
              </div>
              <a href="./pages/services.html" class="w-full btn-secondary text-center">Explore Meditation</a>
            </article>

            <!-- Breathing Workshops -->
            <article class="glass-card group hover:-translate-y-2 transition-all duration-500 !p-8 flex flex-col h-full border border-slate-200/60 dark:border-slate-700/50 hover:border-primary-300 dark:hover:border-primary-600 hover:shadow-2xl hover:shadow-primary-500/10">
              <div class="mb-8 overflow-hidden rounded-[24px]">
                <img src="https://images.unsplash.com/photo-1522845015757-50bce044e5da?auto=format&fit=crop&w=800&q=80" alt="Breathing Workshops" class="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-700">
              </div>
              <h3 class="text-2xl font-semibold mb-3">Breathing Workshops</h3>
              <p class="text-slate-600 dark:text-slate-400 font-light leading-relaxed mb-6 flex-grow">Pranayama techniques designed to regulate the nervous system, boost immunity, and increase vital energy.</p>
              <div class="space-y-3 mb-8 pt-6 border-t border-slate-100 dark:border-slate-800">
                <div class="flex justify-between text-sm"><span class="text-slate-500">Skill Level:</span> <span class="font-medium">Intermediate</span></div>
                <div class="flex justify-between text-sm"><span class="text-slate-500">Duration:</span> <span class="font-medium">45 Min</span></div>
                <div class="flex justify-between text-sm"><span class="text-slate-500">Format:</span> <span class="font-medium">Studio Only</span></div>
              </div>
              <a href="./pages/services.html" class="w-full btn-secondary text-center">Explore Breathwork</a>
            </article>
          </div>
        </section>

        <!-- 4. Haven Advantage -->
        <section class="bg-primary-900 py-32 overflow-hidden relative text-white">
          <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=2000&q=80')] opacity-10 bg-cover bg-center mix-blend-overlay"></div>
          <div class="absolute top-0 right-0 h-full w-1/2 bg-gradient-to-l from-primary-800 to-transparent skew-x-12 translate-x-32"></div>
          
          <div class="mx-auto max-w-7xl px-6 md:px-8 relative z-10">
            <div class="grid gap-16 lg:grid-cols-2 items-center">
              <div class="space-y-12">
                <div>
                  <p class="text-logo text-xs font-bold tracking-widest text-primary-300 uppercase mb-4">The Haven Advantage</p>
                  <h2 class="text-4xl font-semibold md:text-5xl leading-tight">Why our community stays centered.</h2>
                </div>
                <div class="grid gap-8">
                  <div class="flex gap-6 group">
                    <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-white/10 backdrop-blur-md border border-white/20 group-hover:bg-primary-500 transition-colors">
                      <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 13l4 4L19 7"/></svg>
                    </div>
                    <div>
                      <h4 class="text-xl font-semibold mb-2">Master Instructors</h4>
                      <p class="text-primary-100 font-light leading-relaxed">Guidance from certified, compassionate practitioners with decades of combined global experience.</p>
                    </div>
                  </div>
                  <div class="flex gap-6 group">
                    <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-white/10 backdrop-blur-md border border-white/20 group-hover:bg-primary-500 transition-colors">
                      <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                    </div>
                    <div>
                      <h4 class="text-xl font-semibold mb-2">Digital-First Dashboard</h4>
                      <p class="text-primary-100 font-light leading-relaxed">Manage your wellness journey, track progress, and access recorded sessions through our premium student portal.</p>
                    </div>
                  </div>
                  <div class="flex gap-6 group">
                    <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-white/10 backdrop-blur-md border border-white/20 group-hover:bg-primary-500 transition-colors">
                      <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
                    </div>
                    <div>
                      <h4 class="text-xl font-semibold mb-2">Serene Environments</h4>
                      <p class="text-primary-100 font-light leading-relaxed">Aromatherapy, ambient lighting, and acoustic design craft an atmosphere of immediate calm.</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="relative lg:pl-10">
                <div class="rounded-[48px] overflow-hidden border-8 border-white/10 shadow-2xl relative">
                  <img src="https://images.unsplash.com/photo-1545389336-eaeecece96ef?auto=format&fit=crop&w=1000&q=80" alt="Serene Studio Environment" class="w-full h-auto object-cover hover:scale-105 transition-transform duration-1000" />
                  <div class="absolute inset-0 bg-gradient-to-t from-primary-900/80 to-transparent"></div>
                  <div class="absolute bottom-8 left-8 right-8">
                    <p class="text-2xl font-display italic text-white mb-2">"A true sanctuary in the city."</p>
                    <div class="flex items-center gap-2 text-accent-300">
                      <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                      <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                      <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                      <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                      <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 5. Beginner Programs & Wellness Journey -->
        <section class="py-24 mx-auto max-w-7xl px-6 md:px-8">
          <div class="grid lg:grid-cols-[1fr_1.2fr] gap-16 items-center">
            <div class="relative">
              <div class="absolute inset-0 bg-primary-100 dark:bg-primary-900/30 rounded-[40px] transform -rotate-3 scale-105 -z-10"></div>
              <img src="https://images.unsplash.com/photo-1599447421416-3414500d18a5?auto=format&fit=crop&w=800&q=80" alt="Beginner Yoga" class="rounded-[40px] shadow-xl w-full object-cover h-[500px]" />
              <div class="absolute -bottom-8 -right-8 glass-card !p-6 !rounded-3xl border border-white/40 dark:border-slate-700/50 shadow-2xl max-w-[200px]">
                <p class="text-sm font-semibold mb-2">Step-by-step guidance</p>
                <div class="w-full bg-slate-200 dark:bg-slate-700 rounded-full h-2 mb-2">
                  <div class="bg-primary-600 h-2 rounded-full" style="width: 35%"></div>
                </div>
                <p class="text-xs text-slate-500">Foundation Course</p>
              </div>
            </div>
            
            <div class="space-y-10">
              <div>
                <p class="text-logo text-xs font-bold tracking-widest text-primary-600 uppercase mb-4">Start Here</p>
                <h2 class="text-4xl font-semibold md:text-5xl leading-tight mb-6">New to the practice? <br>You belong here.</h2>
                <p class="text-lg text-slate-600 dark:text-slate-300 font-light leading-relaxed">We all start somewhere. Our Foundations program is specifically designed to introduce you to breathwork, basic postures, and meditation in a completely judgment-free zone.</p>
              </div>
              
              <div class="space-y-6 relative before:absolute before:inset-y-0 before:left-[19px] before:w-[2px] before:bg-slate-200 dark:before:bg-slate-800">
                <div class="relative pl-12">
                  <div class="absolute left-0 top-1 h-10 w-10 rounded-full bg-primary-100 dark:bg-primary-900/50 border-4 border-white dark:border-[var(--bg)] flex items-center justify-center text-primary-600 font-bold z-10">1</div>
                  <h4 class="text-xl font-semibold mb-2">Consultation</h4>
                  <p class="text-slate-600 dark:text-slate-400 font-light">A brief 1-on-1 to understand your body, history, and goals.</p>
                </div>
                <div class="relative pl-12">
                  <div class="absolute left-0 top-1 h-10 w-10 rounded-full bg-primary-100 dark:bg-primary-900/50 border-4 border-white dark:border-[var(--bg)] flex items-center justify-center text-primary-600 font-bold z-10">2</div>
                  <h4 class="text-xl font-semibold mb-2">Foundation Classes</h4>
                  <p class="text-slate-600 dark:text-slate-400 font-light">Learn the fundamental poses and breathing techniques safely.</p>
                </div>
                <div class="relative pl-12">
                  <div class="absolute left-0 top-1 h-10 w-10 rounded-full bg-primary-100 dark:bg-primary-900/50 border-4 border-white dark:border-[var(--bg)] flex items-center justify-center text-primary-600 font-bold z-10">3</div>
                  <h4 class="text-xl font-semibold mb-2">Guided Growth</h4>
                  <p class="text-slate-600 dark:text-slate-400 font-light">Transition into regular classes with confidence and a solid base.</p>
                </div>
              </div>
              
              <a href="./pages/register.html" class="btn-primary inline-flex mt-4">Join Foundations Program</a>
            </div>
          </div>
        </section>

        <!-- 6. Meet Our Instructors -->
        <section class="bg-slate-50 dark:bg-slate-900/30 py-32 border-y border-slate-200/50 dark:border-slate-800/50">
          <div class="mx-auto max-w-7xl px-6 md:px-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
              <div class="max-w-2xl">
                <p class="text-logo text-xs font-bold tracking-widest text-primary-600 uppercase mb-4">Guiding Lights</p>
                <h2 class="text-4xl font-semibold md:text-5xl">Meet our expert instructors</h2>
              </div>
              <a href="./pages/about.html" class="text-primary-600 font-semibold hover:text-primary-700 hover:underline underline-offset-4 transition-all">View all instructors &rarr;</a>
            </div>
            
            <div class="grid gap-8 md:grid-cols-3">
              <!-- Instructor 1 -->
              <div class="group cursor-pointer">
                <div class="relative overflow-hidden rounded-[32px] mb-6 aspect-[4/5]">
                  <img src="https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&w=600&q=80" alt="Sarah Jenkins" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                  <div class="absolute inset-0 bg-gradient-to-t from-slate-900/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                  <div class="absolute bottom-0 left-0 right-0 p-6 translate-y-4 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                    <p class="text-white text-sm">"Yoga is the journey of the self, through the self, to the self."</p>
                  </div>
                </div>
                <h3 class="text-2xl font-semibold mb-1">Sarah Jenkins</h3>
                <p class="text-primary-600 text-sm font-medium uppercase tracking-wider mb-3">Lead Vinyasa Instructor</p>
                <p class="text-slate-600 dark:text-slate-400 font-light text-sm">500-RYT certified with 10+ years helping students build strength and fluid mobility.</p>
              </div>
              
              <!-- Instructor 2 -->
              <div class="group cursor-pointer">
                <div class="relative overflow-hidden rounded-[32px] mb-6 aspect-[4/5]">
                  <img src="https://images.unsplash.com/photo-1549476464-37392f717541?auto=format&fit=crop&w=600&q=80" alt="David Chen" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                  <div class="absolute inset-0 bg-gradient-to-t from-slate-900/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                  <div class="absolute bottom-0 left-0 right-0 p-6 translate-y-4 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                    <p class="text-white text-sm">"Stillness is where creativity and healing begin."</p>
                  </div>
                </div>
                <h3 class="text-2xl font-semibold mb-1">David Chen</h3>
                <p class="text-primary-600 text-sm font-medium uppercase tracking-wider mb-3">Meditation & Breathwork</p>
                <p class="text-slate-600 dark:text-slate-400 font-light text-sm">Specializes in Vipassana and modern neuroscience-backed mindfulness techniques.</p>
              </div>
              
              <!-- Instructor 3 -->
              <div class="group cursor-pointer">
                <div class="relative overflow-hidden rounded-[32px] mb-6 aspect-[4/5]">
                  <img src="https://images.unsplash.com/photo-1552196563-55cd4e45efb3?auto=format&fit=crop&w=600&q=80" alt="Maya Patel" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                  <div class="absolute inset-0 bg-gradient-to-t from-slate-900/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                  <div class="absolute bottom-0 left-0 right-0 p-6 translate-y-4 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                    <p class="text-white text-sm">"Embrace where you are today; it's exactly where you need to be."</p>
                  </div>
                </div>
                <h3 class="text-2xl font-semibold mb-1">Maya Patel</h3>
                <p class="text-primary-600 text-sm font-medium uppercase tracking-wider mb-3">Restorative & Yin</p>
                <p class="text-slate-600 dark:text-slate-400 font-light text-sm">Passionate about deep tissue release, recovery, and holistic trauma-informed care.</p>
              </div>
            </div>
          </div>
        </section>

        <!-- 7. Class Schedule Snippet -->
        <section id="schedule" class="mx-auto max-w-7xl px-6 py-32 md:px-8">
          <div class="text-center mb-16">
            <p class="text-logo text-xs font-bold tracking-widest text-primary-600 uppercase mb-4">Find Your Time</p>
            <h2 class="text-4xl font-semibold md:text-5xl">Upcoming Classes</h2>
          </div>
          
          <div class="glass-card !p-0 overflow-hidden border border-slate-200/60 dark:border-slate-700/50 rounded-[32px]">
            <div class="overflow-x-auto">
              <table class="w-full text-left border-collapse">
                <thead>
                  <tr class="bg-slate-50 dark:bg-slate-900/50 border-b border-slate-200 dark:border-slate-700/50">
                    <th class="p-6 font-semibold text-slate-500 uppercase tracking-wider text-xs">Time</th>
                    <th class="p-6 font-semibold text-slate-500 uppercase tracking-wider text-xs">Class</th>
                    <th class="p-6 font-semibold text-slate-500 uppercase tracking-wider text-xs">Instructor</th>
                    <th class="p-6 font-semibold text-slate-500 uppercase tracking-wider text-xs">Level</th>
                    <th class="p-6 font-semibold text-slate-500 uppercase tracking-wider text-xs text-right">Action</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
                  <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/30 transition-colors">
                    <td class="p-6 font-medium whitespace-nowrap">07:00 AM</td>
                    <td class="p-6 font-semibold">Sunrise Vinyasa</td>
                    <td class="p-6 text-slate-600 dark:text-slate-400">Sarah Jenkins</td>
                    <td class="p-6"><span class="px-3 py-1 rounded-full bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400 text-xs font-medium">All Levels</span></td>
                    <td class="p-6 text-right"><a href="./pages/login.html" class="text-primary-600 font-semibold hover:underline">Book</a></td>
                  </tr>
                  <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/30 transition-colors">
                    <td class="p-6 font-medium whitespace-nowrap">09:30 AM</td>
                    <td class="p-6 font-semibold">Morning Meditation</td>
                    <td class="p-6 text-slate-600 dark:text-slate-400">David Chen</td>
                    <td class="p-6"><span class="px-3 py-1 rounded-full bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400 text-xs font-medium">Beginner</span></td>
                    <td class="p-6 text-right"><a href="./pages/login.html" class="text-primary-600 font-semibold hover:underline">Book</a></td>
                  </tr>
                  <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/30 transition-colors">
                    <td class="p-6 font-medium whitespace-nowrap">12:00 PM</td>
                    <td class="p-6 font-semibold">Power Flow (Express)</td>
                    <td class="p-6 text-slate-600 dark:text-slate-400">Sarah Jenkins</td>
                    <td class="p-6"><span class="px-3 py-1 rounded-full bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400 text-xs font-medium">Intermediate</span></td>
                    <td class="p-6 text-right"><a href="./pages/login.html" class="text-primary-600 font-semibold hover:underline">Book</a></td>
                  </tr>
                  <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/30 transition-colors">
                    <td class="p-6 font-medium whitespace-nowrap">06:00 PM</td>
                    <td class="p-6 font-semibold">Restorative Yin</td>
                    <td class="p-6 text-slate-600 dark:text-slate-400">Maya Patel</td>
                    <td class="p-6"><span class="px-3 py-1 rounded-full bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400 text-xs font-medium">All Levels</span></td>
                    <td class="p-6 text-right"><a href="./pages/login.html" class="text-primary-600 font-semibold hover:underline">Book</a></td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="p-6 border-t border-slate-200 dark:border-slate-700/50 text-center bg-slate-50 dark:bg-slate-900/20">
              <a href="./pages/services.html" class="text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-primary-600 dark:hover:text-primary-400">View Full Weekly Schedule &rarr;</a>
            </div>
          </div>
        </section>

        <!-- 8. Testimonials & Member Success -->
        <section class="bg-primary-50 dark:bg-slate-900/50 py-32 border-y border-primary-100 dark:border-slate-800">
          <div class="mx-auto max-w-7xl px-6 md:px-8">
            <div class="text-center mb-20 space-y-4">
              <p class="text-logo text-xs font-bold tracking-widest text-primary-600 uppercase">Success Stories</p>
              <h2 class="text-4xl font-semibold md:text-5xl">Transformations start here</h2>
            </div>
            
            <div class="grid gap-8 md:grid-cols-3">
              <div class="glass-card !bg-white/80 dark:!bg-slate-800/80 !p-8 flex flex-col justify-between border-t-4 border-primary-500 shadow-xl hover:-translate-y-2 transition-transform duration-300">
                <div class="text-accent-500 mb-6 flex gap-1">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                </div>
                <p class="text-lg leading-relaxed text-slate-700 dark:text-slate-300 italic mb-8">"Lotus Haven completely transformed my relationship with stress. The guided meditation programs are incredibly intuitive and the studio itself is a dream."</p>
                <div class="flex items-center gap-4 mt-auto">
                  <div class="h-12 w-12 rounded-full bg-slate-200 overflow-hidden shrink-0">
                    <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=150&q=80" alt="Elena Vance" class="h-full w-full object-cover" />
                  </div>
                  <div>
                    <p class="font-bold text-sm">Elena Vance</p>
                    <p class="text-xs text-slate-500 uppercase tracking-widest">Premium Member</p>
                  </div>
                </div>
              </div>

              <div class="glass-card !bg-white/80 dark:!bg-slate-800/80 !p-8 flex flex-col justify-between border-t-4 border-primary-500 shadow-xl hover:-translate-y-2 transition-transform duration-300">
                <div class="text-accent-500 mb-6 flex gap-1">
                  <!-- 5 stars -->
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                </div>
                <p class="text-lg leading-relaxed text-slate-700 dark:text-slate-300 italic mb-8">"The dashboard makes it so easy to book sessions around my busy work schedule. I've never been more consistent with my practice. I feel stronger than ever."</p>
                <div class="flex items-center gap-4 mt-auto">
                  <div class="h-12 w-12 rounded-full bg-slate-200 overflow-hidden shrink-0">
                    <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80" alt="Marcus Thorne" class="h-full w-full object-cover" />
                  </div>
                  <div>
                    <p class="font-bold text-sm">Marcus Thorne</p>
                    <p class="text-xs text-slate-500 uppercase tracking-widest">Vinyasa Regular</p>
                  </div>
                </div>
              </div>

              <div class="glass-card !bg-white/80 dark:!bg-slate-800/80 !p-8 flex flex-col justify-between border-t-4 border-primary-500 shadow-xl hover:-translate-y-2 transition-transform duration-300">
                <div class="text-accent-500 mb-6 flex gap-1">
                  <!-- 5 stars -->
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                </div>
                <p class="text-lg leading-relaxed text-slate-700 dark:text-slate-300 italic mb-8">"I started with the beginner foundations class six months ago and the difference in my mental clarity is astounding. The instructors truly care about your progress."</p>
                <div class="flex items-center gap-4 mt-auto">
                  <div class="h-12 w-12 rounded-full bg-slate-200 overflow-hidden shrink-0">
                    <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=150&q=80" alt="Sophia Lee" class="h-full w-full object-cover" />
                  </div>
                  <div>
                    <p class="font-bold text-sm">Sophia Lee</p>
                    <p class="text-xs text-slate-500 uppercase tracking-widest">Foundations Alumni</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 9. Strong Call-to-action & Motivation -->
        <section class="mx-auto max-w-7xl px-6 pb-32 md:px-8">
          <div class="relative overflow-hidden rounded-[60px] bg-primary-700 px-8 py-24 text-center text-white md:px-16 md:py-32 shadow-2xl group">
            <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,_var(--tw-gradient-stops))] from-white/20 to-transparent"></div>
            <div class="absolute -left-32 -top-32 w-96 h-96 bg-primary-500/50 blur-[100px] rounded-full group-hover:scale-150 transition-transform duration-1000"></div>
            <div class="absolute -right-32 -bottom-32 w-96 h-96 bg-accent-500/30 blur-[100px] rounded-full group-hover:scale-150 transition-transform duration-1000"></div>
            
            <div class="relative z-10 space-y-10 max-w-3xl mx-auto">
              <h2 class="text-4xl font-semibold md:text-6xl tracking-tight leading-tight">Your mat is waiting. <br>Begin today.</h2>
              <p class="text-xl text-primary-100 font-light leading-relaxed">Join over 1,000 students who have found their center at Lotus Haven. Book your first class or schedule a free wellness consultation to get started.</p>
              <div class="flex flex-col items-center gap-6 sm:flex-row sm:justify-center pt-6">
                <a href="./pages/register.html" class="btn-secondary !bg-white !text-primary-800 border-none px-12 py-5 text-lg hover:shadow-2xl hover:-translate-y-1 transition-all w-full sm:w-auto">Start Free Trial</a>
                <a href="./pages/pricing.html" class="text-base font-semibold underline underline-offset-8 decoration-primary-400 hover:decoration-white hover:text-white transition-all">View Membership Plans</a>
              </div>
            </div>
          </div>
        </section>
      </main>'''

html = re.sub(r'<main class="relative overflow-hidden">.*?</main>', new_main, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
