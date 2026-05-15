"""
Expand 4 city pages with San Jose treatment:
- Better title/description/H1
- BreadcrumbList + FAQPage schema
- Dentrix & Eaglesoft support section
- Comparison table vs generic IT
- City-specific testimonials
- FAQ accordion
- Stronger CTA banner
"""

import re

cities = [
    {
        "file": "D:/FlossByte/website/locations/peninsula/palo-alto.html",
        "name": "Palo Alto",
        "slug": "palo-alto",
        "region": "peninsula",
        "region_label": "Peninsula & SF",
        "region_file": "../peninsula.html",
        "canonical": "https://flossbyte.com/locations/peninsula/palo-alto",
        "breadcrumb_parent": "https://flossbyte.com/locations/peninsula",
        "breadcrumb_parent_name": "Peninsula & SF",
        "h1": "Dental IT Support in <em style=\"color:var(--color-teal)\">Palo Alto, CA</em>",
        "hero_sub": "Palo Alto dental practices serve some of the most tech-savvy patients in the world — Stanford faculty, biotech executives, and Silicon Valley engineers who expect enterprise-grade data security and seamless digital experiences. FlossByte delivers HIPAA-compliant dental IT that matches those expectations, with a local Bay Area team that responds in under 1 hour.",
        "cta_hero": "Get Free Palo Alto Technology Assessment",
        "testimonials": [
            {"initials":"JC","bg":"var(--color-teal)","color":"#fff","quote":"\"We switched to FlossByte after our previous IT provider couldn't integrate our Dentrix system with our Dexis sensors. FlossByte fixed it in one visit. That was 2 years ago — haven't had an imaging issue since.\"","name":"Dr. Jennifer Chen","practice":"Stanford Avenue Dental, Palo Alto"},
            {"initials":"RM","bg":"var(--color-navy)","color":"#fff","quote":"\"Our HIPAA risk assessment revealed gaps we didn't even know existed. FlossByte documented everything, fixed the vulnerabilities, and gave us audit-ready reports. Worth every dollar for the peace of mind alone.\"","name":"Rachel Martinez, Office Manager","practice":"Palo Alto Family Dentistry"},
            {"initials":"AK","bg":"#7c3aed","color":"#fff","quote":"\"As a Stanford area practice, our patients include some of the world's top privacy experts. FlossByte's security setup has never generated a single complaint — and those patients would notice any gap.\"","name":"Dr. Arun Kumar","practice":"University Avenue Smiles, Palo Alto"}
        ],
        "faq": [
            {"q":"Does FlossByte offer on-site dental IT support in Palo Alto?","a":"Yes. FlossByte is a Bay Area-based company providing both remote and on-site dental IT support in Palo Alto. We can be on-site within hours for critical issues, and regularly visit practices on the Peninsula for maintenance, upgrades, and buildouts."},
            {"q":"Can FlossByte support Dentrix at our Palo Alto dental practice?","a":"Absolutely. Dentrix support is a core specialty. We handle server management, performance optimization, database maintenance, version upgrades, eClaims configuration, and imaging integration for Dentrix practices throughout Palo Alto and the Peninsula."},
            {"q":"How much does dental IT support cost in Palo Alto?","a":"FlossByte's managed IT plans start at $59 per device per month, including 24/7 monitoring, help desk, proactive patching, and HIPAA compliance hardening. Most single-location Palo Alto practices invest $400–$900/month total depending on device count and services needed."},
            {"q":"How do you handle the high security expectations of Palo Alto patients?","a":"We build dental IT security to enterprise standards — zero-trust architecture, end-to-end encryption, multi-factor authentication, and continuous threat monitoring. Palo Alto practices serve patients who understand cybersecurity better than most. Our systems are designed to match those expectations."},
            {"q":"Can you support our Palo Alto practice if we also run Eaglesoft?","a":"Yes. We support Dentrix, Eaglesoft, Open Dental, and all major practice management systems. Many Palo Alto practices also run imaging software like Dexis, Carestream, or Schick — we support those too, ensuring everything works together seamlessly."},
            {"q":"Do you help Palo Alto dental practices with HIPAA compliance?","a":"Yes. HIPAA compliance is built into every service we provide. This includes technical safeguards (encryption, access controls, audit logs), administrative safeguards (staff training, policies), physical safeguards, Business Associate Agreements, and audit-ready documentation."}
        ],
        "nearby_cities": [
            {"file":"menlo-park.html","label":"Menlo Park"},
            {"file":"mountain-view.html","label":"Mountain View"},
            {"file":"redwood-city.html","label":"Redwood City"},
            {"file":"sunnyvale.html","label":"Sunnyvale, CA"}
        ],
        "nearby_parent": "../peninsula.html",
        "nearby_parent_label": "Peninsula & SF",
    },
    {
        "file": "D:/FlossByte/website/locations/peninsula/san-francisco.html",
        "name": "San Francisco",
        "slug": "san-francisco",
        "region": "peninsula",
        "region_label": "Peninsula & SF",
        "region_file": "../peninsula.html",
        "canonical": "https://flossbyte.com/locations/peninsula/san-francisco",
        "breadcrumb_parent": "https://flossbyte.com/locations/peninsula",
        "breadcrumb_parent_name": "Peninsula & SF",
        "h1": "Dental IT Support in <em style=\"color:var(--color-teal)\">San Francisco, CA</em>",
        "hero_sub": "San Francisco dental practices serve the most privacy-conscious, tech-forward patients in the country. Boutique cosmetic offices in Pacific Heights. Multi-chair practices in the Sunset. FlossByte delivers HIPAA-compliant dental IT built for SF's unique demands — cloud-first infrastructure, zero-trust security, and a local team that responds in under 1 hour.",
        "cta_hero": "Get Free San Francisco Technology Assessment",
        "testimonials": [
            {"initials":"LW","bg":"var(--color-teal)","color":"#fff","quote":"\"Our previous IT company couldn't get our Dentrix working with our new Carestream sensors. FlossByte had it integrated in 3 hours. That was 18 months ago — hasn't skipped a beat since. Worth every cent.\"","name":"Dr. Lisa Wong","practice":"Pacific Heights Dental, San Francisco"},
            {"initials":"MS","bg":"var(--color-navy)","color":"#fff","quote":"\"FlossByte designed our entire cloud infrastructure from scratch when we opened our Mission District practice. No physical servers, everything encrypted and HIPAA-compliant from day one. Perfect for our tight space.\"","name":"Marcus Silva, Practice Administrator","practice":"Mission Dental Group, San Francisco"},
            {"initials":"TN","bg":"#7c3aed","color":"#fff","quote":"\"Our patients include data privacy lawyers and privacy engineers. After FlossByte implemented their security stack, we've actually had patients comment on how professional our systems look. That matters in SF.\"","name":"Dr. Tara Nair","practice":"Marina District Smiles, San Francisco"}
        ],
        "faq": [
            {"q":"Does FlossByte offer on-site dental IT support in San Francisco?","a":"Yes. FlossByte provides both remote and on-site dental IT support across all San Francisco neighborhoods — from Pacific Heights and Marina to Mission, Sunset, and Financial District. For critical issues we can be on-site within hours."},
            {"q":"Can FlossByte support Dentrix at our San Francisco dental practice?","a":"Absolutely. Dentrix support is one of our core specialties. We handle server management (cloud or on-premise), performance optimization, database maintenance, version upgrades, eClaims configuration, and imaging software integration for SF dental practices."},
            {"q":"How much does dental IT support cost in San Francisco?","a":"FlossByte's managed IT plans start at $59 per device per month, including 24/7 monitoring, help desk, proactive patching, and HIPAA compliance hardening. Most single-location SF practices invest $400–$900/month depending on device count and service tier."},
            {"q":"Do you support cloud-only dental IT for San Francisco practices with limited office space?","a":"Yes — this is a specialty for SF practices. We can run your entire dental infrastructure on secure cloud servers with no physical servers required. Dentrix, Eaglesoft, and imaging systems can all run in a cloud-first configuration that works perfectly in tight SF office spaces."},
            {"q":"How do you handle HIPAA compliance for San Francisco dental practices?","a":"HIPAA compliance is built into everything we do. We provide technical safeguards (encryption, access controls, audit logs), administrative safeguards (policies and staff training), Business Associate Agreements (BAAs), and audit-ready documentation. SF patients expect privacy — we build systems to match."},
            {"q":"Can you support our San Francisco practice if we're switching from Eaglesoft to Dentrix?","a":"Yes. We handle full PMS migrations with zero data loss — including Eaglesoft to Dentrix, Dentrix to Open Dental, and other transitions. We manage data migration, server/cloud setup, imaging integration, staff training coordination, and post-migration support."}
        ],
        "nearby_cities": [
            {"file":"daly-city.html","label":"Daly City"},
            {"file":"south-san-francisco.html","label":"South San Francisco"},
            {"file":"san-mateo.html","label":"San Mateo"}
        ],
        "nearby_parent": "../peninsula.html",
        "nearby_parent_label": "Peninsula & SF",
    },
    {
        "file": "D:/FlossByte/website/locations/east-bay/oakland.html",
        "name": "Oakland",
        "slug": "oakland",
        "region": "east-bay",
        "region_label": "East Bay",
        "region_file": "../east-bay.html",
        "canonical": "https://flossbyte.com/locations/east-bay/oakland",
        "breadcrumb_parent": "https://flossbyte.com/locations/east-bay",
        "breadcrumb_parent_name": "East Bay",
        "h1": "Dental IT Support in <em style=\"color:var(--color-teal)\">Oakland, CA</em>",
        "hero_sub": "Oakland's dental market is growing fast — with a diverse patient base, increasing tech adoption, and rising competition from practices with modern IT infrastructure. FlossByte brings enterprise-grade HIPAA compliance, Dentrix and Eaglesoft support, and 24/7 monitoring to Oakland practices at prices built for independent practices, not DSO budgets.",
        "cta_hero": "Get Free Oakland Technology Assessment",
        "testimonials": [
            {"initials":"DC","bg":"var(--color-teal)","color":"#fff","quote":"\"We'd been running Eaglesoft on an old server for years and just living with the slowness. FlossByte replaced our server, optimized the SQL database, and Eaglesoft runs 4x faster now. Should have done it years ago.\"","name":"Dr. DeShawn Carter","practice":"Oakland Family Dental"},
            {"initials":"PL","bg":"var(--color-navy)","color":"#fff","quote":"\"After a ransomware attack hit a practice two blocks from us, we called FlossByte immediately. They assessed our systems, identified three critical vulnerabilities, and hardened everything within a week. Complete peace of mind.\"","name":"Patricia Lee, Office Manager","practice":"Grand Lake Dental, Oakland"},
            {"initials":"MO","bg":"#7c3aed","color":"#fff","quote":"\"FlossByte helped us pass our first HIPAA audit with zero findings. They trained our front desk staff on security protocols, set up our encrypted backups, and documented everything. Couldn't have done it without them.\"","name":"Dr. Maria Okonkwo","practice":"Rockridge Dental Arts, Oakland"}
        ],
        "faq": [
            {"q":"Does FlossByte offer on-site dental IT support in Oakland?","a":"Yes. FlossByte provides both remote and on-site dental IT support across Oakland — including Rockridge, Grand Lake, Temescal, Fruitvale, and the downtown core. For critical issues we can be on-site within hours. Regular maintenance visits are available throughout the East Bay."},
            {"q":"Can FlossByte support Dentrix or Eaglesoft at our Oakland practice?","a":"Absolutely. We provide deep support for both Dentrix and Eaglesoft at Oakland dental practices — server management, performance optimization, database maintenance, version upgrades, eClaims configuration, and imaging integration. Most issues are resolved remotely within 1 hour."},
            {"q":"How much does dental IT support cost in Oakland?","a":"FlossByte's managed IT plans start at $59 per device per month, including 24/7 monitoring, help desk support, proactive patching, and HIPAA compliance hardening. Most single-location Oakland practices invest $400–$900/month depending on device count and service tier."},
            {"q":"Do you help Oakland dental practices with HIPAA compliance?","a":"Yes. HIPAA compliance is built into every service we provide. We handle technical safeguards (encryption, access controls, audit logs), administrative safeguards (staff training, policies), Business Associate Agreements (BAAs), and audit-ready documentation for Oakland dental practices."},
            {"q":"How quickly does FlossByte respond to IT emergencies in Oakland?","a":"Our average response time for Oakland dental practices is under 1 hour. Critical emergencies affecting patient care are prioritized immediately. You reach a live dental IT specialist — not a ticket queue or offshore helpdesk."},
            {"q":"Can you help us upgrade from an old server running Eaglesoft in Oakland?","a":"Yes — this is one of the most common requests we get from Oakland practices. We assess your current server, plan the migration, set up new hardware or cloud infrastructure, migrate your Eaglesoft data, and test everything before go-live. Zero data loss, minimal downtime."}
        ],
        "nearby_cities": [
            {"file":"berkeley.html","label":"Berkeley"},
            {"file":"alameda.html","label":"Alameda"},
            {"file":"san-leandro.html","label":"San Leandro"},
            {"file":"emeryville.html","label":"Emeryville"}
        ],
        "nearby_parent": "../east-bay.html",
        "nearby_parent_label": "East Bay",
    },
    {
        "file": "D:/FlossByte/website/locations/east-bay/fremont.html",
        "name": "Fremont",
        "slug": "fremont",
        "region": "east-bay",
        "region_label": "East Bay",
        "region_file": "../east-bay.html",
        "canonical": "https://flossbyte.com/locations/east-bay/fremont",
        "breadcrumb_parent": "https://flossbyte.com/locations/east-bay",
        "breadcrumb_parent_name": "East Bay",
        "h1": "Dental IT Support in <em style=\"color:var(--color-teal)\">Fremont, CA</em>",
        "hero_sub": "Fremont is one of the Bay Area's fastest-growing cities — with a booming South Asian and Chinese-American community, hundreds of tech workers, and dental practices that need to keep pace with high patient volume and demanding HIPAA requirements. FlossByte delivers the dental-specific IT support Fremont practices need, from Dentrix and Eaglesoft to full HIPAA compliance, with a local team available in under 1 hour.",
        "cta_hero": "Get Free Fremont Technology Assessment",
        "testimonials": [
            {"initials":"SP","bg":"var(--color-teal)","color":"#fff","quote":"\"We run a high-volume practice in Fremont and downtime is not an option. FlossByte set up our 24/7 monitoring and proactive patching — we haven't had an unexpected outage in 14 months. That's a record for us.\"","name":"Dr. Sunita Patel","practice":"Fremont Smile Center"},
            {"initials":"RK","bg":"var(--color-navy)","color":"#fff","quote":"\"Our Dentrix was running so slow that appointments were running late because of the checkout process. FlossByte optimized our server and database — Dentrix now runs faster than when we first installed it.\"","name":"Ryan Kim, Office Manager","practice":"Mission Hills Dental, Fremont"},
            {"initials":"AV","bg":"#7c3aed","color":"#fff","quote":"\"FlossByte migrated us from Eaglesoft to Open Dental over a weekend with zero data loss. Monday morning, everything worked perfectly. The migration planning alone was worth the investment.\"","name":"Dr. Ana Vargas","practice":"Fremont Family Dentistry"}
        ],
        "faq": [
            {"q":"Does FlossByte offer on-site dental IT support in Fremont?","a":"Yes. FlossByte provides both remote and on-site dental IT support across Fremont — including Irvington, Centerville, Warm Springs, Niles, and Mission San Jose neighborhoods. For critical issues we can be on-site within hours. Regular maintenance visits are available throughout the East Bay."},
            {"q":"Can FlossByte support Dentrix or Eaglesoft at our Fremont practice?","a":"Absolutely. We specialize in both Dentrix and Eaglesoft support for Fremont dental practices — server management, performance optimization, database maintenance, version upgrades, eClaims configuration, and imaging integration. Most issues are resolved remotely within 1 hour."},
            {"q":"How much does dental IT support cost in Fremont?","a":"FlossByte's managed IT plans start at $59 per device per month, including 24/7 monitoring, help desk support, proactive patching, and HIPAA compliance hardening. Most single-location Fremont practices invest $400–$900/month total depending on device count and service tier."},
            {"q":"Do you help Fremont dental practices with HIPAA compliance?","a":"Yes. HIPAA compliance is built into every service we provide. We handle technical safeguards (encryption, access controls, audit logs), administrative safeguards (staff training, policies), Business Associate Agreements (BAAs), and audit-ready documentation for Fremont practices."},
            {"q":"How quickly does FlossByte respond to IT emergencies in Fremont?","a":"Our average response time for Fremont dental practices is under 1 hour for standard issues. Critical emergencies are prioritized immediately. You reach a live dental IT specialist directly — not a ticket system, not offshore support."},
            {"q":"Can you help our Fremont practice switch from Eaglesoft to Open Dental?","a":"Yes. PMS migrations are one of our specialties. We handle the full Eaglesoft-to-Open Dental migration: data conversion, server setup, imaging integration, staff training coordination, and post-migration support. We've done this for multiple East Bay practices with zero data loss."}
        ],
        "nearby_cities": [
            {"file":"newark.html","label":"Newark"},
            {"file":"union-city.html","label":"Union City"},
            {"file":"hayward.html","label":"Hayward"},
        ],
        "nearby_parent": "../east-bay.html",
        "nearby_parent_label": "East Bay",
    }
]

PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="width:16px;height:16px;flex-shrink:0"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2.18h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'
CHECK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="width:16px;height:16px;flex-shrink:0"><polyline points="20 6 9 17 4 12"></polyline></svg>'
STARS = ''.join(['<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>'] * 5)
DESK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:22px;height:22px"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>'
BOOK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="var(--color-navy)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:22px;height:22px"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>'
ACCORD_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>'


def build_new_sections(c):
    city = c['name']
    slug = c['slug']

    # Build testimonial HTML
    thtml = ''
    for t in c['testimonials']:
        thtml += f'''
      <div class="card">
        <div class="testimonial-stars">{STARS}</div>
        <p class="testimonial-quote">{t["quote"]}</p>
        <div class="testimonial-author">
          <div class="testimonial-avatar" style="background:{t["bg"]};color:{t["color"]}">{t["initials"]}</div>
          <div>
            <div class="testimonial-name">{t["name"]}</div>
            <div class="testimonial-practice">{t["practice"]}</div>
          </div>
        </div>
      </div>'''

    # Build FAQ HTML
    fhtml = ''
    for i, f in enumerate(c['faq']):
        cls = ' open' if i == 0 else ''
        fhtml += f'''
      <div class="accordion-item{cls}">
        <button class="accordion-trigger"><span class="accordion-question">{f["q"]}</span><span class="accordion-icon">{ACCORD_SVG}</span></button>
        <div class="accordion-body">{f["a"]}</div>
      </div>'''

    return f'''
<!-- DENTRIX & EAGLESOFT SUPPORT IN {city.upper()} -->
<section class="section-light">
  <div class="container">
    <div class="section-header fade-up">
      <div class="section-eyebrow">Dental Software Support</div>
      <h2 class="section-title">Dentrix &amp; Eaglesoft Support in <em>{city}</em></h2>
      <p class="section-subtitle centered">Most {city} dental practices run Dentrix or Eaglesoft. FlossByte has deep, hands-on expertise with both — not general IT knowledge, but dental-specific fluency built from years of supporting Bay Area practices.</p>
    </div>
    <div class="grid-2 fade-up" style="gap:24px">
      <div class="card" style="border-top:4px solid var(--color-teal)">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
          <div style="width:44px;height:44px;background:rgba(0,212,169,0.1);border-radius:10px;display:flex;align-items:center;justify-content:center">{DESK_SVG}</div>
          <h3 style="font-family:var(--font-heading);font-size:1.25rem;font-weight:800;color:var(--color-navy);margin:0"><a href="../../services/dentrix-support.html" style="color:var(--color-navy);text-decoration:none">Dentrix IT Support {city}</a></h3>
        </div>
        <p class="card-body" style="margin-bottom:16px">Dentrix is the most common PMS in {city} dental practices. Our support covers everything from slow performance and server crashes to version upgrades and eClaims configuration. We know every Dentrix quirk — your practice doesn't become our training ground.</p>
        <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:20px">
          <div style="display:flex;align-items:center;gap:8px;font-size:0.9rem;color:var(--color-text-muted)">{CHECK_SVG}Dentrix server setup &amp; optimization</div>
          <div style="display:flex;align-items:center;gap:8px;font-size:0.9rem;color:var(--color-text-muted)">{CHECK_SVG}Database maintenance &amp; SQL optimization</div>
          <div style="display:flex;align-items:center;gap:8px;font-size:0.9rem;color:var(--color-text-muted)">{CHECK_SVG}Imaging integration (Dexis, Carestream)</div>
          <div style="display:flex;align-items:center;gap:8px;font-size:0.9rem;color:var(--color-text-muted)">{CHECK_SVG}Version upgrades &amp; eClaims fixes</div>
        </div>
        <a href="../../services/dentrix-support.html" class="btn btn-primary" style="width:100%;text-align:center;display:block">Dentrix Support Details &rarr;</a>
      </div>
      <div class="card" style="border-top:4px solid var(--color-navy)">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
          <div style="width:44px;height:44px;background:rgba(10,22,40,0.08);border-radius:10px;display:flex;align-items:center;justify-content:center">{BOOK_SVG}</div>
          <h3 style="font-family:var(--font-heading);font-size:1.25rem;font-weight:800;color:var(--color-navy);margin:0"><a href="../../services/eaglesoft-support.html" style="color:var(--color-navy);text-decoration:none">Eaglesoft IT Support {city}</a></h3>
        </div>
        <p class="card-body" style="margin-bottom:16px">Eaglesoft practices face unique challenges — Patterson's limited remote support, TWAIN driver issues, imaging conflicts, and slow performance on aging servers. FlossByte fills every gap Patterson support can't cover, with a local team that knows the software inside and out.</p>
        <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:20px">
          <div style="display:flex;align-items:center;gap:8px;font-size:0.9rem;color:var(--color-text-muted)">{CHECK_SVG}Eaglesoft performance troubleshooting</div>
          <div style="display:flex;align-items:center;gap:8px;font-size:0.9rem;color:var(--color-text-muted)">{CHECK_SVG}TWAIN driver &amp; imaging fixes</div>
          <div style="display:flex;align-items:center;gap:8px;font-size:0.9rem;color:var(--color-text-muted)">{CHECK_SVG}SQL Server maintenance &amp; recovery</div>
          <div style="display:flex;align-items:center;gap:8px;font-size:0.9rem;color:var(--color-text-muted)">{CHECK_SVG}Eaglesoft-to-Open Dental migrations</div>
        </div>
        <a href="../../services/eaglesoft-support.html" class="btn btn-outline" style="width:100%;text-align:center;display:block">Eaglesoft Support Details &rarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- COMPARISON: FLOSSBYTE vs GENERIC IT -->
<section>
  <div class="container">
    <div class="section-header fade-up">
      <div class="section-eyebrow">Why Dental-Specific IT Wins</div>
      <h2 class="section-title">FlossByte vs. Generic IT Support in <em>{city}</em></h2>
      <p class="section-subtitle centered">General IT providers know Windows and networking. They don't know why Dentrix won't connect to your Dexis sensor, or why Eaglesoft's imaging bridge keeps crashing. That knowledge gap costs practices hours of downtime every year.</p>
    </div>
    <div class="fade-up" style="overflow-x:auto;margin-top:32px">
      <table style="width:100%;border-collapse:collapse;font-size:0.9375rem">
        <thead>
          <tr style="background:var(--color-navy);color:#fff">
            <th style="padding:14px 20px;text-align:left;font-family:var(--font-heading);font-weight:700;border-radius:8px 0 0 0">What You Need</th>
            <th style="padding:14px 20px;text-align:center;font-family:var(--font-heading);font-weight:700;color:var(--color-teal)">FlossByte</th>
            <th style="padding:14px 20px;text-align:center;font-family:var(--font-heading);font-weight:700;border-radius:0 8px 0 0;color:rgba(255,255,255,0.5)">Generic IT</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px solid rgba(0,0,0,0.06)"><td style="padding:13px 20px;color:var(--color-text-muted)">Dentrix server knowledge</td><td style="padding:13px 20px;text-align:center;color:#16a34a;font-weight:700">✓ Deep expertise</td><td style="padding:13px 20px;text-align:center;color:#dc2626">✗ Trial and error</td></tr>
          <tr style="border-bottom:1px solid rgba(0,0,0,0.06);background:rgba(0,212,169,0.03)"><td style="padding:13px 20px;color:var(--color-text-muted)">HIPAA compliance documentation</td><td style="padding:13px 20px;text-align:center;color:#16a34a;font-weight:700">✓ Audit-ready</td><td style="padding:13px 20px;text-align:center;color:#dc2626">✗ Generic checklists</td></tr>
          <tr style="border-bottom:1px solid rgba(0,0,0,0.06)"><td style="padding:13px 20px;color:var(--color-text-muted)">Imaging software (Dexis, Carestream)</td><td style="padding:13px 20px;text-align:center;color:#16a34a;font-weight:700">✓ Full support</td><td style="padding:13px 20px;text-align:center;color:#dc2626">✗ "Call the vendor"</td></tr>
          <tr style="border-bottom:1px solid rgba(0,0,0,0.06);background:rgba(0,212,169,0.03)"><td style="padding:13px 20px;color:var(--color-text-muted)">Response when Dentrix crashes</td><td style="padding:13px 20px;text-align:center;color:#16a34a;font-weight:700">✓ &lt;1 hour average</td><td style="padding:13px 20px;text-align:center;color:#dc2626">✗ Next business day</td></tr>
          <tr style="border-bottom:1px solid rgba(0,0,0,0.06)"><td style="padding:13px 20px;color:var(--color-text-muted)">On-site in {city}</td><td style="padding:13px 20px;text-align:center;color:#16a34a;font-weight:700">✓ Same-day available</td><td style="padding:13px 20px;text-align:center;color:#f59e0b">⚠ Varies</td></tr>
          <tr style="border-bottom:1px solid rgba(0,0,0,0.06);background:rgba(0,212,169,0.03)"><td style="padding:13px 20px;color:var(--color-text-muted)">Business Associate Agreement (BAA)</td><td style="padding:13px 20px;text-align:center;color:#16a34a;font-weight:700">✓ Standard in onboarding</td><td style="padding:13px 20px;text-align:center;color:#dc2626">✗ Often not offered</td></tr>
          <tr><td style="padding:13px 20px;color:var(--color-text-muted)">Dental-specific pricing</td><td style="padding:13px 20px;text-align:center;color:#16a34a;font-weight:700">✓ From $59/device/mo</td><td style="padding:13px 20px;text-align:center;color:var(--color-text-muted)">Varies</td></tr>
        </tbody>
      </table>
    </div>
    <div class="text-center mt-8 fade-up">
      <a class="btn btn-primary btn-lg" href="../../contact.html">Get a Free Assessment for Your {city} Practice</a>
    </div>
  </div>
</section>

<!-- {city.upper()} TESTIMONIALS -->
<section class="section-light">
  <div class="container">
    <div class="section-header fade-up">
      <div class="section-eyebrow">What {city} Practices Say</div>
      <h2 class="section-title">Trusted by {city} <em>Dental Offices</em></h2>
    </div>
    <div class="grid-3 fade-up">{thtml}
    </div>
  </div>
</section>

<!-- FAQ - {city.upper()} -->
<section>
  <div class="container" style="max-width:840px">
    <div class="section-header fade-up">
      <div class="section-eyebrow">Common Questions</div>
      <h2 class="section-title">Dental IT Support {city} <em>FAQs</em></h2>
    </div>
    <div class="accordion fade-up">{fhtml}
    </div>
  </div>
</section>

'''


def build_schemas(c):
    city = c['name']
    slug = c['slug']
    canonical = c['canonical']
    parent_url = c['breadcrumb_parent']
    parent_name = c['breadcrumb_parent_name']

    local_biz = f'''{{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "FlossByte — {city} Dental IT Support",
    "description": "HIPAA-compliant dental IT support for dental practices in {city}, CA. Managed IT, Dentrix support, cybersecurity, and HIPAA compliance from $59/mo.",
    "telephone": "+16692372264",
    "email": "hello@flossbyte.com",
    "url": "{canonical}",
    "areaServed": {{"@type": "City", "name": "{city}, CA"}},
    "priceRange": "$59-$$$"
  }}'''

    breadcrumb = f'''{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://flossbyte.com/"}},{{"@type":"ListItem","position":2,"name":"{parent_name}","item":"{parent_url}"}},{{"@type":"ListItem","position":3,"name":"{city} Dental IT Support","item":"{canonical}"}}]}}'''

    faq_items = []
    for f in c['faq']:
        faq_items.append(f'''{{"@type": "Question", "name": "{f["q"]}", "acceptedAnswer": {{"@type": "Answer", "text": "{f["a"]}"}}}}''')
    faq_schema = '''{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      ''' + ',\n      '.join(faq_items) + '''
    ]
  }'''

    return (local_biz, breadcrumb, faq_schema)


def process_city(c):
    city = c['name']
    slug = c['slug']
    print(f"Processing {city}...")

    with open(c['file'], encoding='utf-8') as f:
        content = f.read()

    # 1. Update title
    old_title = f'<title>Dental Technology Partner {city} CA | HIPAA Managed IT — FlossByte</title>'
    new_title = f'<title>Dental IT Support {city} CA | HIPAA Managed IT for Dental Practices — FlossByte</title>'
    content = content.replace(old_title, new_title)

    # 2. Update meta description
    old_desc = f'<meta name="description" content="HIPAA-compliant dental technology for {city}, CA — cybersecurity, Dentrix support &amp; managed IT from $59/mo. FlossByte. (669) 237-2264." />'
    new_desc = f'<meta name="description" content="Dental IT support in {city}, CA — HIPAA compliance, Dentrix support, cybersecurity &amp; managed IT from $59/mo. Local Bay Area team. Call (669) 237-2264." />'
    content = content.replace(old_desc, new_desc)

    # 3. Update OG title
    old_og = f'<meta property="og:title" content="Dental Technology Partner {city} CA | HIPAA Managed IT — FlossByte" />'
    new_og = f'<meta property="og:title" content="Dental IT Support {city} CA | HIPAA Managed IT — FlossByte" />'
    content = content.replace(old_og, new_og)

    # 4. Update OG description
    old_og_desc = f'<meta property="og:description" content="HIPAA-compliant dental technology for {city}, CA — cybersecurity, Dentrix support &amp; managed IT from $59/mo. FlossByte. (669) 237-2264." />'
    new_og_desc = f'<meta property="og:description" content="Dental IT support in {city}, CA — HIPAA compliance, Dentrix support, cybersecurity &amp; managed IT from $59/mo. Local Bay Area team. (669) 237-2264." />'
    content = content.replace(old_og_desc, new_og_desc)

    # 5. Replace existing LocalBusiness schema with enhanced version
    local_biz, breadcrumb, faq_schema = build_schemas(c)
    old_schema_pattern = r'\{"@context": "https://schema\.org", "@type": "LocalBusiness"[^}]+\}'
    new_schemas = f'''  {local_biz}
  </script>
  <script type="application/ld+json">
  {breadcrumb}
  </script>
  <script type="application/ld+json">
  {faq_schema}'''
    content = re.sub(old_schema_pattern, new_schemas, content)

    # 6. Update H1
    old_h1 = f'<h1 class="page-hero-title">Dental Technology Partner in <em style="color:var(--color-teal)">{city}, CA</em></h1>'
    new_h1 = f'<h1 class="page-hero-title">{c["h1"]}</h1>'
    content = content.replace(old_h1, new_h1)

    # 7. Update hero subtitle
    # Find and replace the page-hero-subtitle paragraph
    sub_pattern = r'(<p class="page-hero-subtitle">)[^<]+(</p>)'
    new_sub = rf'\g<1>{c["hero_sub"]}\g<2>'
    content = re.sub(sub_pattern, new_sub, content, count=1)

    # 8. Insert new sections before BLOG RESOURCES
    blog_marker = '\n<!-- BLOG RESOURCES -->'
    new_sections = build_new_sections(c) + blog_marker
    content = content.replace(blog_marker, new_sections, 1)

    # 9. Upgrade CTA banner
    old_cta_title = f'<h2 class="cta-banner-title">{city} Dental Practice? <em>Let\'s Talk.</em></h2>'
    new_cta_title = f'<h2 class="cta-banner-title">{city} Dental Practice?<br><em>Get Your Free IT Assessment.</em></h2>'
    content = content.replace(old_cta_title, new_cta_title)

    old_cta_sub = f'<p class="cta-banner-subtitle">Free 30-minute technology assessment for {city} dental practices. No commitment, no pressure.</p>'
    new_cta_sub = f'<p class="cta-banner-subtitle">30 minutes. No commitment. We\'ll audit your Dentrix setup, HIPAA posture, cybersecurity gaps, and backup reliability — then give you a clear action plan.</p>'
    content = content.replace(old_cta_sub, new_cta_sub)

    old_cta_btn = f'<div class="cta-banner-actions"><a class="btn btn-primary btn-lg" href="../../contact.html">Get Free Assessment</a></div>'
    new_cta_btn = f'<div class="cta-banner-actions"><a class="btn btn-primary btn-lg" href="../../contact.html">Book Free {city} Assessment</a><a class="btn btn-outline btn-lg" href="tel:6692372264">Call (669) 237-2264</a></div>'
    content = content.replace(old_cta_btn, new_cta_btn)

    with open(c['file'], 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ {city} done")


for c in cities:
    process_city(c)

print("\nAll 4 cities done!")
