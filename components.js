/**
 * FlossByte — Shared Components (Navigation + Footer)
 * Injected via JavaScript so all pages stay perfectly in sync.
 */

const SITE = {
  phone: '(669) 237-2264',
  phoneHref: 'tel:6692372264',
  email: 'hello@flossbyte.com',
  emailHref: 'mailto:hello@flossbyte.com',
  year: new Date().getFullYear(),
  gaId: 'G-XXXXXXXXXX', // Replace with your Google Analytics Measurement ID
};

/* ── Google Analytics ──────────────────────────────────────── */
if (SITE.gaId && SITE.gaId !== 'G-XXXXXXXXXX') {
  const gs = document.createElement('script');
  gs.async = true;
  gs.src = 'https://www.googletagmanager.com/gtag/js?id=' + SITE.gaId;
  document.head.appendChild(gs);
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', SITE.gaId);
}

/* ── Helper: resolve relative paths ─────────────────────── */
function rootPath(path) {
  // Use absolute paths from the site root for reliability across all hosting platforms
  const base = document.querySelector('base')?.href || '/';
  return '/' + path;
}

/* ── Navigation HTML ─────────────────────────────────────── */
function renderNav() {
  const r = rootPath;
  const nav = document.createElement('nav');
  nav.className = 'site-nav';
  nav.setAttribute('aria-label', 'Main navigation');
  nav.innerHTML = `
    <div class="nav-inner">
      <a class="nav-logo" href="${r('index.html')}" aria-label="FlossByte Home"
         style="display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none;">
        <img src="${r('assets/logo-icon.png')}" alt="" width="38" height="49" aria-hidden="true" style="flex-shrink:0;object-fit:contain;" />
        <span style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:0.85rem;
                     letter-spacing:-0.03em;line-height:1;color:#ffffff;">
          Floss<span style="color:#00BFA5;">Byte</span>
        </span>
      </a>

      <div class="nav-links" id="nav-links">
        <a href="${r('index.html')}" id="nav-home">Home</a>
        <a href="${r('services.html')}" id="nav-services">Services</a>
        <a href="${r('pricing.html')}" id="nav-pricing">Pricing</a>
        <a href="${r('about.html')}" id="nav-about">About</a>
        <a href="${r('why-flossbyte.html')}" id="nav-why">Why FlossByte</a>
        <div class="nav-dropdown">
          <span class="nav-dropdown-toggle">Resources
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </span>
          <div class="nav-dropdown-menu">
            <a href="${r('blog/index.html')}">Blog</a>
            <a href="${r('hipaa-compliance.html')}">HIPAA Compliance</a>
            <a href="${r('faqs.html')}">FAQs</a>
          </div>
        </div>
        <a href="${r('contact.html')}" id="nav-contact">Contact</a>
      </div>

      <div class="nav-cta">
        <a class="nav-phone" href="${SITE.phoneHref}">${SITE.phone}</a>
        <a class="btn btn-primary btn-sm" href="${r('contact.html')}">Free Assessment</a>
      </div>

      <button class="nav-mobile-toggle" id="mobile-toggle" aria-label="Toggle mobile menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>

    <!-- Mobile Navigation -->
    <div class="nav-mobile" id="nav-mobile" role="navigation" aria-label="Mobile navigation">
      <a href="${r('index.html')}">Home</a>
      <a href="${r('services.html')}">Services</a>
      <a href="${r('pricing.html')}">Pricing</a>
      <a href="${r('about.html')}">About</a>
      <a href="${r('why-flossbyte.html')}">Why FlossByte</a>
      <div class="mobile-divider"></div>
      <a href="${r('blog/index.html')}">Blog</a>
      <a href="${r('hipaa-compliance.html')}">HIPAA Compliance</a>
      <a href="${r('faqs.html')}">FAQs</a>
      <div class="mobile-divider"></div>
      <a href="${SITE.phoneHref}" style="color: var(--color-teal)">${SITE.phone}</a>
      <a class="mobile-cta" href="${r('contact.html')}">📋 Get Free IT Assessment</a>
    </div>
  `;
  document.body.insertBefore(nav, document.body.firstChild);

  // Scroll behavior
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 20);
  });

  // Mobile toggle
  const toggle = document.getElementById('mobile-toggle');
  const mobileNav = document.getElementById('nav-mobile');
  toggle.addEventListener('click', () => {
    const isOpen = mobileNav.classList.toggle('open');
    toggle.classList.toggle('open', isOpen);
    toggle.setAttribute('aria-expanded', isOpen);
  });

  // Close mobile nav on link click
  mobileNav.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      mobileNav.classList.remove('open');
      toggle.classList.remove('open');
    });
  });

  // Active state
  const currentPath = window.location.pathname.toLowerCase();
  document.querySelectorAll('.nav-links a, .nav-mobile a').forEach(link => {
    const href = link.getAttribute('href') || '';
    if (!href) return;
    const linkBase = href.split('/').pop().split('#')[0].toLowerCase();
    const currentBase = currentPath.split('/').pop().split('#')[0].toLowerCase() || 'index.html';
    if (linkBase === currentBase || (linkBase === 'index.html' && currentBase === '')) {
      link.classList.add('active');
    }
  });
}

/* ── Footer HTML ─────────────────────────────────────────── */
function renderFooter() {
  const r = rootPath;
  const footer = document.createElement('footer');
  footer.className = 'site-footer';
  footer.setAttribute('aria-label', 'Site footer');
  footer.innerHTML = `
    <div class="container">
      <div class="footer-grid">

        <!-- Brand -->
        <div class="footer-brand">
          <a href="${r('index.html')}" style="display:inline-block;text-decoration:none;margin-bottom:12px;">
            <img src="${r('assets/logo-icon.png')}" alt="FlossByte" width="42" height="54" style="object-fit:contain;" />
          </a>
          <p class="footer-tagline">HIPAA-compliant managed IT services built exclusively for dental practices across the Peninsula, East Bay, and South Bay.</p>
          <div class="footer-contact">
            <a href="${SITE.phoneHref}">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2.18h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              ${SITE.phone}
            </a>
            <a href="${SITE.emailHref}">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              ${SITE.email}
            </a>
          </div>
        </div>

        <!-- Company -->
        <div>
          <p class="footer-heading">Company</p>
          <div class="footer-links">
            <a href="${r('about.html')}">About FlossByte</a>
            <a href="${r('why-flossbyte.html')}">Why FlossByte</a>
            <a href="${r('contact.html')}">Contact Us</a>
          </div>
        </div>

        <!-- Services -->
        <div>
          <p class="footer-heading">Services</p>
          <div class="footer-links">
            <a href="${r('services.html')}">All Services</a>
            <a href="${r('hipaa-compliance.html')}">HIPAA Compliance</a>
            <a href="${r('pricing.html')}">Pricing</a>
            <a href="${r('faqs.html')}">FAQs</a>
          </div>
        </div>

        <!-- Service Areas -->
        <div>
          <p class="footer-heading">Service Areas</p>
          <div class="footer-links">
            <a href="${r('locations/peninsula.html')}">Peninsula & SF</a>
            <a href="${r('locations/east-bay.html')}">East Bay</a>
            <a href="${r('locations/south-bay.html')}">South Bay</a>
          </div>
        </div>

        <!-- Social -->
        <div>
          <p class="footer-heading">Connect</p>
          <div class="footer-links">
            <a href="https://www.linkedin.com/company/flossbyte" target="_blank" rel="noopener">LinkedIn</a>
            <a href="https://www.google.com/maps/place/FlossByte/@37.4705913,-124.7927058,7z/data=!3m1!4b1!4m6!3m5!1s0x2ab73c3b8e348151:0x7e405fb8ca7cb2e0!8m2!3d37.4998465!4d-122.1583518!16s%2Fg%2F11xm4y6qgk" target="_blank" rel="noopener">Google Business</a>
          </div>
        </div>

      </div><!-- /footer-grid -->

      <div class="footer-bar">
        <p class="footer-bar-copy">© ${SITE.year} FlossByte | Dental IT Support | Peninsula, East Bay & South Bay, CA. All Rights Reserved.</p>
        <div class="footer-bar-links">
          <a href="${r('blog/index.html')}">Blog</a>
          <a href="${r('hipaa-compliance.html')}">HIPAA</a>
          <a href="${r('contact.html')}">Contact</a>
        </div>
      </div>
    </div>
  `;
  document.body.appendChild(footer);
}

/* ── Scroll Animations ─────────────────────────────────────── */
function initScrollAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));
}

/* ── Accordion ─────────────────────────────────────────────── */
function initAccordions() {
  document.querySelectorAll('.accordion-trigger').forEach(trigger => {
    trigger.addEventListener('click', () => {
      const item = trigger.closest('.accordion-item');
      const isOpen = item.classList.contains('open');
      // Close all
      document.querySelectorAll('.accordion-item.open').forEach(i => i.classList.remove('open'));
      // Open clicked if it was closed
      if (!isOpen) item.classList.add('open');
    });
  });
}

/* ── Exit-Intent Popup ──────────────────────────────────────── */
function initExitIntent() {
  const r = rootPath;
  let shown = false;

  // Build popup
  const overlay = document.createElement('div');
  overlay.id = 'exit-popup-overlay';
  overlay.innerHTML = `
    <div id="exit-popup">
      <button id="exit-popup-close" aria-label="Close popup">&times;</button>
      <div style="text-align:center">
        <div style="display:inline-block;background:rgba(239,68,68,0.1);color:#dc2626;font-size:0.75rem;font-weight:700;padding:4px 12px;border-radius:20px;margin-bottom:12px;letter-spacing:0.02em">Only 3 spots left for ${new Date().toLocaleString('en-US',{month:'long'})}</div>
        <h2 style="font-family:var(--font-heading);font-size:1.4rem;font-weight:800;color:var(--color-navy);margin-bottom:4px">Get Your Free IT Assessment</h2>
        <p style="color:var(--color-text-muted);font-size:0.875rem;margin-bottom:20px">Find out if your dental practice is HIPAA-compliant in 30 minutes. No commitment.</p>
        <form id="exit-popup-form" style="text-align:left">
          <input type="text" name="name" placeholder="Your Name" required
            style="width:100%;padding:12px 14px;border:1.5px solid #e0e0e0;border-radius:8px;font-size:0.95rem;margin-bottom:10px;outline:none;transition:border-color 0.2s;font-family:inherit;box-sizing:border-box" />
          <input type="tel" name="phone" placeholder="Phone Number" required
            style="width:100%;padding:12px 14px;border:1.5px solid #e0e0e0;border-radius:8px;font-size:0.95rem;margin-bottom:10px;outline:none;transition:border-color 0.2s;font-family:inherit;box-sizing:border-box" />
          <input type="email" name="email" placeholder="Email (optional)"
            style="width:100%;padding:12px 14px;border:1.5px solid #e0e0e0;border-radius:8px;font-size:0.95rem;margin-bottom:16px;outline:none;transition:border-color 0.2s;font-family:inherit;box-sizing:border-box" />
          <button type="submit"
            style="width:100%;padding:14px;background:var(--color-teal);color:#fff;font-weight:700;border:none;border-radius:8px;font-size:1rem;cursor:pointer;transition:background 0.2s;font-family:inherit">
            Book My Free Assessment
          </button>
        </form>
        <div id="exit-popup-success" style="display:none;padding:20px 0">
          <div style="font-size:2rem;margin-bottom:8px">&#10003;</div>
          <p style="font-weight:700;color:var(--color-navy);font-size:1.1rem;margin-bottom:4px">We'll be in touch shortly!</p>
          <p style="color:var(--color-text-muted);font-size:0.875rem">Expect a call within 1 business day.</p>
        </div>
        <div style="margin-top:14px;display:flex;flex-direction:column;align-items:center;gap:6px">
          <div style="display:flex;align-items:center;gap:6px">
            <svg viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="width:14px;height:14px;flex-shrink:0"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span style="font-size:0.75rem;color:var(--color-text-muted)">10+ years of dental IT expertise</span>
          </div>
          <div style="display:flex;align-items:center;gap:6px">
            <svg viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="width:14px;height:14px;flex-shrink:0"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span style="font-size:0.75rem;color:var(--color-text-muted)">HIPAA-compliant &amp; dental-software certified</span>
          </div>
        </div>
        <p style="margin-top:10px;font-size:0.8125rem;color:var(--color-text-muted)">Prefer to call? <a href="tel:6692372264" style="color:var(--color-teal);font-weight:600">(669) 237-2264</a></p>
      </div>
    </div>
  `;

  // Styles
  const style = document.createElement('style');
  style.textContent = `
    #exit-popup-overlay {
      display:none; position:fixed; inset:0; background:rgba(0,0,0,0.6);
      z-index:10000; align-items:center; justify-content:center;
      backdrop-filter:blur(4px); -webkit-backdrop-filter:blur(4px);
      animation: exitFadeIn 0.3s ease;
    }
    #exit-popup-overlay.active { display:flex; }
    #exit-popup {
      background:#fff; border-radius:16px; padding:36px 28px; max-width:400px;
      width:90%; position:relative; box-shadow:0 24px 48px rgba(0,0,0,0.2);
      animation: exitSlideUp 0.35s ease;
    }
    #exit-popup-close {
      position:absolute; top:12px; right:16px; background:none; border:none;
      font-size:1.75rem; color:#999; cursor:pointer; line-height:1;
      transition:color 0.2s;
    }
    #exit-popup-close:hover { color:#333; }
    #exit-popup form input:focus { border-color: var(--color-teal); }
    #exit-popup form button:hover { background:#009688; }
    @keyframes exitFadeIn { from{opacity:0} to{opacity:1} }
    @keyframes exitSlideUp { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:translateY(0)} }
  `;
  document.head.appendChild(style);
  document.body.appendChild(overlay);

  // Form submission
  overlay.querySelector('#exit-popup-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const form = e.target;
    const btn = form.querySelector('button[type="submit"]');
    btn.textContent = 'Sending...';
    btn.disabled = true;
    try {
      // Send to same Formspree endpoint as contact form (or mailto fallback)
      const data = new FormData(form);
      data.append('_source', 'exit-intent-popup');
      const contactForm = document.querySelector('#contact-form');
      const action = contactForm ? contactForm.action : 'https://formspree.io/f/xdawvyyr';
      await fetch(action, { method: 'POST', body: data, headers: { 'Accept': 'application/json' } });
    } catch (err) { /* still show success — we'll get the data */ }
    form.style.display = 'none';
    overlay.querySelector('#exit-popup-success').style.display = 'block';
  });

  function showPopup() {
    if (shown) return;
    if (sessionStorage.getItem('fb_exit_shown')) return;
    shown = true;
    sessionStorage.setItem('fb_exit_shown', '1');
    overlay.classList.add('active');
  }

  function closePopup() {
    overlay.classList.remove('active');
  }

  // Close handlers
  overlay.querySelector('#exit-popup-close').addEventListener('click', closePopup);
  overlay.addEventListener('click', (e) => { if (e.target === overlay) closePopup(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closePopup(); });

  // Desktop: mouse leaves viewport toward top
  document.addEventListener('mouseout', (e) => {
    if (e.clientY <= 0 && e.relatedTarget === null) showPopup();
  });

  // Idle detection: show popup after 45s of no interaction
  let idleTimer = null;
  function resetIdle() {
    clearTimeout(idleTimer);
    idleTimer = setTimeout(showPopup, 15000);
  }
  ['mousemove', 'scroll', 'click', 'keydown', 'touchstart'].forEach(evt => {
    document.addEventListener(evt, resetIdle, { passive: true });
  });
  resetIdle();

  // Mobile: back button / scroll-up-fast detection (show after 30s + scroll up)
  let lastScrollY = 0;
  let timeOnPage = 0;
  const timer = setInterval(() => { timeOnPage++; if (timeOnPage > 120) clearInterval(timer); }, 1000);
  window.addEventListener('scroll', () => {
    const currentY = window.scrollY;
    if (timeOnPage >= 30 && lastScrollY - currentY > 300) showPopup();
    lastScrollY = currentY;
  });
}

/* ── Sticky Mobile CTA Bar ─────────────────────────────────── */
function renderMobileCTA() {
  const r = rootPath;
  const bar = document.createElement('div');
  bar.className = 'mobile-sticky-cta';
  bar.innerHTML = `
    <a class="sticky-call" href="${SITE.phoneHref}">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2.18h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
      Call Now
    </a>
    <a class="sticky-assess" href="${r('contact.html')}">Free Assessment</a>
  `;
  document.body.appendChild(bar);
}

/* ── Init ───────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  renderNav();
  renderFooter();
  renderMobileCTA();
  initScrollAnimations();
  initAccordions();
  initExitIntent();
});
