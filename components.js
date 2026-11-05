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
  gaId: 'G-37X7JZG0KY',
};

/* ── Google Analytics ──────────────────────────────────────── */
if (SITE.gaId && SITE.gaId !== 'G-XXXXXXXXXX') {
  const gs = document.createElement('script');
  gs.async = true;
  gs.src = 'https://www.googletagmanager.com/gtag/js?id=' + SITE.gaId;
  document.head.appendChild(gs);
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function(){window.dataLayer.push(arguments);};
  window.gtag('js', new Date());
  window.gtag('config', SITE.gaId);
}

function trackConversion(eventName, params = {}) {
  if (typeof window.gtag !== 'function') return;
  window.gtag('event', eventName, {
    page_path: window.location.pathname,
    page_title: document.title,
    ...params,
  });
}

function setupConversionTracking() {
  document.addEventListener('click', (e) => {
    const target = e.target.closest('a, button');
    if (!target) return;

    const href = target.getAttribute('href') || '';
    const text = target.textContent.trim().replace(/\s+/g, ' ').slice(0, 100);

    if (href.startsWith('tel:')) {
      trackConversion('phone_click', { link_url: href, link_text: text });
      return;
    }

    if (href.startsWith('mailto:')) {
      trackConversion('email_click', { link_url: href, link_text: text });
      return;
    }

    if (href.includes('bookings.cloud.microsoft') || target.id === 'book-toggle') {
      trackConversion('booking_click', { link_url: href || 'embedded_booking_toggle', link_text: text });
    }
  });

  document.addEventListener('submit', (e) => {
    const form = e.target;
    if (!(form instanceof HTMLFormElement)) return;

    if (form.id === 'contact-form') {
      trackConversion('contact_form_submit', { form_id: form.id, form_source: 'contact_page' });
      return;
    }

    if (form.id === 'lead-magnet-form' || form.id === 'exit-popup-form' || form.classList.contains('checklist-form')) {
      const source = form.querySelector('[name="_source"]')?.value || form.id || 'checklist_form';
      trackConversion('checklist_download', { form_id: form.id || 'checklist-form', form_source: source });
    }
  }, true);
}

/* ── Helper: resolve relative paths ─────────────────────── */
function rootPath(path) {
  // Keep root-relative URLs in production, but make file:// previews work locally.
  if (window.location.protocol !== 'file:') return '/' + path;

  const normalized = window.location.pathname.replace(/\\/g, '/');
  const marker = '/website/';
  const markerIndex = normalized.toLowerCase().lastIndexOf(marker);
  const localPath = markerIndex >= 0
    ? normalized.slice(markerIndex + marker.length)
    : normalized.replace(/^\/+/, '');
  const parts = localPath.split('/').filter(Boolean);
  const depth = localPath.endsWith('/') ? parts.length : Math.max(0, parts.length - 1);

  return '../'.repeat(depth) + path;
}

/* ── Navigation HTML ─────────────────────────────────────── */
function renderNav() {
  const r = rootPath;
  const nav = document.createElement('nav');
  nav.className = 'site-nav';
  nav.setAttribute('aria-label', 'Main navigation');
  nav.innerHTML = `
    <div class="nav-inner">
      <a class="nav-logo" href="${r('')}" aria-label="FlossByte Home"
         style="display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none;">
        <img src="${r('assets/logo-icon.png')}" alt="" width="38" height="49" aria-hidden="true" loading="eager" style="flex-shrink:0;object-fit:contain;" />
        <span style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:0.85rem;
                     letter-spacing:-0.03em;line-height:1;color:#ffffff;">
          Floss<span style="color:#00BFA5;">Byte</span>
        </span>
      </a>

      <div class="nav-links" id="nav-links">
        <a href="${r('')}" id="nav-home">Home</a>
        <div class="nav-dropdown">
          <a href="${r('services')}" id="nav-services" class="nav-dropdown-toggle">Services
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </a>
          <div class="nav-dropdown-menu">
            <a href="${r('services/dental-vcio')}">Technology Strategy &amp; vCIO</a>
            <a href="${r('services/ai-dental-technology')}">AI Integration</a>
            <a href="${r('services/managed-it-support')}">Managed IT Support</a>
            <a href="${r('services/dental-cybersecurity')}">Cybersecurity</a>
            <a href="${r('services/dental-data-backup')}">Backup &amp; Recovery</a>
            <a href="${r('services/dental-network-infrastructure')}">Network &amp; Infrastructure</a>
            <a href="${r('services/dental-voip-phone-systems')}">VoIP &amp; Phone Systems</a>
            <a href="${r('services/dental-hardware-management')}">Hardware Management</a>
            <a href="${r('services/dentrix-support')}">Dentrix Support</a>
            <a href="${r('services/eaglesoft-support')}">Eaglesoft Support</a>
            <a href="${r('services/open-dental-support')}">Open Dental Support</a>
            <a href="${r('services/dso-multi-location')}">DSO &amp; Multi-Location</a>
            <a href="${r('services')}">All Services →</a>
          </div>
        </div>
        <a href="${r('pricing')}" id="nav-pricing">Pricing</a>
        <a href="${r('about')}" id="nav-about">About</a>
        <a href="${r('why-flossbyte')}" id="nav-why">Why FlossByte</a>
        <div class="nav-dropdown">
          <span class="nav-dropdown-toggle">Resources
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </span>
          <div class="nav-dropdown-menu">
            <a href="${r('blog/')}">Blog</a>
            <a href="${r('hipaa-compliance')}">HIPAA Compliance</a>
            <a href="${r('faqs')}">FAQs</a>
          </div>
        </div>
        <a href="${r('contact')}" id="nav-contact">Contact</a>
      </div>

      <div class="nav-cta">
        <a class="nav-phone" href="${SITE.phoneHref}">${SITE.phone}</a>
        <a class="btn btn-outline btn-sm" href="https://portal.flossbyte.com">Client Login</a>
        <a class="btn btn-primary btn-sm" href="${r('contact')}">Free Assessment</a>
      </div>

      <button class="nav-mobile-toggle" id="mobile-toggle" aria-label="Toggle mobile menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>

    <!-- Mobile Navigation -->
    <div class="nav-mobile" id="nav-mobile" role="navigation" aria-label="Mobile navigation">
      <a href="${r('')}">Home</a>
      <a href="${r('services')}">All Services</a>
      <a href="${r('services/dental-vcio')}" style="padding-left:24px;font-size:0.875rem">Technology Strategy &amp; vCIO</a>
      <a href="${r('services/ai-dental-technology')}" style="padding-left:24px;font-size:0.875rem">AI Integration</a>
      <a href="${r('services/managed-it-support')}" style="padding-left:24px;font-size:0.875rem">Managed IT Support</a>
      <a href="${r('services/dental-cybersecurity')}" style="padding-left:24px;font-size:0.875rem">Cybersecurity</a>
      <a href="${r('services/dental-network-infrastructure')}" style="padding-left:24px;font-size:0.875rem">Network &amp; Infrastructure</a>
      <a href="${r('services/dental-voip-phone-systems')}" style="padding-left:24px;font-size:0.875rem">VoIP &amp; Phone Systems</a>
      <a href="${r('services/dental-hardware-management')}" style="padding-left:24px;font-size:0.875rem">Hardware Management</a>
      <a href="${r('services/dso-multi-location')}" style="padding-left:24px;font-size:0.875rem">DSO &amp; Multi-Location</a>
      <a href="${r('pricing')}">Pricing</a>
      <a href="${r('about')}">About</a>
      <a href="${r('why-flossbyte')}">Why FlossByte</a>
      <div class="mobile-divider"></div>
      <a href="${r('blog/')}">Blog</a>
      <a href="${r('hipaa-compliance')}">HIPAA Compliance</a>
      <a href="${r('faqs')}">FAQs</a>
      <div class="mobile-divider"></div>
      <a href="${SITE.phoneHref}" style="color: var(--color-teal)">${SITE.phone}</a>
      <a href="https://portal.flossbyte.com">Client Login</a>
      <a class="mobile-cta" href="${r('contact')}">Get Free Technology Assessment</a>
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
    const currentBase = currentPath.split('/').pop().split('#')[0].toLowerCase() || './';
    if (linkBase === currentBase || (linkBase === './' && currentBase === '')) {
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
          <a href="${r('')}" style="display:inline-block;text-decoration:none;margin-bottom:12px;">
            <img src="${r('assets/logo-icon.png')}" alt="FlossByte" width="42" height="54" loading="lazy" style="object-fit:contain;" />
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
            <a href="${r('about')}">About FlossByte</a>
            <a href="${r('why-flossbyte')}">Why FlossByte</a>
            <a href="${r('contact')}">Contact Us</a>
          </div>
        </div>

        <!-- Services -->
        <div>
          <p class="footer-heading">Services</p>
          <div class="footer-links">
            <a href="${r('services')}">All Services</a>
            <a href="${r('services/dental-vcio')}">Technology Strategy &amp; vCIO</a>
            <a href="${r('services/ai-dental-technology')}">AI Integration</a>
            <a href="${r('services/dental-cybersecurity')}">Cybersecurity</a>
            <a href="${r('services/dso-multi-location')}">DSO &amp; Multi-Location</a>
            <a href="${r('hipaa-compliance')}">HIPAA Compliance</a>
            <a href="${r('pricing')}">Pricing</a>
          </div>
        </div>

        <!-- Service Areas -->
        <div>
          <p class="footer-heading">Service Areas</p>
          <div class="footer-links">
            <a href="${r('locations/peninsula')}">Peninsula & SF</a>
            <a href="${r('locations/east-bay')}">East Bay</a>
            <a href="${r('locations/south-bay')}">South Bay</a>
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
          <a href="${r('blog/')}">Blog</a>
          <a href="${r('hipaa-compliance')}">HIPAA</a>
          <a href="${r('contact')}">Contact</a>
          <a href="${r('privacy')}">Privacy Policy</a>
          <a href="${r('terms')}">Terms</a>
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
        <div style="display:inline-block;background:rgba(0,191,165,0.1);color:var(--color-teal);font-size:0.75rem;font-weight:700;padding:4px 12px;border-radius:20px;margin-bottom:12px;letter-spacing:0.02em">FREE DOWNLOAD</div>
        <h2 style="font-family:var(--font-heading);font-size:1.4rem;font-weight:800;color:var(--color-navy);margin-bottom:4px">Before You Go — Grab This Free Checklist</h2>
        <p style="color:var(--color-text-muted);font-size:0.875rem;margin-bottom:20px">15 critical HIPAA IT safeguards every dental practice needs. Takes 30 seconds — instant PDF download.</p>
        <form id="exit-popup-form" style="text-align:left">
          <input type="hidden" name="_source" value="exit-intent-checklist" />
          <input type="text" name="name" placeholder="Your Name" required
            style="width:100%;padding:12px 14px;border:1.5px solid #e0e0e0;border-radius:8px;font-size:0.95rem;margin-bottom:10px;outline:none;transition:border-color 0.2s;font-family:inherit;box-sizing:border-box" />
          <input type="email" name="email" placeholder="Work Email" required
            style="width:100%;padding:12px 14px;border:1.5px solid #e0e0e0;border-radius:8px;font-size:0.95rem;margin-bottom:16px;outline:none;transition:border-color 0.2s;font-family:inherit;box-sizing:border-box" />
          <button type="submit"
            style="width:100%;padding:14px;background:var(--color-teal);color:#fff;font-weight:700;border:none;border-radius:8px;font-size:1rem;cursor:pointer;transition:background 0.2s;font-family:inherit">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="width:16px;height:16px;vertical-align:middle;margin-right:6px"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            Download Free Checklist
          </button>
        </form>
        <div style="margin-top:14px;display:flex;flex-direction:column;align-items:center;gap:6px">
          <div style="display:flex;align-items:center;gap:6px">
            <svg viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="width:14px;height:14px;flex-shrink:0"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span style="font-size:0.75rem;color:var(--color-text-muted)">Used by dental practices across the Bay Area</span>
          </div>
          <div style="display:flex;align-items:center;gap:6px">
            <svg viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="width:14px;height:14px;flex-shrink:0"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span style="font-size:0.75rem;color:var(--color-text-muted)">Covers encryption, backups, access controls &amp; more</span>
          </div>
        </div>
        <p style="margin-top:10px;font-size:0.8125rem;color:var(--color-text-muted)">Want a full assessment instead? <a href="${r('contact')}" style="color:var(--color-teal);font-weight:600">Book free IT assessment</a></p>
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
    // Redirect to thank-you/download page
    window.location.href = '/thank-you';
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
    idleTimer = setTimeout(showPopup, 45000);
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
    <a class="sticky-assess" href="${r('contact')}">Free Assessment</a>
  `;
  document.body.appendChild(bar);
}

/* ── Blog: Email Signup CTA ────────────────────────────────── */
function createSignupCTA(source) {
  const div = document.createElement('div');
  div.style.cssText = 'max-width:800px;margin:32px auto;padding:0 24px';
  div.innerHTML = `
    <div style="background:linear-gradient(135deg,var(--color-navy),#1a2744);border:1.5px solid rgba(0,191,165,0.2);border-radius:16px;padding:36px 32px;text-align:center">
      <div style="display:inline-block;background:rgba(0,191,165,0.1);color:var(--color-teal);font-size:0.75rem;font-weight:700;padding:4px 14px;border-radius:20px;margin-bottom:14px;letter-spacing:0.03em">FREE RESOURCE</div>
      <h3 style="font-family:var(--font-heading);font-size:1.3rem;font-weight:800;color:#fff;margin-bottom:8px">Get the HIPAA IT Compliance Checklist</h3>
      <p style="color:rgba(255,255,255,0.6);font-size:0.9rem;margin-bottom:20px;max-width:480px;margin-left:auto;margin-right:auto">15 critical technical safeguards every dental practice needs. Free PDF — instant download.</p>
      <form class="checklist-form" style="display:flex;gap:10px;max-width:440px;margin:0 auto;flex-wrap:wrap;justify-content:center">
        <input type="hidden" name="_subject" value="HIPAA Checklist — Blog Signup" />
        <input type="hidden" name="_source" value="${source}" />
        <input type="email" name="email" placeholder="Your work email" required
          style="flex:1;min-width:200px;padding:12px 16px;border:1.5px solid rgba(255,255,255,0.15);background:rgba(255,255,255,0.05);border-radius:8px;font-size:0.95rem;color:#fff;outline:none;font-family:inherit;box-sizing:border-box" />
        <button type="submit"
          style="padding:12px 24px;background:var(--color-teal);color:#fff;font-weight:700;border:none;border-radius:8px;font-size:0.9rem;cursor:pointer;transition:background 0.2s;font-family:inherit;white-space:nowrap">
          Download Free
        </button>
      </form>
      <p style="font-size:0.7rem;color:rgba(255,255,255,0.3);margin-top:12px">No spam. Unsubscribe anytime.</p>
    </div>
  `;
  return div;
}

function injectBlogEmailSignup() {
  const path = window.location.pathname;
  if (!path.includes('/blog/') || path.endsWith('/blog/') || path.endsWith('/blog/')) return;

  const main = document.querySelector('main');
  if (!main) return;

  // Find the article content container
  const content = main.querySelector('.blog-post-content');
  if (!content) return;
  const articleSection = content.closest('section');
  if (!articleSection) return;

  // INLINE: inject after the 3rd paragraph within the article
  const paragraphs = content.querySelectorAll(':scope > p');
  if (paragraphs.length >= 3) {
    const inlineCTA = createSignupCTA('blog-inline-signup');
    inlineCTA.style.cssText = 'margin:32px 0;padding:0';
    paragraphs[2].after(inlineCTA);
  }

  // BOTTOM: inject after the article section (keep as a second touchpoint)
  const bottomCTA = createSignupCTA('blog-bottom-signup');
  bottomCTA.style.cssText = 'max-width:800px;margin:0 auto;padding:0 24px 48px';
  articleSection.after(bottomCTA);
}

/* ── Checklist Form Handler (JS redirect since Formspree free plan doesn't support _next) ── */
document.addEventListener('submit', async (e) => {
  const form = e.target;
  if (!form.classList.contains('checklist-form') && form.id !== 'lead-magnet-form') return;
  e.preventDefault();
  const btn = form.querySelector('button[type="submit"]');
  const origText = btn.textContent;
  btn.textContent = 'Sending...';
  btn.disabled = true;
  try {
    await fetch('https://formspree.io/f/xdawvyyr', {
      method: 'POST',
      body: new FormData(form),
      headers: { 'Accept': 'application/json' }
    });
  } catch (err) { /* redirect anyway */ }
  window.location.href = '/thank-you';
});

/* ── Blog: Service Area Links ──────────────────────────────── */
function injectBlogServiceAreas() {
  // Only on blog post pages (not the blog index)
  const path = window.location.pathname;
  if (!path.includes('/blog/') || path.endsWith('/blog/') || path.endsWith('/blog/')) return;

  const r = rootPath;
  const main = document.querySelector('main');
  if (!main) return;

  const section = document.createElement('section');
  section.style.cssText = 'padding:0 0 48px';
  section.innerHTML = `
    <div class="container" style="max-width:800px">
      <h2 style="font-family:var(--font-heading);font-size:1.5rem;font-weight:700;color:var(--color-navy);margin-bottom:16px">Dental IT Support Across the Bay Area</h2>
      <p style="color:var(--color-text-muted);font-size:0.95rem;margin-bottom:20px">FlossByte serves dental practices throughout the Bay Area. Find IT support near you:</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a href="${r('locations/peninsula')}" style="display:inline-flex;align-items:center;gap:8px;padding:10px 18px;background:var(--color-gray-50);border-radius:8px;text-decoration:none;font-weight:600;font-size:0.9rem;color:var(--color-navy);transition:background 0.2s" onmouseover="this.style.background='#e8f5f3'" onmouseout="this.style.background='var(--color-gray-50)'">
          <svg viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:16px;height:16px"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
          Peninsula & SF
        </a>
        <a href="${r('locations/east-bay')}" style="display:inline-flex;align-items:center;gap:8px;padding:10px 18px;background:var(--color-gray-50);border-radius:8px;text-decoration:none;font-weight:600;font-size:0.9rem;color:var(--color-navy);transition:background 0.2s" onmouseover="this.style.background='#e8f5f3'" onmouseout="this.style.background='var(--color-gray-50)'">
          <svg viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:16px;height:16px"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
          East Bay
        </a>
        <a href="${r('locations/south-bay')}" style="display:inline-flex;align-items:center;gap:8px;padding:10px 18px;background:var(--color-gray-50);border-radius:8px;text-decoration:none;font-weight:600;font-size:0.9rem;color:var(--color-navy);transition:background 0.2s" onmouseover="this.style.background='#e8f5f3'" onmouseout="this.style.background='var(--color-gray-50)'">
          <svg viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:16px;height:16px"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
          South Bay
        </a>
      </div>
      <div style="margin-top:16px;display:flex;gap:12px;flex-wrap:wrap;font-size:0.85rem">
        <a href="${r('services')}" style="color:var(--color-teal);text-decoration:none;font-weight:600">View All Services →</a>
        <a href="${r('pricing')}" style="color:var(--color-teal);text-decoration:none;font-weight:600">See Pricing →</a>
      </div>
    </div>
  `;

  // Insert before the last section (author/CTA) in main
  const lastSection = main.querySelector('section.section-light:last-of-type');
  if (lastSection) {
    main.insertBefore(section, lastSection);
  } else {
    main.appendChild(section);
  }
}

/* ── Related content (blog posts): contextual internal links ── */
function injectRelatedContent() {
  // Only on blog post pages (not the blog index)
  const path = window.location.pathname;
  if (!path.includes('/blog/') || path.endsWith('/blog/') || path.endsWith('/blog/')) return;
  const main = document.querySelector('main');
  if (!main) return;

  const r = rootPath;
  const slug = path.toLowerCase();

  // [keywords] -> related services, related posts, related city pages
  const MAP = [
    { k: ['dentrix'], services: [
        ['services/dentrix-support', 'Dentrix IT Support'],
        ['services/dental-network-infrastructure', 'Dental Network & Server Infrastructure'],
        ['services/managed-it-support', 'Managed IT Support for Dental Practices'] ],
      posts: [
        ['blog/dentrix-it-support-guide', 'Dentrix IT Support: The Complete Guide'],
        ['blog/dentrix-running-slow', 'Dentrix Running Slow? How to Fix It'],
        ['blog/dentrix-vs-eaglesoft-vs-open-dental', 'Dentrix vs Eaglesoft vs Open Dental'] ],
      cities: [] },
    { k: ['eaglesoft', 'open-dental'], services: [
        ['services/eaglesoft-support', 'Eaglesoft IT Support'],
        ['services/open-dental-support', 'Open Dental IT Support'],
        ['services/dentrix-support', 'Dentrix IT Support'] ],
      posts: [
        ['blog/dentrix-vs-eaglesoft-vs-open-dental', 'Dentrix vs Eaglesoft vs Open Dental'] ],
      cities: [] },
    { k: ['hipaa'], services: [
        ['hipaa-compliance', 'HIPAA Compliance for Dental Practices'],
        ['services/dental-cybersecurity', 'Dental Cybersecurity'],
        ['services/managed-it-support', 'Managed IT Support for Dental Practices'] ],
      posts: [
        ['blog/done-for-you-hipaa-compliance-setup-dental', 'Done-for-You HIPAA Compliance Setup'],
        ['blog/hipaa-compliance-for-dental-practices', 'HIPAA Compliance for Dental Practices'],
        ['blog/hipaa-it-requirements-dental-offices', 'HIPAA IT Requirements for Dental Offices'] ],
      cities: [] },
    { k: ['backup', 'recovery'], services: [
        ['services/dental-data-backup', 'Dental Data Backup & Disaster Recovery'],
        ['services/managed-it-support', 'Managed IT Support for Dental Practices'] ],
      posts: [
        ['blog/dental-data-backup-recovery-guide', 'Dental Data Backup & Recovery Guide'],
        ['blog/dental-data-backup-cost-risks', 'Dental Data Backup: Costs & Risks'] ],
      cities: [] },
    { k: ['ransomware', 'cybersecurity', 'antivirus', 'firewall'], services: [
        ['services/dental-cybersecurity', 'Dental Cybersecurity & HIPAA Security'],
        ['services/dental-data-backup', 'Dental Data Backup & Disaster Recovery'] ],
      posts: [
        ['blog/dental-office-ransomware-prevention', 'Dental Office Ransomware Prevention'],
        ['blog/dental-cybersecurity-antivirus', 'Antivirus & Cybersecurity for Dental Offices'] ],
      cities: [] },
    { k: ['voip', 'phone'], services: [
        ['services/dental-voip-phone-systems', 'Dental VoIP Phone Systems'],
        ['services/managed-it-support', 'Managed IT Support for Dental Practices'] ],
      posts: [],
      cities: [] },
    { k: ['network', 'server', 'wifi', 'wi-fi', 'cabling'], services: [
        ['services/dental-network-infrastructure', 'Dental Network & Infrastructure'],
        ['services/dental-office-network-setup', 'Dental Office Network Setup'],
        ['services/managed-it-support', 'Managed IT Support for Dental Practices'] ],
      posts: [
        ['blog/dental-office-server-issues', 'Dental Office Server Issues: Diagnosis Guide'],
        ['blog/dental-it-support-common-issues', 'Common Dental IT Issues & Fixes'] ],
      cities: [] },
    { k: ['vcio', 'roadmap', 'strategy'], services: [
        ['services/dental-vcio', 'Dental vCIO & Technology Strategy'],
        ['services/managed-it-support', 'Managed IT Support for Dental Practices'] ],
      posts: [
        ['blog/what-is-dental-vcio', 'What Is a Dental vCIO?'],
        ['blog/dental-practice-technology-roadmap', 'Dental Practice Technology Roadmap'] ],
      cities: [] },
    { k: ['cost', 'pricing', 'price'], services: [
        ['pricing', 'Dental IT Pricing Plans'],
        ['services/managed-it-support', 'Managed IT Support for Dental Practices'] ],
      posts: [
        ['blog/dental-it-support-cost-2026', 'How Much Does Dental IT Support Cost?'] ],
      cities: [] },
    { k: ['ai-'], services: [
        ['services/ai-dental-technology', 'AI Integration for Dental Practices'],
        ['services/dental-vcio', 'Dental vCIO & Technology Strategy'] ],
      posts: [
        ['blog/ai-transforming-dental-practices-2026', 'How AI Is Transforming Dental Practices'] ],
      cities: [] },
    { k: ['new-dental-practice', 'startup', 'opening'], services: [
        ['services/dental-office-network-setup', 'New Dental Office IT Setup'],
        ['services/managed-it-support', 'Managed IT Support for Dental Practices'] ],
      posts: [
        ['blog/new-dental-practice-it-setup-checklist', 'New Dental Practice IT Setup Checklist'] ],
      cities: [
        ['locations/south-bay/san-jose', 'Dental IT Support in San Jose'],
        ['locations/peninsula/san-francisco', 'Dental IT Support in San Francisco'] ] },
    { k: ['dso', 'multi-location', 'group-practice'], services: [
        ['services/dso-multi-location', 'DSO & Multi-Location Dental IT'],
        ['services/dental-vcio', 'Dental vCIO & Technology Strategy'] ],
      posts: [],
      cities: [] },
    { k: ['imaging', 'dexis', 'x-ray', 'cbct'], services: [
        ['services/dental-imaging-it-support', 'Dental Imaging IT Support'],
        ['services/dental-network-infrastructure', 'Dental Network & Infrastructure'] ],
      posts: [],
      cities: [] },
    { k: ['outage', 'downtime', 'emergency'], services: [
        ['services/managed-it-support', 'Managed IT Support for Dental Practices'],
        ['services/dental-network-infrastructure', 'Dental Network & Infrastructure'] ],
      posts: [
        ['blog/dental-it-support-bay-area-outage', 'Dental IT Outage: Emergency Response'],
        ['blog/dental-downtime-revenue-loss', 'What Dental Downtime Really Costs'] ],
      cities: [] },
    { k: ['switching', 'best-dental-it', 'why-general-it-fails', 'need-specialized'], services: [
        ['services/managed-it-support', 'Managed IT Support for Dental Practices'],
        ['why-flossbyte', 'Why Dental Practices Choose FlossByte'] ],
      posts: [
        ['blog/best-dental-it-companies-bay-area', 'Best Dental IT Companies in the Bay Area'],
        ['blog/switching-dental-it-provider', 'Switching Your Dental IT Provider'] ],
      cities: [] }
  ];

  const seen = new Set();
  const base = (h) => h.toLowerCase().split('/').pop().replace(/\.html$/, '');
  seen.add(base(slug)); // never link a page to itself
  const services = [];
  const posts = [];
  const cities = [];
  const pushUnique = (arr, href, label, cap) => {
    const key = base(href);
    if (arr.length >= cap || seen.has(key)) return;
    seen.add(key);
    arr.push([href, label]);
  };

  MAP.forEach(entry => {
    if (!entry.k.some(k => slug.includes(k))) return;
    entry.services.forEach(([href, label]) => pushUnique(services, href, label, 3));
    entry.posts.forEach(([href, label]) => pushUnique(posts, href, label, 3));
    entry.cities.forEach(([href, label]) => pushUnique(cities, href, label, 2));
  });

  // Fallback: every post gets at least the core conversion links
  if (!services.length) {
    pushUnique(services, 'services/managed-it-support', 'Managed IT Support for Dental Practices', 3);
    pushUnique(services, 'services/dental-cybersecurity', 'Dental Cybersecurity & HIPAA Security', 3);
  }

  const linkList = (items) => items.map(([href, label]) =>
    `<li style="margin-bottom:8px"><a href="${r(href)}" style="color:var(--color-teal);font-weight:600;text-decoration:none">${label} →</a></li>`
  ).join('');

  let html = `<div class="container" style="max-width:800px">
    <h2 style="font-family:var(--font-heading);font-size:1.5rem;font-weight:700;color:var(--color-navy);margin-bottom:16px">Related Reading</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px">`;
  if (services.length) {
    html += `<div><p style="font-weight:700;color:var(--color-navy);margin-bottom:10px;font-size:0.95rem">Our Services</p><ul style="list-style:none;padding:0;margin:0;font-size:0.95rem">${linkList(services)}</ul></div>`;
  }
  if (posts.length || cities.length) {
    html += `<div><p style="font-weight:700;color:var(--color-navy);margin-bottom:10px;font-size:0.95rem">More Guides</p><ul style="list-style:none;padding:0;margin:0;font-size:0.95rem">${linkList(posts.concat(cities))}</ul></div>`;
  }
  html += `</div></div>`;

  const section = document.createElement('section');
  section.style.cssText = 'padding:0 0 40px';
  section.setAttribute('aria-label', 'Related reading');
  section.innerHTML = html;

  // Insert before the service-areas block if present, else before last light section
  const svcAreas = Array.from(main.querySelectorAll('section')).find(s => s.textContent.includes('Dental IT Support Across the Bay Area'));
  if (svcAreas) {
    main.insertBefore(section, svcAreas);
  } else {
    const lastSection = main.querySelector('section.section-light:last-of-type');
    if (lastSection) main.insertBefore(section, lastSection);
    else main.appendChild(section);
  }
}

/* ── City pages: service link grid (local SEO) ───────────────── */
function injectCityServices() {
  // Only on individual city pages: /locations/<region>/<city>
  const path = window.location.pathname.replace(/\.html$/, '').replace(/\/$/, '');
  const m = path.match(/\/locations\/([^/]+)\/([^/]+)$/);
  if (!m) return;
  const main = document.querySelector('main');
  if (!main) return;

  const r = rootPath;
  const city = m[2].split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');

  const services = [
    ['services/managed-it-support', 'Managed IT Support', 'Help desk, monitoring & proactive maintenance'],
    ['hipaa-compliance', 'HIPAA Compliance', 'Risk assessments, hardening & audit readiness'],
    ['services/dental-cybersecurity', 'Cybersecurity', 'Threat monitoring & ransomware protection'],
    ['services/dentrix-support', 'Dentrix, Eaglesoft & Open Dental', 'Practice management software experts'],
    ['services/dental-data-backup', 'Backup & Recovery', 'Encrypted backups & disaster recovery'],
    ['services/dental-network-infrastructure', 'Network & Wi-Fi', 'Infrastructure for imaging & X-ray systems'],
    ['services/dental-voip-phone-systems', 'VoIP Phone Systems', 'Modern phones with scheduling integrations'],
    ['services/dental-vcio', 'vCIO & Strategy', 'Technology roadmapping & IT budgeting']
  ];

  const cards = services.map(([href, label, desc]) => `
    <a href="${r(href)}" style="display:block;padding:18px;background:var(--color-gray-50);border-radius:12px;text-decoration:none;transition:background 0.2s" onmouseover="this.style.background='#e8f5f3'" onmouseout="this.style.background='var(--color-gray-50)'">
      <p style="font-weight:700;color:var(--color-navy);margin:0 0 6px;font-size:1rem">${label} in ${city}</p>
      <p style="color:var(--color-text-muted);margin:0;font-size:0.88rem">${desc}</p>
    </a>`).join('');

  const section = document.createElement('section');
  section.style.cssText = 'padding:24px 0 48px';
  section.setAttribute('aria-label', 'Services in ' + city);
  section.innerHTML = `
    <div class="container" style="max-width:1000px">
      <h2 style="font-family:var(--font-heading);font-size:1.6rem;font-weight:700;color:var(--color-navy);margin-bottom:8px">Dental IT Services in ${city}</h2>
      <p style="color:var(--color-text-muted);font-size:0.95rem;margin-bottom:24px">Every service below is delivered by our Bay Area dental technology team — HIPAA-compliant from day one.</p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px">${cards}</div>
    </div>`;

  const lastSection = main.querySelector('section.section-light:last-of-type');
  if (lastSection) main.insertBefore(section, lastSection);
  else main.appendChild(section);
}

/* ── BreadcrumbList Schema ──────────────────────────────────── */
function injectBreadcrumbSchema() {
  // Match breadcrumb nav by class or by aria-label, or by content pattern (Home › ...)
  const breadcrumbNav = document.querySelector('.page-hero-breadcrumb')
    || document.querySelector('nav[aria-label="Breadcrumb"]')
    || Array.from(document.querySelectorAll('nav')).find(n => {
         const text = n.textContent;
         return text.includes('›') && text.includes('Home') && !n.classList.contains('site-nav');
       });
  if (!breadcrumbNav) return;

  const items = [];
  const children = breadcrumbNav.childNodes;
  let position = 0;

  for (const node of children) {
    if (node.nodeType === Node.TEXT_NODE) continue;
    if (node.tagName === 'SPAN' && node.textContent.trim() === '›') continue;

    position++;
    if (node.tagName === 'A') {
      items.push({
        '@type': 'ListItem',
        'position': position,
        'name': node.textContent.trim(),
        'item': new URL(node.getAttribute('href'), window.location.href).href
      });
    } else if (node.tagName === 'SPAN') {
      items.push({
        '@type': 'ListItem',
        'position': position,
        'name': node.textContent.trim()
      });
    }
  }

  if (items.length < 2) return;

  const script = document.createElement('script');
  script.type = 'application/ld+json';
  script.textContent = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    'itemListElement': items
  });
  document.head.appendChild(script);
}

/* ── Init ───────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  setupConversionTracking();
  renderNav();
  renderFooter();
  renderMobileCTA();
  initScrollAnimations();
  initAccordions();
  initExitIntent();
  injectBreadcrumbSchema();
  injectBlogEmailSignup();
  injectBlogServiceAreas();
  injectRelatedContent();
  injectCityServices();
});
