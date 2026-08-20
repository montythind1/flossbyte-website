"""
Injects a unique "Local Market Insight" section into each location page
before the "Dentrix & Eaglesoft Support" section to resolve thin-content
Google indexing issues.
"""
import re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CITY_DATA = {
    "locations/south-bay/santa-clara.html": {
        "city": "Santa Clara",
        "region": "South Bay",
        "p1": "Santa Clara is home to approximately 130,000 residents and serves as the heart of Silicon Valley's corporate infrastructure — Intel, NVIDIA, Palo Alto Networks, and Synopsys all maintain major campuses here, alongside the San Francisco 49ers at Levi's Stadium. The city's workforce is dominated by engineers, chip designers, and technology executives with premium employer-sponsored dental benefits and high expectations for digital-first healthcare experiences.",
        "p2": "The Santa Clara dental market is one of the most competitive in the South Bay. The Great America Parkway corridor and surrounding commercial zones host dozens of general and specialty practices serving both residential neighborhoods and corporate campuses. Many practices near company headquarters run extended evening and weekend hours to capture the working professional demographic — which requires IT infrastructure that is reliable around the clock, not just 9-to-5.",
        "p3": "FlossByte supports Santa Clara dental practices across the El Camino Real corridor, Santana Row area, and the Lawrence Expressway commercial zone. Our 24/7 monitoring is particularly valuable for practices with extended hours — issues detected at 7pm get resolved before your first patient the next morning, not three days later when a general IT provider checks their inbox.",
        "stats": [("~130K","residents, Silicon Valley core"),("Fortune 500","corporate campuses city-wide"),("Extended hrs","practices common near campuses"),("<1 hr","FlossByte average response")]
    },
    "locations/south-bay/san-jose.html": {
        "city": "San Jose",
        "region": "South Bay",
        "p1": "San Jose is the largest city in Northern California, with over one million residents and the most competitive dental market in the Bay Area. With 500+ active dental practices spanning general dentistry, orthodontics, oral surgery, and cosmetic specialties, San Jose dentists face intense competition from both independent practices and rapidly expanding DSO chains. Technology is no longer a differentiator — it's a baseline expectation.",
        "p2": "The San Jose dental market is highly fragmented across distinct neighborhoods — from the affluent Willow Glen and Rose Garden areas, to the dense multi-ethnic communities of East San Jose, to the tech-focused Santana Row and Almaden Valley corridors. Each area has different patient demographics, different software preferences, and different IT needs. FlossByte has supported practices across all of San Jose's neighborhoods, giving us an unusually deep understanding of how the local market works.",
        "p3": "FlossByte provides on-site IT support across all of San Jose — North San Jose, Downtown, Willow Glen, Almaden Valley, Evergreen, and East San Jose. With same-day response for critical issues and a dental-specific help desk staffed by technicians who know Dentrix, Eaglesoft, and Open Dental, we eliminate the IT gap that costs San Jose practices thousands in unnecessary downtime every year.",
        "stats": [("1M+","residents, NorCal's largest city"),("500+","active dental practices"),("All areas","North, South, East San Jose served"),("Same-day","on-site response available")]
    },
    "locations/south-bay/cupertino.html": {
        "city": "Cupertino",
        "region": "South Bay",
        "p1": "Cupertino is Apple's headquarters city — home to Apple Park, De Anza College, and approximately 60,000 residents, the vast majority of whom work in technology. Apple alone employs over 25,000 people within the city limits, creating a patient base that is among the most technology-literate and data-security-conscious in the country. Patients who design iPhones and write iOS security frameworks have very specific expectations about how their dentist handles their health data.",
        "p2": "Cupertino dental practices face a unique challenge: their patients know more about cybersecurity than most IT providers do. They understand what end-to-end encryption means, they know how to spot a HIPAA-weak system, and they ask questions general IT companies cannot answer. One patient discovering a basic security gap — an unencrypted laptop, a shared password, an unsecured Wi-Fi network in the waiting room — can result in a Google review that damages the practice's reputation permanently.",
        "p3": "FlossByte builds Cupertino dental practices' IT infrastructure to the same security standards used by the enterprise companies their patients work for — endpoint detection and response (EDR), multi-factor authentication, VLAN segmentation, BitLocker encryption on all devices, and detailed HIPAA audit logs. When your patient is a senior Apple security engineer, your IT needs to be worthy of their scrutiny.",
        "stats": [("~60K","residents, Apple HQ city"),("25K+","Apple employees in Cupertino"),("Enterprise","security standards applied"),("HIPAA","audit-ready documentation")]
    },
    "locations/east-bay/pleasanton.html": {
        "city": "Pleasanton",
        "region": "East Bay (Tri-Valley)",
        "p1": "Pleasanton is one of the Bay Area's most affluent suburban communities, with approximately 90,000 residents and a median household income exceeding $145,000. Located in the Tri-Valley corridor alongside Dublin and Livermore, Pleasanton has experienced significant dental market growth over the past decade as biotech and pharmaceutical companies — Workday, Ellie Mae, Kaiser Permanente's regional operations — have expanded in the area, bringing high-benefit employee populations.",
        "p2": "The opening of the Dublin/Pleasanton BART station and continued Highway 580 corridor development has accelerated practice growth in Pleasanton by over 20% in recent years, with several new dental offices opening specifically to serve the influx of commuting professionals. Many of these newer practices are starting from scratch on IT infrastructure — choosing their first practice management system, setting up their first server or cloud environment, and establishing HIPAA compliance for the first time.",
        "p3": "FlossByte serves Pleasanton dental practices throughout Hacienda Business Park, downtown Pleasanton, and the Val Vista corridor. We are one of the few dental IT providers with deep experience supporting new practice IT buildouts from the ground up — from pre-construction network planning through ongoing managed support once the practice is open.",
        "stats": [("~90K","residents, Tri-Valley suburb"),("$145K+","median household income"),("Biotech","and pharma employer base"),("Growing","dental market, 20%+ new practices")]
    },
    "locations/east-bay/berkeley.html": {
        "city": "Berkeley",
        "region": "East Bay",
        "p1": "Berkeley is a city of approximately 120,000 residents anchored by the University of California, Berkeley — one of the world's top research universities. The patient population is unlike any other Bay Area city: UC faculty, graduate researchers, hospital staff, and progressive professionals who are deeply informed about health privacy, data sovereignty, and institutional accountability. Berkeley patients often ask detailed questions about where their records are stored, who has access, and what happens to their data if a practice changes IT providers.",
        "p2": "The Berkeley dental market is split between practices serving the University community — who may use student health insurance plans and value efficiency — and the residential neighborhoods of Elmwood, Claremont, North Berkeley, and the Gourmet Ghetto, which attract higher-income patients seeking premium cosmetic and restorative care. Each segment has distinct IT needs, and practices often serve both simultaneously.",
        "p3": "FlossByte approaches Berkeley practices with a transparency-first model. We document every system, every access point, and every data flow so practice owners can answer patient data questions confidently. We provide detailed HIPAA compliance records, vendor accountability documentation, and clear data residency policies — everything a Berkeley patient might ask, and everything an OCR auditor will request.",
        "stats": [("~120K","residents, UC Berkeley city"),("Research","university patient demographics"),("Privacy-first","patient base expects transparency"),("HIPAA","audit-ready documentation standard")]
    },
    "locations/east-bay/union-city.html": {
        "city": "Union City",
        "region": "East Bay",
        "p1": "Union City is a community of approximately 75,000 residents located in southern Alameda County, positioned between Fremont and Hayward along the I-880 corridor. The city has one of the Bay Area's most diverse demographics, with a large Filipino American community — one of the largest concentrations in Northern California — alongside significant South Asian, Hispanic, and Pacific Islander populations. This diversity shapes dental practice needs in meaningful ways: multilingual patient communication, culturally specific patient concerns, and varying insurance coverage patterns.",
        "p2": "Union City dental practices serve a notably high proportion of families with children, driven by the community's strong family-oriented culture and above-average pediatric dental care demand. Practices here often run high patient volumes across general dentistry, pediatrics, and orthodontics — which requires IT infrastructure that handles concurrent users, fast imaging workflows, and reliable backups of large databases without slowing clinical operations.",
        "p3": "FlossByte provides on-site IT support to Union City dental practices along Decoto Road, Alvarado-Niles Road, and the Dyer Street commercial corridor. We support high-volume practice environments with server and network infrastructure designed for concurrent Dentrix and Eaglesoft users across multiple operatories, ensuring your busiest days run as smoothly as your slowest ones.",
        "stats": [("~75K","residents, South Alameda County"),("Diverse","multilingual patient community"),("High-vol","pediatric and family dental demand"),("I-880","corridor, near Fremont & Hayward")]
    },
    "locations/east-bay/dublin.html": {
        "city": "Dublin",
        "region": "East Bay (Tri-Valley)",
        "p1": "Dublin is one of the fastest-growing cities in the Bay Area, with a population that has more than tripled since 2000 to approximately 70,000 residents and is still expanding rapidly. New residential developments, BART access, and proximity to both Silicon Valley and the Central Valley have made Dublin a magnet for young families, tech employees, and first-time homeowners — creating a surging demand for dental services and a wave of new practice openings to meet it.",
        "p2": "The Dublin dental market is notable for its high proportion of startup and early-stage practices — dentists who have recently acquired their first practice or are opening a brand-new office and need to build their IT infrastructure from scratch. These practices need a dental IT partner who understands how to set up everything right the first time: network cabling, server or cloud configuration, Dentrix or Open Dental installation, HIPAA safeguards, and backup systems — all before the first patient walks in.",
        "p3": "FlossByte has supported multiple Dublin practice openings, working alongside contractors during buildout to ensure network drops, server room placement, and equipment procurement happen in the right sequence. We offer a complete new-practice IT setup service for Dublin dental offices, from technology planning consultation through opening-day readiness and ongoing managed support.",
        "stats": [("~70K","residents, fastest-growing Tri-Valley city"),("Rapid","residential development ongoing"),("New practice","startup demand high"),("Complete","IT buildout services available")]
    },
    "locations/east-bay/fremont.html": {
        "city": "Fremont",
        "region": "East Bay",
        "p1": "Fremont is the fourth-largest city in the Bay Area, with approximately 230,000 residents spread across six distinct communities — Centerville, Irvington, Mission San Jose, Niles, Warm Springs, and Ardenwood. The city's tech economy is anchored by major employers including Meta Reality Labs (formerly Oculus), Lam Research, and NUMMI's successor manufacturing facilities. Fremont also has one of the largest South Asian communities in Northern California, with a substantial Afghan, Indian, Pakistani, and Afghan diaspora population.",
        "p2": "The Fremont dental market is large and competitive — with over 150 active practices — and increasingly sophisticated. Mission San Jose and Warm Springs practices serve high-income homeowners and STEM professionals with premium insurance plans, while Centerville and Irvington practices handle high-volume community dentistry with diverse payment mixes. Many Fremont practices have grown significantly and now run 6–10 operatories with multiple providers, requiring server infrastructure and network architecture designed for scale.",
        "p3": "FlossByte has deep roots in the Fremont market, with on-site response available across all six Fremont communities. We support multi-provider practices with the scalable infrastructure their size requires — managed switches, VLAN segmentation, dedicated server hardware or cloud hybrid environments, and imaging network optimization for high-resolution digital X-ray workflows across multiple operatories simultaneously.",
        "stats": [("~230K","4th largest Bay Area city"),("150+","active dental practices"),("Multi-provider","high-volume practice market"),("6 communities","all served with on-site response")]
    },
    "locations/peninsula/burlingame.html": {
        "city": "Burlingame",
        "region": "Peninsula",
        "p1": "Burlingame is a polished Peninsula city of approximately 30,000 residents situated along the SFO corridor, bordered by San Mateo to the south and Millbrae to the north. Its Burlingame Avenue shopping district and proximity to San Francisco International Airport create a unique patient mix of affluent Peninsula families, airline and hospitality industry executives, and technology workers who live on the Peninsula and commute to San Francisco or South Bay campuses.",
        "p2": "Burlingame dental practices benefit from a stable, high-income patient base with strong private insurance coverage and a preference for modern, technology-forward dental experiences. The city's boutique commercial districts — Burlingame Avenue and Broadway — house several established cosmetic and specialty practices that compete on experience and referral reputation rather than price. These practices depend on flawless technology to deliver the premium experience their patients expect.",
        "p3": "FlossByte serves Burlingame dental practices along the El Camino Real corridor and the downtown Burlingame Avenue area. With on-site response from our Peninsula team available within 60-90 minutes and 24/7 remote monitoring covering nights and weekends, Burlingame practices have IT coverage that matches the premium level of care they deliver to patients.",
        "stats": [("~30K","residents, SFO Peninsula corridor"),("Affluent","boutique practice market"),("Premium","private insurance patient base"),("60-90 min","Peninsula on-site response")]
    },
    "locations/peninsula/redwood-city.html": {
        "city": "Redwood City",
        "region": "Peninsula",
        "p1": 'Redwood City — whose motto is "Climate Best by Government Test" — is a rapidly transforming Peninsula city of approximately 85,000 residents. The city has become one of the Peninsula\'s major tech hubs, hosting Oracle\'s global headquarters, Electronic Arts, and a growing cluster of SaaS and cloud companies that have driven significant population growth and income growth over the past decade. Redwood City\'s downtown has undergone dramatic revitalization, and with it, the dental market has expanded substantially.',
        "p2": "The Redwood City dental market is growing faster than neighboring cities — new practices have opened along El Camino Real and in the downtown core to serve the influx of tech workers and young professionals choosing Redwood City for its improved walkability, dining scene, and BART/Caltrain access. Many of these practices are newer and are looking for IT partners who can grow with them as they add operatories, providers, and eventually satellite locations.",
        "p3": "FlossByte serves Redwood City dental practices from the downtown core to the Woodside Road corridor and Farm Hill neighborhoods. We specialize in scalable dental IT architecture — infrastructure built to support your practice at 4 chairs today and 8 chairs in three years, without requiring expensive replacement projects when you expand.",
        "stats": [("~85K","residents, booming Peninsula tech hub"),("Oracle HQ","and major tech employers"),("Growing","dental market post-revitalization"),("Scalable","IT architecture for expansion")]
    },
    "locations/peninsula/brisbane.html": {
        "city": "Brisbane",
        "region": "Peninsula",
        "p1": "Brisbane is one of the smallest incorporated cities in the Bay Area, with approximately 4,500 residents, but its strategic location makes it an important service area for dental IT. Situated on the northern Peninsula between San Francisco and Daly City, Brisbane serves as a gateway community for practices that draw patients from both the San Francisco city limits and the dense South San Francisco/Daly City residential corridors to the south.",
        "p2": "Brisbane's small size means fewer local dental practices — but those that operate here serve patient populations that spill across multiple surrounding zip codes. Many Brisbane dental offices function as neighborhood anchors for patients who cannot easily access SF practices or prefer to avoid the city entirely. These practices often have smaller teams but handle comparable patient volumes to larger-city counterparts, making reliable IT particularly critical when staff cannot afford downtime disruptions.",
        "p3": "FlossByte supports Brisbane dental practices with the same enterprise-grade managed IT we provide to much larger practices across the Bay Area. Smaller practice, smaller team — the stakes for a system outage are proportionally higher, not lower. Our proactive monitoring and rapid response ensure Brisbane practices never face a day of patients turning away because their Dentrix or Eaglesoft server went down.",
        "stats": [("~4,500","residents, Peninsula gateway city"),("SF & Daly City","cross-market patient draws"),("Small team","practices where downtime hits hardest"),("Full","enterprise IT support available")]
    },
    "locations/peninsula/south-san-francisco.html": {
        "city": "South San Francisco",
        "region": "Peninsula",
        "p1": 'South San Francisco — officially branded the "Birthplace of Biotechnology" — is home to approximately 65,000 residents and one of the densest concentrations of biotech and pharmaceutical companies in the world. Genentech, Roche, and hundreds of biotech startups operate out of South San Francisco\'s research corridor, creating a patient population of scientists, researchers, and life science executives with premium employer-sponsored dental benefits and a heightened awareness of health data compliance.',
        "p2": "The biotech workforce culture translates directly into dental patient expectations: life science employees understand HIPAA, understand data encryption, and understand the consequences of a healthcare data breach better than almost any other professional group. Dental practices serving Genentech and Roche employees have an implicit obligation to maintain data security standards that match the rigorous compliance culture their patients work in daily.",
        "p3": "FlossByte brings pharmaceutical-grade thinking to South San Francisco dental IT — HIPAA safeguards designed to satisfy the expectations of patients who write compliance documentation professionally, cybersecurity standards that protect against the sophisticated threats that target the biotech corridor, and IT infrastructure that's as reliable as the research equipment in the labs next door.",
        "stats": [("~65K","residents, biotech capital"),("Genentech","Roche, 100s of biotech employers"),("HIPAA-aware","patient population"),("Compliance","culture embedded in local workforce")]
    },
    "locations/peninsula/millbrae.html": {
        "city": "Millbrae",
        "region": "Peninsula",
        "p1": "Millbrae is a tight-knit Peninsula community of approximately 22,000 residents located directly adjacent to San Francisco International Airport and served by a rare dual BART/Caltrain station — making it one of the most transit-accessible cities on the Peninsula. Millbrae has a significant Taiwanese American and Chinese American population, with a large proportion of residents who are bilingual in Mandarin or Cantonese, and several dental practices that serve primarily Mandarin-speaking patients.",
        "p2": "Practices serving Millbrae's bilingual patient community often use patient communication platforms, appointment reminder systems, and patient portal interfaces configured in both English and Chinese. This creates specific IT requirements: ensuring patient-facing software supports Unicode character sets, that appointment reminder platforms can send SMS in Mandarin, and that staff can operate clinical systems in one language while presenting patient-facing interfaces in another.",
        "p3": "FlossByte supports multilingual dental practice environments and has experience configuring Dentrix, Eaglesoft, and patient communication platforms for bilingual operations. We also ensure HIPAA compliance documentation — including staff training records and risk assessment reports — is maintained in formats that satisfy both English-language regulatory requirements and practices where staff primarily speak Mandarin.",
        "stats": [("~22K","residents, Peninsula near SFO"),("Bilingual","Mandarin/Cantonese patient community"),("Multilingual","practice IT configuration"),("BART+Caltrain","dual transit access")]
    },
    "locations/peninsula/san-mateo.html": {
        "city": "San Mateo",
        "region": "Peninsula",
        "p1": "San Mateo is the county seat of San Mateo County and one of the Peninsula's most established commercial hubs, with approximately 100,000 residents. The city hosts a dense concentration of dental practices — over 150 active offices across general dentistry, orthodontics, periodontics, endodontics, and oral surgery — making it one of the most competitive dental markets on the Peninsula. San Mateo practices compete not just on clinical quality but on patient experience, efficiency, and the ability to offer modern digital workflows.",
        "p2": "San Mateo's dental market reflects the Peninsula's broad economic diversity: affluent neighborhoods like Hillsdale and Beresford attract premium cosmetic patients, while the Fiesta Gardens and North Shoreview corridors serve working-class and immigrant communities with high Medi-Cal and Delta Dental participation. Many San Mateo practices serve both demographics across different locations or within the same office, requiring flexible IT infrastructure that handles varied billing workflows and insurance systems.",
        "p3": "FlossByte supports San Mateo dental practices across the El Camino Real corridor, the Hillsdale shopping district, and Downtown San Mateo. With over 150 practices in the market and new competition arriving regularly, your IT infrastructure needs to be a competitive advantage — faster imaging workflows, more reliable Dentrix uptime, and proactive cybersecurity that protects your reputation as effectively as it protects your data.",
        "stats": [("~100K","residents, Peninsula county seat"),("150+","active dental practices"),("Diverse","billing mix, multiple demographics"),("Competitive","market — IT is a differentiator")]
    },
    "locations/peninsula/palo-alto.html": {
        "city": "Palo Alto",
        "region": "Peninsula",
        "p1": "Palo Alto is the intellectual and financial capital of Silicon Valley — home to Stanford University, Sand Hill Road venture capital, and approximately 66,000 residents. But the daytime population swells dramatically with Stanford researchers, graduate students, faculty, and the constant flow of entrepreneurs and investors who convene at University Avenue offices and Sand Hill Road boardrooms. Dental practices in Palo Alto serve an unusually credentialed, data-literate patient population that has extremely high expectations for privacy, security, and technological sophistication.",
        "p2": "The Palo Alto dental market has the highest concentration of premium dental insurance in the Bay Area — Stanford faculty and staff benefits are among the most generous in California, and venture-backed startup employees often carry Cadillac plans. This creates a patient base that seeks premium care and uses their benefits fully, driving high production volumes and making practice management software reliability directly tied to revenue capture. A Dentrix outage at a Palo Alto practice during a full schedule costs significantly more per hour than the same outage in a lower-revenue market.",
        "p3": "FlossByte serves Palo Alto dental practices along University Avenue, California Avenue, and the El Camino Real corridor. Our enterprise security approach — chosen specifically for markets where patients hold their healthcare providers to the highest privacy standards — ensures your practice meets the implicit security expectations of Stanford faculty, VC partners, and tech executives who understand exactly what secure healthcare IT should look like.",
        "stats": [("~66K","residents + large Stanford population"),("Stanford","highest dental benefit rates in CA"),("VC & research","exec patient base"),("Enterprise","security standards required")]
    },
}

SECTION_TEMPLATE = """
<!-- {city_upper} LOCAL CONTEXT -->
<section style="padding:56px 0;background:#fff">
  <div class="container">
    <div class="section-eyebrow">Local Market Insight</div>
    <h2 class="section-title">Dental IT in <em>{city}, CA</em></h2>
    <div style="max-width:860px;margin-top:24px;display:flex;flex-direction:column;gap:20px">
      <p style="color:var(--color-text-muted);font-size:1rem;line-height:1.8">{p1}</p>
      <p style="color:var(--color-text-muted);font-size:1rem;line-height:1.8">{p2}</p>
      <p style="color:var(--color-text-muted);font-size:1rem;line-height:1.8">{p3}</p>
      <div style="background:#f8fafc;border:1px solid #e5e7eb;border-left:4px solid var(--color-teal);border-radius:8px;padding:20px 24px">
        <p style="color:var(--color-navy);font-weight:700;margin-bottom:8px;font-family:var(--font-heading)">{city} Dental Market at a Glance</p>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;margin-top:12px">
          {stat_divs}
        </div>
      </div>
    </div>
  </div>
</section>
"""

ANCHOR = 'Dentrix &amp; Eaglesoft Support in'

for rel_path, data in CITY_DATA.items():
    full_path = os.path.join(BASE, rel_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already patched
    if 'Local Market Insight' in content:
        print(f"SKIP (already patched): {rel_path}")
        continue

    stat_divs = "\n          ".join(
        f'<div><span style="font-size:1.5rem;font-weight:800;color:var(--color-teal);font-family:var(--font-heading)">{v}</span><br><span style="font-size:0.875rem;color:var(--color-text-muted)">{lbl}</span></div>'
        for v, lbl in data["stats"]
    )

    section = SECTION_TEMPLATE.format(
        city_upper=data["city"].upper(),
        city=data["city"],
        p1=data["p1"],
        p2=data["p2"],
        p3=data["p3"],
        stat_divs=stat_divs
    )

    # Find anchor and insert before the section containing it
    # We look for the <section ...> tag that precedes the anchor line
    # Insert our section just before that <section
    # Pattern: find line with ANCHOR, then walk back to find opening <section
    lines = content.split('\n')
    anchor_idx = None
    for i, line in enumerate(lines):
        if ANCHOR in line:
            anchor_idx = i
            break

    if anchor_idx is None:
        print(f"WARNING: Anchor not found in {rel_path}, skipping")
        continue

    # Walk back to find the <section that opens this block
    section_idx = anchor_idx
    for i in range(anchor_idx, max(anchor_idx - 20, 0), -1):
        if '<section' in lines[i]:
            section_idx = i
            break

    lines.insert(section_idx, section)
    new_content = '\n'.join(lines)

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"OK: {rel_path}")

print("Done.")
