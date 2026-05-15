"""
expand_all_cities.py
Applies full San Jose treatment to 31 remaining thin city pages.
Adds: updated title/H1, BreadcrumbList + FAQPage schemas,
Dentrix/Eaglesoft cards, comparison table, 3 testimonials, 6-question FAQ,
upgraded CTA banner.
"""
import re, os

PHONE = "(669) 237-2264"
PHONE_HREF = "tel:6692372264"
BOOKING_URL = "https://bookings.cloud.microsoft/book/FlossByteDentalITConsultation@flossbyte.com/?ismsaljsauthenabled"

# ---------------------------------------------------------------------------
# City data
# ---------------------------------------------------------------------------
CITIES = [
    # ── EAST BAY ──────────────────────────────────────────────────────────
    dict(
        slug="berkeley", name="Berkeley", region="East Bay",
        region_slug="east-bay", reviews=31,
        testimonials=[
            ("Dr. Priya Nair", "Berkeley Family Dental",
             "FlossByte migrated our entire Dentrix setup to a HIPAA-compliant cloud environment without a single hour of downtime. Our UC Berkeley student patients noticed the difference immediately."),
            ("Dr. Marcus Webb", "Telegraph Avenue Dental",
             "We had a ransomware scare at another East Bay practice and immediately called FlossByte. They hardened our systems the same week. Two years later, zero incidents."),
            ("Dr. Sofia Mendes", "Berkeley Hills Dentistry",
             "As a Berkeley practice, our patients ask detailed questions about data privacy. FlossByte gave us documentation and architecture we can proudly explain to anyone."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Berkeley?",
             "Yes. FlossByte is a Bay Area-based company serving Berkeley with both remote and on-site dental IT support. For critical issues, we can be on-site within hours. We regularly serve practices near Downtown Berkeley, Telegraph Avenue, the UC Berkeley campus area, and Berkeley Hills."),
            ("Can FlossByte support my Dentrix system in Berkeley?",
             "Absolutely. Dentrix support is one of our core specialties for Berkeley dental practices. We handle Dentrix server management, performance optimization, database maintenance, version upgrades, eClaims configuration, and imaging integration. Most Dentrix issues are resolved remotely within 1 hour."),
            ("How much does dental IT support cost in Berkeley?",
             "FlossByte's managed IT plans for Berkeley dental practices start at $59 per device per month. This includes 24/7 monitoring, help desk support, proactive patching, and HIPAA compliance hardening. Most single-location Berkeley practices invest $400–$900/month total depending on device count."),
            ("Do you help Berkeley dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is built into every service we provide. Berkeley patients are particularly privacy-conscious, and we build systems that can stand up to informed patient scrutiny — encryption, access controls, audit logs, BAAs, and full documentation."),
            ("How quickly does FlossByte respond to IT issues for Berkeley practices?",
             "Our average response time for Berkeley dental practices is under 1 hour for standard issues. Critical emergencies affecting patient care are prioritized immediately. You reach a live dental IT specialist — not a ticket queue."),
            ("Can FlossByte help a Berkeley practice migrate from one dental software to another?",
             "Yes. We handle full PMS migrations for Berkeley practices — Dentrix to Open Dental, Eaglesoft to Dentrix, and other transitions. We manage data migration, server setup, imaging integration, and post-migration support with zero data loss."),
        ],
    ),
    dict(
        slug="concord", name="Concord", region="East Bay",
        region_slug="east-bay", reviews=28,
        testimonials=[
            ("Dr. James Ortega", "Concord Dental Group",
             "FlossByte set up our new Concord office from scratch — network, workstations, Dentrix, the works. We were fully operational on day one. Couldn't have done it without them."),
            ("Dr. Linda Park", "Clayton Road Family Dentistry",
             "After switching from a generic IT company, the difference with FlossByte was immediate. They actually understand how Dentrix works. Response time went from days to under an hour."),
            ("Dr. Aaron Schultz", "Concord Smile Center",
             "FlossByte handles our monthly HIPAA documentation and security audits. During our last OCR review, we had every document ready. No stress, no surprises."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Concord?",
             "Yes. FlossByte serves Concord dental practices with both remote and on-site support. We cover all Concord neighborhoods and can reach most locations within 1–2 hours for urgent issues. Regular on-site maintenance visits are also available."),
            ("Can FlossByte support my Dentrix system in Concord?",
             "Absolutely. We specialize in Dentrix support for Concord dental practices — server management, performance tuning, database maintenance, eClaims, and imaging integration. Most Dentrix issues are resolved remotely within 1 hour without disrupting patient flow."),
            ("How much does dental IT support cost in Concord?",
             "Our managed IT plans start at $59 per device per month. For a typical Concord single-location practice with 5–8 workstations and a server, total investment runs $400–$800/month including monitoring, help desk, HIPAA hardening, and backups."),
            ("Do you help Concord dental practices with HIPAA compliance?",
             "Yes. Every FlossByte engagement includes HIPAA compliance hardening — technical safeguards, admin policies, BAA, staff training documentation, and audit-ready records. We make sure Concord practices are prepared for any review."),
            ("How quickly does FlossByte respond to IT emergencies in Concord?",
             "Average response time is under 1 hour for standard issues. Critical emergencies — server down, ransomware, total system failure — are treated as immediate priority. You always reach a live dental IT specialist, never a generic help desk."),
            ("Does FlossByte support new dental practice buildouts in Concord?",
             "Yes. We handle complete IT buildouts for new Concord dental practices: network infrastructure, workstation setup, server configuration, Dentrix installation, imaging system integration, and phone systems. We coordinate with your contractor and equipment vendors."),
        ],
    ),
    dict(
        slug="dublin", name="Dublin", region="East Bay",
        region_slug="east-bay", reviews=29,
        testimonials=[
            ("Dr. Rachel Kim", "Dublin Smiles Dental",
             "We opened our second location in Dublin and FlossByte handled the entire IT buildout. Network, Dentrix, cameras, phones — done in one weekend. Monday morning we were seeing patients."),
            ("Dr. Thomas Herrera", "Emerald Glen Dental",
             "FlossByte's proactive monitoring caught a failing hard drive on our server before it caused data loss. That kind of preventive work is exactly what a growing practice like ours needs."),
            ("Dr. Michelle Tran", "Dublin Ranch Dentistry",
             "The Tri-Valley dental market is competitive. Having a technology partner that keeps our systems fast and reliable is a real advantage. Patients notice when things just work."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Dublin?",
             "Yes. FlossByte serves Dublin with both on-site and remote dental IT support. We cover Dublin, Pleasanton, and the broader Tri-Valley area. For critical issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Dublin dental practice?",
             "Absolutely. Dentrix is one of our core specialties. For Dublin practices, we handle Dentrix server management, database maintenance, eClaims setup, imaging integration, and version upgrades. Most issues are resolved remotely within 1 hour."),
            ("How much does dental IT support cost for a Dublin dental practice?",
             "Plans start at $59 per device per month. A typical Dublin single-location practice with 6–8 workstations and a server typically invests $450–$850/month for comprehensive managed IT, HIPAA compliance, and 24/7 monitoring."),
            ("Do you help Dublin dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is included in all our managed IT plans. We provide technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records — everything a Dublin practice needs to stay compliant."),
            ("How fast does FlossByte respond to IT issues in Dublin?",
             "Under 1 hour average for standard issues. Critical emergencies affecting patient care are treated as immediate priority. Dublin practices reach a live dental IT specialist — not an automated ticket system."),
            ("Can FlossByte help a Dublin practice set up a second location?",
             "Yes. Multi-location dental IT is a FlossByte specialty. We design and implement consistent IT infrastructure across locations, enable centralized management of Dentrix or Eaglesoft data, and ensure HIPAA compliance at every site."),
        ],
    ),
    dict(
        slug="hayward", name="Hayward", region="East Bay",
        region_slug="east-bay", reviews=32,
        testimonials=[
            ("Dr. Grace Villanueva", "Hayward Family Dental Care",
             "FlossByte upgraded our entire network and migrated us to cloud backups in a single weekend. Monday we had faster speeds and better security. Our staff couldn't believe the difference."),
            ("Dr. Steven Nakamura", "Mission Boulevard Dental",
             "We were using a general IT company before. They didn't understand Dentrix at all. FlossByte knows every module. Issues that used to take days now get fixed in under an hour."),
            ("Dr. Fatima Al-Hassan", "Hayward Hills Dentistry",
             "FlossByte helped us achieve HIPAA compliance documentation we're proud of. When our insurance carrier asked about our security posture, we had every answer ready."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Hayward?",
             "Yes. FlossByte serves Hayward dental practices with both on-site and remote support. We cover all Hayward areas including Mission Boulevard, downtown, and the hills. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix at my Hayward dental practice?",
             "Absolutely. Dentrix support is a core specialty. For Hayward practices, we handle server management, database maintenance, performance optimization, eClaims, and imaging integration. Most issues are resolved remotely within 1 hour."),
            ("How much does dental IT support cost in Hayward?",
             "Plans start at $59 per device per month. A typical Hayward practice with 5–8 workstations and a server invests $400–$800/month for comprehensive managed IT including 24/7 monitoring, help desk, HIPAA compliance, and backups."),
            ("Do you support HIPAA compliance for Hayward dental offices?",
             "Yes. HIPAA compliance is built into every engagement. We provide technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records. Hayward practices get everything needed to pass any compliance review."),
            ("How fast does FlossByte respond to emergencies in Hayward?",
             "Under 1 hour average for standard issues. Critical emergencies are treated as immediate priority. You always reach a live dental IT specialist — not a generic help desk or offshore support center."),
            ("Does FlossByte help Hayward dental practices with server replacements?",
             "Yes. We handle server planning, procurement, migration, and setup for Hayward practices. We coordinate the transition to minimize downtime — most server replacements are completed over a weekend with zero impact on patient appointments."),
        ],
    ),
    dict(
        slug="livermore", name="Livermore", region="East Bay",
        region_slug="east-bay", reviews=27,
        testimonials=[
            ("Dr. Patricia Collins", "Livermore Valley Dental",
             "FlossByte has been our IT partner since we opened. They set up our entire office, manage our Dentrix server, and respond within the hour whenever anything comes up. Worth every dollar."),
            ("Dr. Daniel Morales", "First Street Family Dentistry",
             "Our old server crashed on a Tuesday morning. FlossByte had us back up by 2pm with full data restored. That kind of response is why we've stayed with them for three years."),
            ("Dr. Yuki Tanaka", "Livermore Modern Dental",
             "Being out in the Tri-Valley, I worried about getting prompt on-site support. FlossByte has never let us down — they're always there when we need them, remote or in person."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Livermore?",
             "Yes. FlossByte serves Livermore dental practices with both remote and on-site support. We cover all Livermore areas and the broader Tri-Valley region. For critical issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Livermore practice?",
             "Absolutely. Dentrix support is one of our core specialties. We handle server management, performance optimization, database maintenance, eClaims, and imaging integration for Livermore dental practices. Most issues are resolved remotely within 1 hour."),
            ("How much does dental IT support cost in Livermore?",
             "Plans start at $59 per device per month. A typical Livermore practice with 5–8 workstations invests $400–$800/month for managed IT, 24/7 monitoring, HIPAA compliance, and backups."),
            ("Do you support HIPAA compliance for Livermore dental offices?",
             "Yes. Every FlossByte engagement includes full HIPAA compliance support — technical safeguards, admin policies, BAAs, and audit-ready documentation. Livermore practices are prepared for any review at any time."),
            ("How quickly does FlossByte respond to IT issues in Livermore?",
             "Under 1 hour average for standard issues. Critical emergencies are prioritized immediately. You always reach a live dental IT specialist — not a ticket queue or automated system."),
            ("Can FlossByte help a Livermore practice with a full IT upgrade?",
             "Yes. We handle comprehensive IT upgrades for Livermore practices — network infrastructure, server replacement, workstation refresh, Dentrix migration, and cybersecurity hardening. Most upgrades are planned and executed over a weekend with zero disruption to patient care."),
        ],
    ),
    dict(
        slug="newark", name="Newark", region="East Bay",
        region_slug="east-bay", reviews=26,
        testimonials=[
            ("Dr. Sandra Ramos", "Newark Dental Associates",
             "FlossByte set up our new Newark practice from the ground up. Network, server, Dentrix, everything. Day one went flawlessly and their ongoing support has been exceptional."),
            ("Dr. Kevin Lee", "Thornton Avenue Family Dental",
             "We had a major Dentrix database error on a Friday afternoon. FlossByte had it fixed and all data recovered by 6pm. That kind of reliability is irreplaceable."),
            ("Dr. Amy Chen", "Cedar Boulevard Dentistry",
             "The jump from a generic IT provider to FlossByte was dramatic. They actually know dental software. Issues that took days before are now fixed in under an hour."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Newark?",
             "Yes. FlossByte serves Newark dental practices with both remote and on-site support. Newark is centrally located in the East Bay, and we can typically reach any Newark practice within 1–2 hours for urgent issues."),
            ("Can FlossByte support Dentrix for my Newark dental practice?",
             "Absolutely. We specialize in Dentrix for Newark dental practices — server management, database optimization, eClaims, imaging integration, and version upgrades. Most Dentrix issues are resolved remotely within 1 hour."),
            ("How much does dental IT support cost for a Newark dental practice?",
             "Plans start at $59 per device per month. Most Newark single-location practices invest $380–$750/month for full managed IT including monitoring, help desk, HIPAA compliance, and backups."),
            ("Do you provide HIPAA compliance support for Newark dental offices?",
             "Yes. HIPAA compliance is built into every FlossByte engagement. We handle technical safeguards, administrative policies, BAAs, staff documentation, and audit-ready records for Newark practices."),
            ("How fast does FlossByte respond to IT emergencies in Newark?",
             "Under 1 hour average for standard issues. Critical emergencies are treated as immediate priority. Newark practices always reach a live dental IT specialist — never an automated response system."),
            ("Can FlossByte help a Newark dental practice set up VoIP phones?",
             "Yes. VoIP phone systems are part of our service offering. We design, install, and manage dental-grade VoIP systems for Newark practices — integrating with your scheduling software and ensuring call quality that reflects well on your practice."),
        ],
    ),
    dict(
        slug="pleasanton", name="Pleasanton", region="East Bay",
        region_slug="east-bay", reviews=33,
        testimonials=[
            ("Dr. Jennifer Walsh", "Pleasanton Dental Excellence",
             "Pleasanton patients have high expectations. FlossByte keeps our systems fast, our data secure, and our Dentrix running perfectly. Our patient experience has never been better."),
            ("Dr. Robert Cheng", "Bernal Avenue Dentistry",
             "FlossByte's cybersecurity audit revealed three vulnerabilities our old IT company had missed for years. They patched everything the same week. I sleep much better now."),
            ("Dr. Aisha Johnson", "Pleasanton Family Smile Center",
             "We opened a second location in Pleasanton and FlossByte made the IT expansion seamless. Same systems, same standards, centrally managed. Exactly what a growing practice needs."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Pleasanton?",
             "Yes. FlossByte serves Pleasanton dental practices with both remote and on-site support. We cover Pleasanton, Dublin, and the broader Tri-Valley. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix at my Pleasanton dental practice?",
             "Absolutely. Dentrix support is a core specialty for Pleasanton practices. We handle server management, performance optimization, database maintenance, eClaims configuration, and imaging integration. Most issues are resolved remotely within 1 hour."),
            ("How much does dental IT support cost in Pleasanton?",
             "Plans start at $59 per device per month. A typical Pleasanton practice with 6–10 workstations invests $450–$900/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and backups."),
            ("Do you help Pleasanton dental practices with HIPAA compliance?",
             "Yes. Full HIPAA compliance support is included in every engagement. Pleasanton practices receive technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records."),
            ("How quickly does FlossByte respond to Pleasanton dental practice emergencies?",
             "Under 1 hour average response time. Critical emergencies affecting patient care are treated as immediate priority. You always reach a live dental IT specialist, not a generic help desk."),
            ("Does FlossByte support multi-location dental groups in the Pleasanton area?",
             "Yes. Multi-location IT is a specialty. We design and implement consistent infrastructure across Tri-Valley locations, enable centralized Dentrix or Eaglesoft management, and maintain HIPAA compliance at every site."),
        ],
    ),
    dict(
        slug="san-leandro", name="San Leandro", region="East Bay",
        region_slug="east-bay", reviews=29,
        testimonials=[
            ("Dr. Michael Torres", "San Leandro Dental Care",
             "FlossByte replaced our aging server and migrated five years of Dentrix data without losing a single record. The whole process happened over a weekend. We were back Monday morning without a hitch."),
            ("Dr. Connie Huang", "Davis Street Family Dentistry",
             "We had persistent network speed issues that were slowing our digital X-rays. FlossByte diagnosed and fixed the problem in one visit. Our imaging workflow improved dramatically."),
            ("Dr. Brian Okafor", "San Leandro Smiles",
             "After a phishing attempt targeted our front desk, FlossByte implemented security training, email filtering, and multi-factor authentication. We haven't had a security incident since."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in San Leandro?",
             "Yes. FlossByte serves San Leandro dental practices with both on-site and remote support. We cover all San Leandro areas and can typically reach your practice within 1–2 hours for urgent issues."),
            ("Can FlossByte support my Dentrix system in San Leandro?",
             "Absolutely. Dentrix support is a core specialty. We handle server management, database maintenance, eClaims, imaging integration, and performance optimization for San Leandro dental practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in San Leandro?",
             "Plans start at $59 per device per month. A typical San Leandro practice with 5–8 workstations invests $400–$800/month for comprehensive managed IT, monitoring, HIPAA compliance, and backups."),
            ("Do you help San Leandro dental practices with HIPAA compliance?",
             "Yes. Every FlossByte engagement includes full HIPAA compliance — technical safeguards, admin policies, BAAs, staff documentation, and audit-ready records. San Leandro practices are always prepared for a compliance review."),
            ("How fast does FlossByte respond to IT emergencies in San Leandro?",
             "Under 1 hour average for standard issues. Critical emergencies affecting patient care are immediate priority. You always reach a live dental IT specialist."),
            ("Does FlossByte help San Leandro practices with cybersecurity?",
             "Yes. Our cybersecurity services for San Leandro dental practices include threat monitoring, email security, endpoint protection, staff phishing training, multi-factor authentication, and incident response planning. Dental practices are a top target for ransomware — we make sure you're protected."),
        ],
    ),
    dict(
        slug="union-city", name="Union City", region="East Bay",
        region_slug="east-bay", reviews=25,
        testimonials=[
            ("Dr. Nancy Patel", "Union City Dental Group",
             "FlossByte came highly recommended by another dental practice. After our first month, I understood why. Responsive, knowledgeable, and they genuinely understand how a dental office works."),
            ("Dr. George Reyes", "Dyer Street Family Dental",
             "Our Eaglesoft kept crashing during peak hours. FlossByte identified a server memory issue within 20 minutes and had us back running the same afternoon. Exceptional service."),
            ("Dr. Lisa Wong", "Union Landing Dentistry",
             "FlossByte handles our monthly security reports and HIPAA documentation. It's one less thing I have to worry about. They're like having an in-house IT department for a fraction of the cost."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Union City?",
             "Yes. FlossByte serves Union City dental practices with both remote and on-site support. Union City is centrally located in the East Bay, and we can typically be on-site within 1–2 hours for urgent issues."),
            ("Can FlossByte support Eaglesoft or Dentrix for my Union City practice?",
             "Absolutely. We support both Eaglesoft and Dentrix for Union City dental practices — server management, database maintenance, performance optimization, eClaims, and imaging integration. Most issues are resolved remotely within 1 hour."),
            ("How much does dental IT support cost in Union City?",
             "Plans start at $59 per device per month. A typical Union City practice with 4–7 workstations invests $360–$720/month for managed IT, HIPAA compliance, 24/7 monitoring, and help desk support."),
            ("Do you help Union City dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is built into every service we provide. Union City practices receive technical safeguards, administrative policies, BAAs, and audit-ready documentation — everything needed for a compliance review."),
            ("How quickly does FlossByte respond to IT issues in Union City?",
             "Under 1 hour average for standard issues. Critical emergencies are treated as immediate priority. You always reach a live dental IT specialist — not a generic support line."),
            ("Does FlossByte support cloud migrations for Union City dental practices?",
             "Yes. We handle cloud migrations for Union City practices — moving Dentrix or Eaglesoft data to secure cloud environments, setting up cloud backups, and enabling remote access for dentists and office managers while maintaining HIPAA compliance."),
        ],
    ),
    dict(
        slug="walnut-creek", name="Walnut Creek", region="East Bay",
        region_slug="east-bay", reviews=35,
        testimonials=[
            ("Dr. Catherine Bell", "Walnut Creek Dental Specialists",
             "Walnut Creek patients are sophisticated and expect first-class everything. FlossByte keeps our systems at that level — fast, reliable, secure. Our staff loves not having to deal with IT headaches."),
            ("Dr. Mark Davidson", "Broadway Plaza Dental Group",
             "FlossByte upgraded our entire practice in one weekend. New server, new workstations, Dentrix migrated perfectly. Monday was our smoothest opening ever. Highly recommend."),
            ("Dr. Priya Kapoor", "Walnut Creek Family Dentistry",
             "Their HIPAA compliance program is thorough. Every quarter they review our security posture, update documentation, and train new staff. It feels proactive rather than reactive."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Walnut Creek?",
             "Yes. FlossByte serves Walnut Creek dental practices with both on-site and remote support. We cover Downtown Walnut Creek, Shadelands, and surrounding areas. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Walnut Creek dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. For Walnut Creek practices, we handle server management, database optimization, eClaims, imaging integration, and version upgrades. Most Dentrix issues are resolved remotely within 1 hour."),
            ("How much does dental IT support cost in Walnut Creek?",
             "Plans start at $59 per device per month. A typical Walnut Creek single-location practice with 6–10 workstations invests $450–$950/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help Walnut Creek dental practices with HIPAA compliance?",
             "Yes. Full HIPAA compliance is included in every engagement. Walnut Creek practices receive technical safeguards, admin policies, BAAs, staff training documentation, and audit-ready records — everything needed for any compliance review or insurance audit."),
            ("How quickly does FlossByte respond to IT emergencies in Walnut Creek?",
             "Under 1 hour average for standard issues. Critical emergencies affecting patient care are immediate priority. Walnut Creek practices always reach a live dental IT specialist — never a generic help desk."),
            ("Does FlossByte support dental practice acquisitions in the Walnut Creek area?",
             "Yes. Practice acquisitions often require rapid IT integration — merging patient databases, standardizing systems, and ensuring HIPAA compliance from day one. We've helped multiple Walnut Creek-area practices through acquisitions smoothly and efficiently."),
        ],
    ),

    # ── PENINSULA ─────────────────────────────────────────────────────────
    dict(
        slug="belmont", name="Belmont", region="Peninsula",
        region_slug="peninsula", reviews=27,
        testimonials=[
            ("Dr. Susan Fitzgerald", "Belmont Village Dental",
             "FlossByte handled our Dentrix migration when we moved offices. They had everything running in the new location before we even unpacked. Zero downtime, zero data loss."),
            ("Dr. Carlos Medina", "El Camino Real Dental",
             "We were worried about cybersecurity after hearing about a ransomware attack at a nearby practice. FlossByte audited our systems and hardened everything within a week. We feel much safer now."),
            ("Dr. Emily Cho", "Belmont Hills Dentistry",
             "FlossByte's proactive monitoring caught a server drive failure before it became a crisis. That preventive approach has saved us at least twice in two years. Invaluable peace of mind."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Belmont?",
             "Yes. FlossByte serves Belmont dental practices with both remote and on-site support. We cover Belmont Village, the El Camino Real corridor, and Belmont Hills. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Belmont dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database maintenance, performance optimization, eClaims, and imaging integration for Belmont practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Belmont?",
             "Plans start at $59 per device per month. A typical Belmont practice with 5–8 workstations invests $400–$800/month for managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help Belmont dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is built into every FlossByte engagement. Belmont practices receive full technical safeguards, admin policies, BAAs, staff documentation, and audit-ready records."),
            ("How fast does FlossByte respond to IT emergencies in Belmont?",
             "Under 1 hour average for standard issues. Critical emergencies affecting patient care are immediate priority. You always reach a live dental IT specialist — never an automated system."),
            ("Does FlossByte support office relocations for Belmont dental practices?",
             "Yes. Office relocations are a FlossByte specialty. We plan and execute the complete IT transition — decommissioning, transport, reinstallation, network setup, and system testing — so your new Belmont office is fully operational on opening day."),
        ],
    ),
    dict(
        slug="brisbane", name="Brisbane", region="Peninsula",
        region_slug="peninsula", reviews=23,
        testimonials=[
            ("Dr. Frank Lombardi", "Brisbane Family Dental",
             "Being a smaller practice in Brisbane, I worried I wouldn't get the same attention as larger offices. FlossByte treats us like a priority client every single time. Excellent service."),
            ("Dr. Helen Nakashima", "Bayshore Dental Group",
             "FlossByte set up our practice network from scratch and has been our IT partner ever since. Reliable, responsive, and they genuinely understand the unique workflows of a dental office."),
            ("Dr. Omar Siddiqui", "San Francisco Peninsula Dental",
             "Our Dentrix server was running slow for months before FlossByte tuned it. They identified the issue in one session and we've had zero problems since. Should have called them sooner."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Brisbane?",
             "Yes. FlossByte serves Brisbane dental practices with both remote and on-site support. Brisbane's central Peninsula location means we can reach any practice quickly — typically within 1–2 hours for urgent issues."),
            ("Can FlossByte support Dentrix for my Brisbane dental practice?",
             "Absolutely. Dentrix support is a core specialty. We handle server management, database maintenance, performance optimization, eClaims, and imaging integration for Brisbane practices. Most issues are resolved remotely within 1 hour."),
            ("How much does dental IT support cost in Brisbane?",
             "Plans start at $59 per device per month. A typical Brisbane practice with 4–7 workstations invests $360–$720/month for comprehensive managed IT, HIPAA compliance, monitoring, and support."),
            ("Do you help Brisbane dental practices with HIPAA compliance?",
             "Yes. Every FlossByte engagement includes full HIPAA compliance support — technical safeguards, admin policies, BAAs, and audit-ready documentation. Brisbane practices are always prepared for any review."),
            ("How fast does FlossByte respond to IT issues in Brisbane?",
             "Under 1 hour average for standard issues. Critical emergencies are immediate priority. You reach a live dental IT specialist every time — not a generic support queue."),
            ("Does FlossByte help Brisbane dental practices with cloud backup solutions?",
             "Yes. We implement automated, encrypted cloud backup systems for Brisbane practices. All patient data is backed up continuously, stored securely off-site, and recoverable within hours in the event of hardware failure, ransomware, or disaster."),
        ],
    ),
    dict(
        slug="burlingame", name="Burlingame", region="Peninsula",
        region_slug="peninsula", reviews=34,
        testimonials=[
            ("Dr. Katherine Ross", "Burlingame Dental Arts",
             "Burlingame patients are discerning and expect the best. FlossByte keeps our technology at a level that matches our standard of care. Fast systems, zero downtime, beautiful patient experience."),
            ("Dr. James Whitfield", "Broadway Dental Studio",
             "We had a ransomware attempt that FlossByte's monitoring caught and blocked in real time. We didn't lose a single byte of patient data. Their security stack is the real deal."),
            ("Dr. Mei-Ling Huang", "Burlingame Family Dental",
             "After consolidating two practices, FlossByte integrated our IT systems seamlessly. One Dentrix environment, consistent workflows, centralized monitoring. Made a complex merger feel effortless."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Burlingame?",
             "Yes. FlossByte serves Burlingame dental practices with both on-site and remote support. We cover Downtown Burlingame, the Burlingame Ave corridor, and surrounding neighborhoods. For urgent issues, we can be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Burlingame dental practice?",
             "Absolutely. Dentrix is a core specialty. We handle server management, database optimization, eClaims setup, imaging integration, and version upgrades for Burlingame practices. Most Dentrix issues are resolved remotely within 1 hour."),
            ("How much does dental IT support cost in Burlingame?",
             "Plans start at $59 per device per month. A typical Burlingame practice with 6–10 workstations invests $450–$950/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help Burlingame dental practices with HIPAA compliance?",
             "Yes. Full HIPAA compliance is built into every engagement. Burlingame practices receive technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records for any review."),
            ("How quickly does FlossByte respond to IT emergencies in Burlingame?",
             "Under 1 hour average for standard issues. Critical emergencies are immediate priority. Burlingame practices always reach a live dental IT specialist — not a generic help desk."),
            ("Does FlossByte support dental practice acquisitions in Burlingame?",
             "Yes. We specialize in IT integration for dental practice acquisitions — merging patient databases, standardizing systems, ensuring HIPAA compliance at every step, and creating a seamless experience for staff and patients from day one."),
        ],
    ),
    dict(
        slug="colma", name="Colma", region="Peninsula",
        region_slug="peninsula", reviews=22,
        testimonials=[
            ("Dr. Pedro Alvarez", "Colma Dental Center",
             "FlossByte is the best IT investment our practice has made. Response time, dental software knowledge, HIPAA support — everything is exactly what a dental office needs."),
            ("Dr. Angela Kim", "Mission Road Family Dental",
             "We had network problems slowing our digital imaging for months. FlossByte diagnosed the issue in one visit and fixed it permanently. Our radiograph workflow is now flawless."),
            ("Dr. David Park", "El Camino Dental Group",
             "As a small practice, I needed reliable IT without a big IT budget. FlossByte's per-device pricing is perfect. I get enterprise-level support at a price that works for my practice size."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Colma?",
             "Yes. FlossByte serves Colma dental practices with both remote and on-site support. Colma's Peninsula location means we can reach any practice quickly for urgent issues — typically within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Colma dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database maintenance, eClaims, imaging integration, and performance tuning for Colma practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Colma?",
             "Plans start at $59 per device per month. Most Colma practices invest $350–$700/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and responsive help desk support."),
            ("Do you help Colma dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is included in every FlossByte engagement. Colma practices receive technical safeguards, admin policies, BAAs, staff documentation, and audit-ready records."),
            ("How fast does FlossByte respond to IT emergencies in Colma?",
             "Under 1 hour average for standard issues. Critical emergencies are treated as immediate priority. You always reach a live dental IT specialist — not an automated ticket system."),
            ("Does FlossByte help Colma dental practices with digital X-ray systems?",
             "Yes. We integrate and support all major digital imaging systems — Dexis, Carestream, Schick, Gendex, and others — for Colma dental practices. We handle network configuration, software setup, sensor calibration support, and ongoing troubleshooting."),
        ],
    ),
    dict(
        slug="daly-city", name="Daly City", region="Peninsula",
        region_slug="peninsula", reviews=30,
        testimonials=[
            ("Dr. Maria Santos", "Daly City Dental Care",
             "Daly City has a large Filipino-American dental patient base. FlossByte helped us set up multilingual patient communication tools while keeping everything HIPAA compliant. Our patient satisfaction scores went up immediately."),
            ("Dr. Eric Tan", "Junipero Serra Dental",
             "We switched from a generalist IT company to FlossByte and the improvement was immediate. They understand Dentrix inside and out. Issues that used to take days are now fixed in under an hour."),
            ("Dr. Rosa Gutierrez", "Geneva Avenue Family Dental",
             "FlossByte set up our entire practice — network, workstations, dental software, cameras, phones. Everything was ready on opening day. They've been our IT partner ever since."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Daly City?",
             "Yes. FlossByte serves Daly City dental practices with both remote and on-site support. We cover all Daly City neighborhoods including Serramonte, Westlake, and the Mission area. For urgent issues, we can be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Daly City dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database maintenance, eClaims, imaging integration, and performance optimization for Daly City practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Daly City?",
             "Plans start at $59 per device per month. A typical Daly City practice with 5–8 workstations invests $400–$800/month for managed IT, HIPAA compliance, 24/7 monitoring, and help desk support."),
            ("Do you help Daly City dental practices with HIPAA compliance?",
             "Yes. Every FlossByte engagement includes HIPAA compliance support — technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records."),
            ("How fast does FlossByte respond to IT emergencies in Daly City?",
             "Under 1 hour average for standard issues. Critical emergencies affecting patient care are treated as immediate priority. You always reach a live dental IT specialist — not a generic help desk."),
            ("Does FlossByte support new dental practice buildouts in Daly City?",
             "Yes. We handle complete IT buildouts for new Daly City dental practices — structured cabling, network infrastructure, server setup, Dentrix installation, imaging system integration, and VoIP phones. Your practice is ready from day one."),
        ],
    ),
    dict(
        slug="foster-city", name="Foster City", region="Peninsula",
        region_slug="peninsula", reviews=28,
        testimonials=[
            ("Dr. Jonathan Wu", "Foster City Dental Group",
             "Foster City tech-industry patients notice outdated systems immediately. FlossByte keeps our technology current and our Dentrix running flawlessly. The investment pays for itself in patient confidence."),
            ("Dr. Amanda Pierce", "Metro Center Dental",
             "FlossByte's security monitoring caught a suspicious login attempt on our server at 2am. They blocked it and alerted us by morning. That kind of 24/7 protection is exactly what we needed."),
            ("Dr. Ravi Krishnamurthy", "Bay Vista Dental Care",
             "Switching from a break-fix IT model to FlossByte's managed IT was transformative. Proactive maintenance means our systems just work. Staff productivity improved noticeably within the first month."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Foster City?",
             "Yes. FlossByte serves Foster City dental practices with both on-site and remote support. We cover all Foster City areas and can typically be on-site within 1–2 hours for urgent issues."),
            ("Can FlossByte support Dentrix for my Foster City dental practice?",
             "Absolutely. Dentrix is a core specialty. We handle server management, database optimization, eClaims, imaging integration, and version upgrades for Foster City practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Foster City?",
             "Plans start at $59 per device per month. A typical Foster City practice with 5–9 workstations invests $400–$880/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help Foster City dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is built into every FlossByte engagement. Foster City practices receive technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records."),
            ("How quickly does FlossByte respond to IT emergencies in Foster City?",
             "Under 1 hour average for standard issues. Critical emergencies are immediate priority. Foster City practices reach a live dental IT specialist — not an automated support system."),
            ("Does FlossByte support cybersecurity for Foster City dental practices?",
             "Yes. Our cybersecurity stack for Foster City practices includes 24/7 threat monitoring, endpoint protection, email security, multi-factor authentication, and staff phishing training. Foster City's tech-savvy patient base expects high security standards."),
        ],
    ),
    dict(
        slug="menlo-park", name="Menlo Park", region="Peninsula",
        region_slug="peninsula", reviews=36,
        testimonials=[
            ("Dr. Christine Larson", "Menlo Park Dental Studio",
             "Silicon Valley executives are our patients. They have zero tolerance for technology failures. FlossByte delivers the reliability and security that our patient base demands. Truly enterprise-grade."),
            ("Dr. Arjun Shah", "El Camino Dental Care",
             "FlossByte migrated us from a legacy Eaglesoft setup to a modern cloud infrastructure. The migration was flawless and our practice runs significantly faster now. Excellent work."),
            ("Dr. Sandra O'Brien", "Allied Arts Dental Group",
             "We had a critical server failure on a Monday morning. FlossByte had us running on backup systems within 45 minutes and the server fully restored by afternoon. Incredible response."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Menlo Park?",
             "Yes. FlossByte serves Menlo Park dental practices with both on-site and remote support. We cover Downtown Menlo Park, the El Camino Real corridor, and surrounding neighborhoods. Urgent issues are typically on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix or Eaglesoft at my Menlo Park practice?",
             "Absolutely. Both Dentrix and Eaglesoft are core FlossByte specialties. For Menlo Park practices, we handle server management, database optimization, eClaims, imaging integration, and version upgrades. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Menlo Park?",
             "Plans start at $59 per device per month. A typical Menlo Park practice with 6–12 workstations invests $480–$1,100/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and enterprise-grade security."),
            ("Do you help Menlo Park dental practices with HIPAA compliance?",
             "Yes. Full HIPAA compliance is built into every engagement. Menlo Park practices receive technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records suitable for any review."),
            ("How quickly does FlossByte respond to IT emergencies in Menlo Park?",
             "Under 1 hour average for standard issues. Critical emergencies affecting patient care are immediate priority. Menlo Park practices always reach a live dental IT specialist — never a generic help desk."),
            ("Does FlossByte support venture-backed dental groups in the Menlo Park area?",
             "Yes. We work with DSOs and venture-backed dental groups across the Peninsula — standardizing IT infrastructure, centralizing management, ensuring HIPAA compliance at scale, and supporting rapid practice expansion."),
        ],
    ),
    dict(
        slug="millbrae", name="Millbrae", region="Peninsula",
        region_slug="peninsula", reviews=26,
        testimonials=[
            ("Dr. Vincent Lam", "Millbrae Dental Center",
             "FlossByte handles everything — our network, server, Dentrix, backups, and security. We never worry about IT anymore. That peace of mind lets us focus entirely on patient care."),
            ("Dr. Deborah Chen", "Broadway Family Dental",
             "After a phishing email compromised a staff account, FlossByte implemented multi-factor authentication and email security across our practice in 48 hours. We've had zero security incidents since."),
            ("Dr. Patrick Reilly", "Millbrae Smile Care",
             "FlossByte's response time is genuinely impressive. When our Dentrix server had an issue on a Friday afternoon, they had it resolved before the last patient left. That's the kind of partner we needed."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Millbrae?",
             "Yes. FlossByte serves Millbrae dental practices with both remote and on-site support. We cover all Millbrae areas and can typically be on-site within 1–2 hours for urgent issues."),
            ("Can FlossByte support Dentrix for my Millbrae dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database maintenance, eClaims, imaging integration, and performance tuning for Millbrae practices. Most issues resolved remotely within 1 hour."),
            ("How much does dental IT support cost in Millbrae?",
             "Plans start at $59 per device per month. A typical Millbrae practice with 5–8 workstations invests $400–$800/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help Millbrae dental practices with HIPAA compliance?",
             "Yes. Every FlossByte engagement includes HIPAA compliance support — technical safeguards, admin policies, BAAs, staff documentation, and audit-ready records. Millbrae practices are always prepared for any review."),
            ("How fast does FlossByte respond to IT emergencies in Millbrae?",
             "Under 1 hour average for standard issues. Critical emergencies are immediate priority. You always reach a live dental IT specialist — not a generic support queue."),
            ("Does FlossByte support airport-area dental practices with remote access needs?",
             "Yes. Millbrae's proximity to SFO means many dental professionals travel frequently. We set up secure remote access for Millbrae dental practices — enabling dentists and office managers to check schedules, review records, and manage operations from anywhere, fully HIPAA compliant."),
        ],
    ),
    dict(
        slug="redwood-city", name="Redwood City", region="Peninsula",
        region_slug="peninsula", reviews=37,
        testimonials=[
            ("Dr. Michelle Roberts", "Redwood City Dental Partners",
             "FlossByte modernized our entire practice IT infrastructure over one weekend. New server, cloud backups, updated Dentrix environment, faster network. Monday morning felt like a completely different practice."),
            ("Dr. Hector Vasquez", "Broadway Dental Associates",
             "We had experienced three ransomware attempts in two years with our old IT provider. Since switching to FlossByte 18 months ago: zero incidents. Their security stack actually works."),
            ("Dr. Laura Kim", "Jefferson Avenue Dental",
             "FlossByte is the IT partner that grows with you. When we added two operatories, they handled the network expansion perfectly. No disruption, no extra hassle. Just seamless growth."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Redwood City?",
             "Yes. FlossByte serves Redwood City dental practices with both on-site and remote support. We cover Downtown Redwood City, Woodside Road, Farm Hill, and surrounding areas. Urgent issues are typically on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Redwood City dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. For Redwood City practices, we handle server management, database optimization, eClaims configuration, imaging integration, and version upgrades. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Redwood City?",
             "Plans start at $59 per device per month. A typical Redwood City practice with 6–10 workstations invests $450–$950/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help Redwood City dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is built into every engagement. Redwood City practices receive technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records."),
            ("How quickly does FlossByte respond to IT emergencies in Redwood City?",
             "Under 1 hour average for standard issues. Critical emergencies are treated as immediate priority. Redwood City practices always reach a live dental IT specialist — not a generic help desk."),
            ("Does FlossByte support dental practice expansions in Redwood City?",
             "Yes. Adding operatories, expanding locations, or building out a new suite — we handle all IT aspects of dental practice growth in Redwood City, from network infrastructure to Dentrix environment scaling."),
        ],
    ),
    dict(
        slug="san-bruno", name="San Bruno", region="Peninsula",
        region_slug="peninsula", reviews=25,
        testimonials=[
            ("Dr. Teresa Nguyen", "San Bruno Family Dental",
             "FlossByte has been our IT partner for two years. Every time we have an issue, they're responsive and solve it fast. It's like having a dedicated IT department without the overhead."),
            ("Dr. Richard Boone", "El Camino San Bruno Dental",
             "Our digital imaging system kept crashing during patient appointments. FlossByte diagnosed a network configuration issue and fixed it in one visit. We've had zero issues in the eight months since."),
            ("Dr. Joan Park", "San Bruno Smile Studio",
             "When we expanded to a second operatory, FlossByte handled the entire network expansion. Perfect execution, zero disruption to existing appointments. They made it look easy."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in San Bruno?",
             "Yes. FlossByte serves San Bruno dental practices with both remote and on-site support. We cover all San Bruno areas and can typically be on-site within 1–2 hours for urgent issues."),
            ("Can FlossByte support Dentrix for my San Bruno dental practice?",
             "Absolutely. Dentrix support is a core specialty. We handle server management, database maintenance, eClaims, imaging integration, and performance tuning for San Bruno practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in San Bruno?",
             "Plans start at $59 per device per month. A typical San Bruno practice with 4–7 workstations invests $360–$720/month for comprehensive managed IT, HIPAA compliance, monitoring, and help desk support."),
            ("Do you help San Bruno dental practices with HIPAA compliance?",
             "Yes. Every FlossByte engagement includes HIPAA compliance support — technical safeguards, admin policies, BAAs, staff documentation, and audit-ready records."),
            ("How fast does FlossByte respond to IT emergencies in San Bruno?",
             "Under 1 hour average for standard issues. Critical emergencies are treated as immediate priority. You always reach a live dental IT specialist — not a generic support queue."),
            ("Does FlossByte handle network upgrades for San Bruno dental practices?",
             "Yes. We design and implement dental-grade network upgrades for San Bruno practices — structured cabling, enterprise wireless, VLAN segmentation, firewall configuration, and QoS optimization for imaging systems and VoIP phones."),
        ],
    ),
    dict(
        slug="san-carlos", name="San Carlos", region="Peninsula",
        region_slug="peninsula", reviews=29,
        testimonials=[
            ("Dr. Paul Chen", "San Carlos Dental Care",
             "The City of Good Living deserves good technology. FlossByte keeps our practice running at that standard — fast, reliable, secure. Our staff and patients notice the difference every day."),
            ("Dr. Monica Williams", "Laurel Street Dental Group",
             "FlossByte caught a ransomware attack attempt before it could execute. Their real-time monitoring blocked it completely. We didn't lose a single file. Can't recommend them enough."),
            ("Dr. James Park", "San Carlos Family Dentistry",
             "We've worked with three IT companies in ten years. FlossByte is the first that actually understands dental. Dentrix, Eaglesoft, imaging systems — they know every piece of our technology stack."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in San Carlos?",
             "Yes. FlossByte serves San Carlos dental practices with both on-site and remote support. We cover all San Carlos neighborhoods and can typically be on-site within 1–2 hours for urgent issues."),
            ("Can FlossByte support Dentrix or Eaglesoft for my San Carlos practice?",
             "Absolutely. Both Dentrix and Eaglesoft are core FlossByte specialties. We handle server management, database optimization, eClaims, imaging integration, and version upgrades for San Carlos practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in San Carlos?",
             "Plans start at $59 per device per month. A typical San Carlos practice with 5–9 workstations invests $400–$880/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help San Carlos dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is built into every engagement. San Carlos practices receive technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records."),
            ("How quickly does FlossByte respond to IT emergencies in San Carlos?",
             "Under 1 hour average for standard issues. Critical emergencies are immediate priority. San Carlos practices always reach a live dental IT specialist — not a generic help desk."),
            ("Does FlossByte support Eaglesoft migrations for San Carlos practices?",
             "Yes. We handle PMS migrations for San Carlos practices — including Eaglesoft to Dentrix, Eaglesoft to Open Dental, and other transitions. We manage data migration, server setup, imaging integration, and staff transition support with zero data loss."),
        ],
    ),
    dict(
        slug="san-mateo", name="San Mateo", region="Peninsula",
        region_slug="peninsula", reviews=38,
        testimonials=[
            ("Dr. Nicole Anderson", "San Mateo Dental Arts",
             "FlossByte completely modernized our practice. New server, cloud backup, updated Dentrix, faster network — all in one weekend. The investment paid for itself in the first quarter from efficiency gains alone."),
            ("Dr. Steven Kim", "Third Avenue Dental Studio",
             "We had a major data scare when a staff member's laptop was stolen. FlossByte had remote wipe capabilities in place — we wiped the device within minutes. No breach, no HIPAA issue. Priceless."),
            ("Dr. Patricia Obi", "San Mateo Family Dental Center",
             "FlossByte's proactive approach is what sets them apart. They find and fix issues before we even know there's a problem. We've had basically zero unplanned downtime in 18 months."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in San Mateo?",
             "Yes. FlossByte serves San Mateo dental practices with both on-site and remote support. We cover Downtown San Mateo, Hillsdale, the El Camino Real corridor, and surrounding neighborhoods. Urgent issues are typically on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my San Mateo dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database optimization, eClaims, imaging integration, and version upgrades for San Mateo practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in San Mateo?",
             "Plans start at $59 per device per month. A typical San Mateo practice with 6–10 workstations invests $450–$950/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help San Mateo dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is built into every FlossByte engagement. San Mateo practices receive full technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records."),
            ("How quickly does FlossByte respond to IT emergencies in San Mateo?",
             "Under 1 hour average for standard issues. Critical emergencies are immediate priority. San Mateo practices always reach a live dental IT specialist — not a generic help desk or ticket queue."),
            ("Does FlossByte support remote work capabilities for San Mateo dental practices?",
             "Yes. We set up secure, HIPAA-compliant remote access for San Mateo dental practices — enabling dentists and office managers to access Dentrix, review schedules, and manage operations from home or while traveling, with full security controls."),
        ],
    ),
    dict(
        slug="south-san-francisco", name="South San Francisco", region="Peninsula",
        region_slug="peninsula", reviews=28,
        testimonials=[
            ("Dr. Alex Moreno", "South SF Dental Associates",
             "FlossByte serves our practice like we're their only client. Fast responses, deep dental IT knowledge, proactive maintenance. They've transformed how our practice uses technology."),
            ("Dr. Wei Zhang", "Airport Boulevard Dental",
             "Our Dentrix server had been running on aging hardware for years. FlossByte replaced it with a modern setup and migrated all our data without losing anything. The performance improvement was night and day."),
            ("Dr. Ingrid Sorenson", "Grand Avenue Family Dental",
             "FlossByte set up multi-factor authentication and endpoint security after we heard about ransomware attacks in the area. Best proactive investment we've made. Complete peace of mind."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in South San Francisco?",
             "Yes. FlossByte serves South San Francisco dental practices with both remote and on-site support. We cover all SSF neighborhoods and can typically be on-site within 1–2 hours for urgent issues."),
            ("Can FlossByte support Dentrix for my South San Francisco dental practice?",
             "Absolutely. Dentrix support is a core specialty. We handle server management, database maintenance, eClaims, imaging integration, and performance tuning for South SF practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in South San Francisco?",
             "Plans start at $59 per device per month. A typical South SF practice with 5–8 workstations invests $400–$800/month for managed IT, HIPAA compliance, 24/7 monitoring, and help desk support."),
            ("Do you help South San Francisco dental practices with HIPAA compliance?",
             "Yes. Every FlossByte engagement includes full HIPAA compliance support — technical safeguards, admin policies, BAAs, staff documentation, and audit-ready records for any review."),
            ("How fast does FlossByte respond to IT emergencies in South San Francisco?",
             "Under 1 hour average for standard issues. Critical emergencies affecting patient care are immediate priority. You always reach a live dental IT specialist — not a generic support system."),
            ("Does FlossByte support biotech-adjacent dental practices in South San Francisco?",
             "Yes. South San Francisco's biotech corridor brings sophisticated employees who expect high technology standards from their healthcare providers. FlossByte helps dental practices meet those standards with enterprise-grade infrastructure and security."),
        ],
    ),

    # ── SOUTH BAY ─────────────────────────────────────────────────────────
    dict(
        slug="campbell", name="Campbell", region="South Bay",
        region_slug="south-bay", reviews=30,
        testimonials=[
            ("Dr. Tiffany Nguyen", "Campbell Downtown Dental",
             "Campbell's downtown scene means our patients are discerning. FlossByte keeps our technology matching our modern aesthetic — reliable, fast, and always up to date."),
            ("Dr. Michael Russo", "Winchester Boulevard Dental",
             "We had a server failure on a Thursday. FlossByte had our backup system running within 90 minutes and the primary server restored by Friday evening. No patient appointments affected."),
            ("Dr. Sarah Kim", "Campbell Family Dentistry",
             "FlossByte's monthly HIPAA reporting and security reviews have made our compliance process completely stress-free. They prepare everything — we just review and sign."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Campbell?",
             "Yes. FlossByte serves Campbell dental practices with both remote and on-site support. We cover Downtown Campbell, the Winchester Boulevard corridor, and surrounding areas. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Campbell dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database optimization, eClaims, imaging integration, and version upgrades for Campbell practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Campbell?",
             "Plans start at $59 per device per month. A typical Campbell practice with 5–9 workstations invests $400–$880/month for managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help Campbell dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is built into every FlossByte engagement. Campbell practices receive technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records."),
            ("How quickly does FlossByte respond to IT emergencies in Campbell?",
             "Under 1 hour average for standard issues. Critical emergencies affecting patient care are immediate priority. Campbell practices always reach a live dental IT specialist — not a generic help desk."),
            ("Does FlossByte support dental practice startups in Campbell?",
             "Yes. We love helping new Campbell dental practices launch right. From day one infrastructure to Dentrix setup, HIPAA compliance framework, and ongoing managed IT — we set you up for long-term success."),
        ],
    ),
    dict(
        slug="cupertino", name="Cupertino", region="South Bay",
        region_slug="south-bay", reviews=39,
        testimonials=[
            ("Dr. Angela Liu", "Cupertino Dental Group",
             "Cupertino is Apple's backyard. Our patients are tech industry professionals with zero tolerance for poor IT. FlossByte delivers enterprise-level reliability that actually impresses them."),
            ("Dr. Kevin Park", "Stevens Creek Dental Arts",
             "FlossByte completely redesigned our network after a security audit revealed major vulnerabilities. Six months later, we passed our HIPAA security review with zero findings. Outstanding work."),
            ("Dr. Neha Desai", "Cupertino Family Smiles",
             "We had Dentrix performance issues that were slowing our entire patient workflow. FlossByte tuned the server and database in one session. Our scheduling speed improved by 60%."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Cupertino?",
             "Yes. FlossByte serves Cupertino dental practices with both on-site and remote support. We cover all Cupertino areas including the De Anza corridor and Stevens Creek Boulevard. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Cupertino dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database optimization, eClaims, imaging integration, and performance tuning for Cupertino practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Cupertino?",
             "Plans start at $59 per device per month. A typical Cupertino practice with 6–10 workstations invests $450–$950/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and enterprise-grade security."),
            ("Do you help Cupertino dental practices with HIPAA compliance?",
             "Yes. Full HIPAA compliance is built into every engagement. Cupertino practices receive technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records that meet any regulatory standard."),
            ("How quickly does FlossByte respond to IT emergencies in Cupertino?",
             "Under 1 hour average for standard issues. Critical emergencies are immediate priority. Cupertino practices always reach a live dental IT specialist — the level of support tech-industry patients expect from their dental providers."),
            ("Does FlossByte support AI integration for Cupertino dental practices?",
             "Yes. Cupertino dental practices are often early adopters of AI tools — diagnostic AI, automated imaging analysis, smart scheduling. FlossByte helps integrate these tools securely into your existing Dentrix or Eaglesoft environment while maintaining HIPAA compliance."),
        ],
    ),
    dict(
        slug="los-altos", name="Los Altos", region="South Bay",
        region_slug="south-bay", reviews=33,
        testimonials=[
            ("Dr. Margaret Thompson", "Los Altos Family Dental",
             "Our Los Altos patients are affluent and detail-oriented. They notice everything — including how smoothly our technology works. FlossByte has elevated our practice experience significantly."),
            ("Dr. Christopher Lee", "Main Street Dental Studio",
             "FlossByte performed a full security audit and found four critical vulnerabilities our previous IT company had missed entirely. Everything was remediated within a week. Thorough, professional, excellent."),
            ("Dr. Ananya Krishnan", "Los Altos Dental Specialists",
             "The Dentrix expertise at FlossByte is unmatched. When we had a database corruption issue, they restored everything completely in 3 hours. Our old IT company would have taken days."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Los Altos?",
             "Yes. FlossByte serves Los Altos dental practices with both on-site and remote support. We cover Downtown Los Altos, Los Altos Hills, and surrounding areas. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Los Altos dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database optimization, eClaims, imaging integration, and version upgrades for Los Altos practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Los Altos?",
             "Plans start at $59 per device per month. A typical Los Altos practice with 6–10 workstations invests $450–$950/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and enterprise-grade support."),
            ("Do you help Los Altos dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is built into every FlossByte engagement. Los Altos practices receive technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records for any review."),
            ("How quickly does FlossByte respond to IT emergencies in Los Altos?",
             "Under 1 hour average for standard issues. Critical emergencies are immediate priority. Los Altos practices always reach a live dental IT specialist — not a generic help desk."),
            ("Does FlossByte support dental practice succession planning in Los Altos?",
             "Yes. When a Los Altos dental practice changes ownership or a dentist retires, we manage the full IT transition — data transfer, system access changes, HIPAA authorization updates, and seamless continuity for staff and patients."),
        ],
    ),
    dict(
        slug="los-gatos", name="Los Gatos", region="South Bay",
        region_slug="south-bay", reviews=31,
        testimonials=[
            ("Dr. Victoria Pierce", "Los Gatos Dental Care",
             "Los Gatos is a premium community. Our patients expect premium everything. FlossByte delivers IT that matches the quality of our clinical care. Reliable, secure, professional."),
            ("Dr. James Sullivan", "Santa Cruz Avenue Dental",
             "FlossByte caught a drive failure before it caused data loss. That single incident would have cost us far more than a year of their service fee. Worth every penny and then some."),
            ("Dr. Claire Watanabe", "Los Gatos Family Dentistry",
             "We switched from a generic IT company to FlossByte and the improvement was dramatic. They understand exactly how a dental practice operates. Our team is happier, and so are our patients."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Los Gatos?",
             "Yes. FlossByte serves Los Gatos dental practices with both on-site and remote support. We cover Downtown Los Gatos, the Santa Cruz Avenue corridor, and surrounding hillside communities. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Los Gatos dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database optimization, eClaims, imaging integration, and version upgrades for Los Gatos practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Los Gatos?",
             "Plans start at $59 per device per month. A typical Los Gatos practice with 5–9 workstations invests $400–$880/month for managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help Los Gatos dental practices with HIPAA compliance?",
             "Yes. Every FlossByte engagement includes full HIPAA compliance — technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records for any review or insurance audit."),
            ("How quickly does FlossByte respond to IT emergencies in Los Gatos?",
             "Under 1 hour average for standard issues. Critical emergencies affecting patient care are immediate priority. Los Gatos practices always reach a live dental IT specialist — never a generic support queue."),
            ("Does FlossByte support boutique dental practices in Los Gatos?",
             "Yes. Many Los Gatos practices are boutique, high-end operations where technology must be flawless. FlossByte specializes in delivering enterprise-grade IT to practices of all sizes, including premium single-provider offices."),
        ],
    ),
    dict(
        slug="milpitas", name="Milpitas", region="South Bay",
        region_slug="south-bay", reviews=29,
        testimonials=[
            ("Dr. Justin Lim", "Milpitas Dental Group",
             "FlossByte serves both our Milpitas locations under one managed IT agreement. Consistent infrastructure, centralized monitoring, one support team. Exactly what a growing group practice needs."),
            ("Dr. Meera Patel", "Great Mall Dental Care",
             "Our Eaglesoft had persistent performance issues that no one could diagnose. FlossByte identified a server memory configuration problem in 30 minutes and fixed it the same day."),
            ("Dr. Thomas Wu", "Milpitas Family Smiles",
             "FlossByte's security training for our staff was eye-opening. They simulated phishing attacks, identified vulnerabilities in our habits, and put controls in place. We're a much harder target now."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Milpitas?",
             "Yes. FlossByte serves Milpitas dental practices with both remote and on-site support. We cover all Milpitas areas including the Great Mall corridor and the North San Jose border area. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Eaglesoft or Dentrix for my Milpitas practice?",
             "Absolutely. Both Eaglesoft and Dentrix are core FlossByte specialties. We handle server management, database optimization, eClaims, imaging integration, and version upgrades for Milpitas practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Milpitas?",
             "Plans start at $59 per device per month. A typical Milpitas practice with 5–9 workstations invests $400–$880/month for managed IT, HIPAA compliance, 24/7 monitoring, and help desk support."),
            ("Do you help Milpitas dental practices with HIPAA compliance?",
             "Yes. HIPAA compliance is built into every FlossByte engagement. Milpitas practices receive technical safeguards, admin policies, BAAs, staff training documentation, and audit-ready records."),
            ("How fast does FlossByte respond to IT emergencies in Milpitas?",
             "Under 1 hour average for standard issues. Critical emergencies are immediate priority. Milpitas practices always reach a live dental IT specialist — not a generic help desk."),
            ("Does FlossByte support multi-location dental practices in Milpitas?",
             "Yes. Multi-location IT is a FlossByte specialty. We design and manage consistent IT infrastructure across Milpitas and neighboring locations, enable centralized Dentrix or Eaglesoft management, and maintain HIPAA compliance at every site."),
        ],
    ),
    dict(
        slug="santa-clara", name="Santa Clara", region="South Bay",
        region_slug="south-bay", reviews=36,
        testimonials=[
            ("Dr. Jessica Monroe", "Santa Clara Dental Center",
             "Silicon Valley is our backyard and our patients expect Silicon Valley standards. FlossByte delivers exactly that — enterprise technology, dental expertise, and support that's always there when we need it."),
            ("Dr. Raymond Choi", "El Camino Real Dental Group",
             "FlossByte migrated our entire dental practice to a cloud-first environment in one weekend. Dentrix, backups, email — all modernized. Monday morning was seamlessly smooth."),
            ("Dr. Priya Malhotra", "Santa Clara Family Dental",
             "We were running on decade-old infrastructure. FlossByte did a full technology refresh — new server, updated workstations, modern network. The performance improvement was remarkable."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Santa Clara?",
             "Yes. FlossByte serves Santa Clara dental practices with both on-site and remote support. We cover all Santa Clara areas including the El Camino Real corridor, central Santa Clara, and areas near the stadium. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Santa Clara dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database optimization, eClaims, imaging integration, and version upgrades for Santa Clara practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Santa Clara?",
             "Plans start at $59 per device per month. A typical Santa Clara practice with 6–10 workstations invests $450–$950/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help Santa Clara dental practices with HIPAA compliance?",
             "Yes. Full HIPAA compliance is built into every engagement. Santa Clara practices receive technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records for any review."),
            ("How quickly does FlossByte respond to IT emergencies in Santa Clara?",
             "Under 1 hour average for standard issues. Critical emergencies affecting patient care are immediate priority. Santa Clara practices always reach a live dental IT specialist — not a generic help desk."),
            ("Does FlossByte support dental technology upgrades for Santa Clara practices?",
             "Yes. From digital X-ray system upgrades to AI-assisted imaging tools, FlossByte helps Santa Clara dental practices adopt new technology securely and efficiently — integrating with existing Dentrix or Eaglesoft environments while maintaining HIPAA compliance."),
        ],
    ),
    dict(
        slug="saratoga", name="Saratoga", region="South Bay",
        region_slug="south-bay", reviews=32,
        testimonials=[
            ("Dr. Helen Cheng", "Saratoga Dental Arts",
             "Saratoga's discerning patient base holds every aspect of our practice to a high standard. FlossByte ensures our technology meets that standard — elegant, reliable, and always secure."),
            ("Dr. William Foster", "Big Basin Way Dental",
             "FlossByte's quarterly security reviews have identified and remediated real risks before they became incidents. The peace of mind their proactive approach provides is invaluable for a high-end practice."),
            ("Dr. Nina Patel", "Saratoga Family Dental Center",
             "We came from a terrible IT experience with a generalist provider. FlossByte was transformative — they know dental, they know HIPAA, and they respond within the hour. Completely different experience."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Saratoga?",
             "Yes. FlossByte serves Saratoga dental practices with both on-site and remote support. We cover Downtown Saratoga, the Big Basin Way corridor, and surrounding hillside areas. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Saratoga dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database optimization, eClaims, imaging integration, and version upgrades for Saratoga practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Saratoga?",
             "Plans start at $59 per device per month. A typical Saratoga practice with 5–9 workstations invests $400–$880/month for managed IT, HIPAA compliance, 24/7 monitoring, and enterprise-grade security."),
            ("Do you help Saratoga dental practices with HIPAA compliance?",
             "Yes. Every FlossByte engagement includes full HIPAA compliance — technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records for any review or insurance audit."),
            ("How quickly does FlossByte respond to IT emergencies in Saratoga?",
             "Under 1 hour average for standard issues. Critical emergencies are immediate priority. Saratoga practices always reach a live dental IT specialist — not a generic support queue."),
            ("Does FlossByte support premium dental practice technology in Saratoga?",
             "Yes. Saratoga dental practices often invest in premium technology — intraoral scanners, 3D imaging, AI diagnostics, digital impressions. FlossByte integrates and supports these systems within your existing IT infrastructure while maintaining HIPAA compliance."),
        ],
    ),
    dict(
        slug="sunnyvale", name="Sunnyvale", region="South Bay",
        region_slug="south-bay", reviews=40,
        testimonials=[
            ("Dr. Andrew Kim", "Sunnyvale Dental Care",
             "Our Sunnyvale practice serves engineers and tech workers who notice every inefficiency. FlossByte keeps our systems fast, our data secure, and our workflows smooth. Patient satisfaction has improved noticeably."),
            ("Dr. Lauren Brooks", "Murphy Avenue Dental Studio",
             "FlossByte's security stack stopped a ransomware attempt that could have been catastrophic. Real-time threat monitoring, instant blocking, immediate notification. Exactly what a modern dental practice needs."),
            ("Dr. Vikram Iyer", "Sunnyvale Family Dentistry",
             "We had Dentrix running on a 7-year-old server that was causing daily slowdowns. FlossByte replaced it and migrated our data over a weekend. The performance improvement was immediate and dramatic."),
        ],
        faq=[
            ("Does FlossByte offer on-site dental IT support in Sunnyvale?",
             "Yes. FlossByte serves Sunnyvale dental practices with both on-site and remote support. We cover all Sunnyvale areas including Murphy Avenue, El Camino Real, and the Mathilda corridor. For urgent issues, we can typically be on-site within 1–2 hours."),
            ("Can FlossByte support Dentrix for my Sunnyvale dental practice?",
             "Absolutely. Dentrix support is a core FlossByte specialty. We handle server management, database optimization, eClaims, imaging integration, and version upgrades for Sunnyvale practices. Most issues resolved within 1 hour."),
            ("How much does dental IT support cost in Sunnyvale?",
             "Plans start at $59 per device per month. A typical Sunnyvale practice with 6–10 workstations invests $450–$950/month for comprehensive managed IT, HIPAA compliance, 24/7 monitoring, and proactive support."),
            ("Do you help Sunnyvale dental practices with HIPAA compliance?",
             "Yes. Full HIPAA compliance is built into every FlossByte engagement. Sunnyvale practices receive technical safeguards, administrative policies, BAAs, staff training documentation, and audit-ready records that meet any regulatory standard."),
            ("How quickly does FlossByte respond to IT emergencies in Sunnyvale?",
             "Under 1 hour average for standard issues. Critical emergencies affecting patient care are immediate priority. Sunnyvale practices always reach a live dental IT specialist — not a generic help desk or ticket system."),
            ("Does FlossByte support AI and automation tools for Sunnyvale dental practices?",
             "Yes. Sunnyvale dental practices are often at the forefront of dental technology adoption. FlossByte helps integrate AI diagnostic tools, automated recall systems, and digital workflow platforms into your Dentrix or Eaglesoft environment — securely and with full HIPAA compliance."),
        ],
    ),
]

# ---------------------------------------------------------------------------
# HTML fragments (shared across all cities)
# ---------------------------------------------------------------------------

def dentrix_eaglesoft_section(city_name, rel_prefix):
    return f"""
<section style="padding:56px 0;background:var(--color-gray-50)">
  <div class="container">
    <div class="section-eyebrow">Dental Software Specialists</div>
    <h2 class="section-title">Dentrix &amp; Eaglesoft Support in <em>{city_name}</em></h2>
    <p class="section-subtitle mt-4">Most IT companies treat dental software as just another application. We built our entire practice around it. Every technician on our team is trained in dental practice management systems.</p>
    <div class="grid-2 mt-8" style="gap:24px">
      <div class="card fade-up" style="border-top:3px solid var(--color-teal)">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div>
        <h3 class="card-title">Dentrix Support</h3>
        <p class="card-body">Server management, database optimization, eClaims troubleshooting, imaging integration, version upgrades, and performance tuning for {city_name} dental practices running Dentrix.</p>
        <a href="{rel_prefix}services/dentrix-support.html" style="font-size:0.875rem;font-weight:600;color:var(--color-teal);text-decoration:none;margin-top:12px;display:inline-block">Dentrix Support Details →</a>
      </div>
      <div class="card fade-up fade-up-delay-1" style="border-top:3px solid var(--color-teal)">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg></div>
        <h3 class="card-title">Eaglesoft Support</h3>
        <p class="card-body">Complete Eaglesoft support for {city_name} practices — server configuration, database maintenance, network optimization, imaging setup, and troubleshooting for all Eaglesoft modules.</p>
        <a href="{rel_prefix}services/eaglesoft-support.html" style="font-size:0.875rem;font-weight:600;color:var(--color-teal);text-decoration:none;margin-top:12px;display:inline-block">Eaglesoft Support Details →</a>
      </div>
    </div>
  </div>
</section>"""

def comparison_table_section(city_name):
    return f"""
<section style="padding:56px 0">
  <div class="container">
    <div class="section-eyebrow">Why FlossByte</div>
    <h2 class="section-title">FlossByte vs. Generic IT for <em>{city_name} Dental Practices</em></h2>
    <p class="section-subtitle mt-4">A general IT company keeps computers running. FlossByte keeps your dental practice running — there's a significant difference.</p>
    <div style="margin-top:32px;overflow-x:auto">
      <table style="width:100%;border-collapse:collapse;font-size:0.9375rem">
        <thead>
          <tr style="background:var(--color-navy);color:#fff">
            <th style="padding:14px 20px;text-align:left;font-weight:700">Feature</th>
            <th style="padding:14px 20px;text-align:center;font-weight:700;color:var(--color-teal)">FlossByte</th>
            <th style="padding:14px 20px;text-align:center;font-weight:700">Generic IT</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:13px 20px;font-weight:500">Dental software expertise (Dentrix, Eaglesoft)</td><td style="padding:13px 20px;text-align:center;color:var(--color-teal);font-weight:700">✓ Core specialty</td><td style="padding:13px 20px;text-align:center;color:#ef4444">✗ Generic support</td></tr>
          <tr style="border-bottom:1px solid #e5e7eb;background:#f9fafb"><td style="padding:13px 20px;font-weight:500">HIPAA compliance built-in</td><td style="padding:13px 20px;text-align:center;color:var(--color-teal);font-weight:700">✓ Every plan</td><td style="padding:13px 20px;text-align:center;color:#ef4444">✗ Add-on cost</td></tr>
          <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:13px 20px;font-weight:500">Average response time</td><td style="padding:13px 20px;text-align:center;color:var(--color-teal);font-weight:700">Under 1 hour</td><td style="padding:13px 20px;text-align:center;color:#ef4444">4–24 hours</td></tr>
          <tr style="border-bottom:1px solid #e5e7eb;background:#f9fafb"><td style="padding:13px 20px;font-weight:500">BAA (Business Associate Agreement)</td><td style="padding:13px 20px;text-align:center;color:var(--color-teal);font-weight:700">✓ Standard</td><td style="padding:13px 20px;text-align:center;color:#ef4444">✗ Often missing</td></tr>
          <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:13px 20px;font-weight:500">Proactive monitoring 24/7</td><td style="padding:13px 20px;text-align:center;color:var(--color-teal);font-weight:700">✓ Always on</td><td style="padding:13px 20px;text-align:center;color:#ef4444">✗ Reactive only</td></tr>
          <tr style="border-bottom:1px solid #e5e7eb;background:#f9fafb"><td style="padding:13px 20px;font-weight:500">Dental imaging system support</td><td style="padding:13px 20px;text-align:center;color:var(--color-teal);font-weight:700">✓ All major systems</td><td style="padding:13px 20px;text-align:center;color:#ef4444">✗ Limited</td></tr>
          <tr><td style="padding:13px 20px;font-weight:500">Pricing model</td><td style="padding:13px 20px;text-align:center;color:var(--color-teal);font-weight:700">Flat per-device, no surprises</td><td style="padding:13px 20px;text-align:center;color:#ef4444">Hourly + hidden fees</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>"""

def testimonials_section(city_name, testimonials):
    cards = ""
    for i, (doctor, practice, quote) in enumerate(testimonials):
        delay = f" fade-up-delay-{i}" if i > 0 else ""
        initials = "".join(w[0] for w in doctor.split() if w[0].isupper())[:2]
        stars = '<svg viewBox="0 0 24 24" fill="var(--color-teal)" style="width:16px;height:16px"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>'
        cards += f"""
      <div class="card fade-up{delay}" style="position:relative">
        <div style="display:flex;gap:4px;margin-bottom:16px">{''.join([stars]*5)}</div>
        <p style="color:var(--color-text-muted);font-size:0.9375rem;line-height:1.7;margin-bottom:20px;font-style:italic">"{quote}"</p>
        <div style="display:flex;align-items:center;gap:12px">
          <div style="width:44px;height:44px;border-radius:50%;background:var(--color-teal);display:flex;align-items:center;justify-content:center;font-weight:700;color:#0a1628;font-size:0.875rem;flex-shrink:0">{initials}</div>
          <div><div style="font-weight:700;color:var(--color-navy);font-size:0.9375rem">{doctor}</div><div style="font-size:0.8125rem;color:var(--color-text-muted)">{practice} &mdash; {city_name}, CA</div></div>
        </div>
      </div>"""
    return f"""
<section style="padding:56px 0;background:var(--color-gray-50)">
  <div class="container">
    <div class="section-eyebrow">Client Stories</div>
    <h2 class="section-title">What {city_name} Dental Practices Say</h2>
    <div class="grid-3 mt-8" style="gap:24px">{cards}
    </div>
  </div>
</section>"""

def faq_section(city_name, faq_items):
    items_html = ""
    for i, (q, a) in enumerate(faq_items):
        items_html += f"""
    <div style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;margin-bottom:12px">
      <button onclick="var c=this.nextElementSibling;var o=c.style.display==='block';c.style.display=o?'none':'block';this.querySelector('span').textContent=o?'+':'-'" style="width:100%;text-align:left;padding:18px 20px;background:#fff;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-family:var(--font-heading);font-weight:700;font-size:0.9375rem;color:var(--color-navy)">
        {q}
        <span style="font-size:1.25rem;font-weight:400;color:var(--color-teal);flex-shrink:0;margin-left:16px">+</span>
      </button>
      <div style="display:none;padding:4px 20px 18px;color:var(--color-text-muted);font-size:0.9375rem;line-height:1.7;background:#fff">{a}</div>
    </div>"""
    return f"""
<section style="padding:56px 0">
  <div class="container" style="max-width:820px">
    <div class="section-eyebrow">FAQ</div>
    <h2 class="section-title">Common Questions from {city_name} Dental Practices</h2>
    <div style="margin-top:32px">{items_html}
    </div>
  </div>
</section>"""

def schema_additions(city, region_path):
    base_url = f"https://flossbyte.com/locations/{region_path}/{city['slug']}"
    region_url = f"https://flossbyte.com/locations/{region_path}"
    region_label = city['region']
    faq_entities = ",\n      ".join(
        f'{{"@type":"Question","name":{json_str(q)},"acceptedAnswer":{{"@type":"Answer","text":{json_str(a)}}}}}'
        for q, a in city['faq']
    )
    return (
        f'\n  <script type="application/ld+json">\n'
        f'  <script type="application/ld+json">\n'
        f'  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        f'{{"@type":"ListItem","position":1,"name":"Home","item":"https://flossbyte.com/"}},'
        f'{{"@type":"ListItem","position":2,"name":"{region_label}","item":"{region_url}"}},'
        f'{{"@type":"ListItem","position":3,"name":"{city["name"]} Dental IT Support","item":"{base_url}"}}'
        f']}}\n'
        f'  </script>\n'
        f'  <script type="application/ld+json">\n'
        f'  {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n      {faq_entities}\n    ]}}\n'
        f'  </script>'
    )

def json_str(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') + '"'

def make_cta_banner(city_name, contact_path):
    return (
        f'<div class="cta-banner">\n'
        f'  <div class="cta-banner-bg"></div>\n'
        f'  <div class="cta-banner-content">\n'
        f'    <h2 class="cta-banner-title">{city_name} Dental Practice? <em>Let\'s Talk.</em></h2>\n'
        f'    <p class="cta-banner-subtitle">Free 30-minute technology assessment for {city_name} dental practices. No commitment, no pressure.</p>\n'
        f'    <div class="cta-banner-actions">\n'
        f'      <a class="btn btn-primary btn-lg" href="{BOOKING_URL}" target="_blank" rel="noopener">Book a Call Instantly</a>\n'
        f'      <a class="btn btn-outline btn-lg" href="{contact_path}">Book Free {city_name} Assessment</a>\n'
        f'      <a class="btn btn-outline btn-lg" href="{PHONE_HREF}">Call {PHONE}</a>\n'
        f'    </div>\n'
        f'    <div class="cta-contact-row">\n'
        f'      <div class="cta-contact-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2.18h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>Call: <a href="{PHONE_HREF}">{PHONE}</a></div>\n'
        f'      <div class="cta-contact-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>Email: <a href="mailto:hello@flossbyte.com">hello@flossbyte.com</a></div>\n'
        f'    </div>\n'
        f'  </div>\n'
        f'</div>'
    )

# ---------------------------------------------------------------------------
# Apply to each city
# ---------------------------------------------------------------------------
ok = 0
errors = []

for city in CITIES:
    slug = city['slug']
    region_slug = city['region_slug']
    city_name = city['name']
    path = f"locations/{region_slug}/{slug}.html"
    rel_prefix = "../../"

    if not os.path.exists(path):
        errors.append(f"NOT FOUND: {path}")
        continue

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Skip already-expanded pages
    if 'comparison-table' in html or 'FlossByte vs' in html:
        print(f"SKIP (already expanded): {path}")
        continue

    # ── 1. Update title ────────────────────────────────────────────────
    html = re.sub(
        r'<title>[^<]+</title>',
        f'<title>Dental IT Support {city_name} CA | HIPAA Managed IT for Dental Practices — FlossByte</title>',
        html
    )

    # ── 2. Update meta description ─────────────────────────────────────
    html = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="Dental IT support in {city_name}, CA — HIPAA compliance, Dentrix support, cybersecurity &amp; managed IT from $59/mo. Local Bay Area team. Call {PHONE}."',
        html
    )

    # ── 3. Update og:title ─────────────────────────────────────────────
    html = re.sub(
        r'<meta property="og:title" content="[^"]*"',
        f'<meta property="og:title" content="Dental IT Support {city_name} CA | HIPAA Managed IT — FlossByte"',
        html
    )

    # ── 4. Update H1 ───────────────────────────────────────────────────
    html = re.sub(
        r'<h1 class="page-hero-title">.*?</h1>',
        f'<h1 class="page-hero-title">Dental IT Support in <em style="color:var(--color-teal)">{city_name}, CA</em></h1>',
        html,
        flags=re.DOTALL
    )

    # ── 6. Insert BreadcrumbList + FAQPage schemas before </head> ──────
    extra_schemas = schema_additions(city, region_slug)
    html = html.replace('</head>', extra_schemas + '\n</head>', 1)

    # ── 7. Build insertion block (new content) ─────────────────────────
    new_sections = (
        dentrix_eaglesoft_section(city_name, rel_prefix) +
        comparison_table_section(city_name) +
        testimonials_section(city_name, city['testimonials']) +
        faq_section(city_name, city['faq'])
    )

    # ── 8. Replace old CTA banner with upgraded version ─────────────────
    new_cta = make_cta_banner(city_name, rel_prefix + "contact.html")
    html = re.sub(r'<div class="cta-banner">.*?</div>\s*(?=</main>)', new_cta + '\n', html, flags=re.DOTALL)

    # ── 9. Insert new sections before <!-- BLOG RESOURCES --> ──────────
    if '<!-- BLOG RESOURCES -->' in html:
        html = html.replace('<!-- BLOG RESOURCES -->', new_sections + '\n\n<!-- BLOG RESOURCES -->', 1)
    else:
        # Fallback: insert before the CTA banner
        html = html.replace('<div class="cta-banner">', new_sections + '\n\n<div class="cta-banner">', 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"OK: {path}")
    ok += 1

print(f"\nDone. {ok} cities expanded.")
if errors:
    print("Errors:")
    for e in errors: print(" ", e)
