const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType,
  ShadingType, PageNumber, PageBreak, LevelFormat
} = require("docx");

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };
const cellMargins = { top: 80, bottom: 80, left: 120, right: 120 };

function headerCell(text, width) {
  return new TableCell({
    borders,
    width: { size: width, type: WidthType.DXA },
    shading: { fill: "1B4D6E", type: ShadingType.CLEAR },
    margins: cellMargins,
    verticalAlign: "center",
    children: [new Paragraph({ children: [new TextRun({ text, bold: true, color: "FFFFFF", font: "Arial", size: 20 })] })]
  });
}

function cell(text, width, opts = {}) {
  const runs = [];
  if (opts.bold) {
    runs.push(new TextRun({ text, bold: true, font: "Arial", size: 20, color: opts.color || "333333" }));
  } else {
    runs.push(new TextRun({ text, font: "Arial", size: 20, color: opts.color || "333333" }));
  }
  return new TableCell({
    borders,
    width: { size: width, type: WidthType.DXA },
    shading: opts.fill ? { fill: opts.fill, type: ShadingType.CLEAR } : undefined,
    margins: cellMargins,
    children: [new Paragraph({ children: runs })]
  });
}

function heading1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 360, after: 200 },
    children: [new TextRun({ text, bold: true, font: "Arial", size: 36, color: "1B4D6E" })]
  });
}

function heading2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 160 },
    children: [new TextRun({ text, bold: true, font: "Arial", size: 28, color: "2E86AB" })]
  });
}

function heading3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 200, after: 120 },
    children: [new TextRun({ text, bold: true, font: "Arial", size: 24, color: "444444" })]
  });
}

function para(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 120 },
    children: [new TextRun({ text, font: "Arial", size: 22, color: opts.color || "333333", bold: opts.bold || false, italics: opts.italics || false })]
  });
}

function richPara(runs) {
  return new Paragraph({
    spacing: { after: 120 },
    children: runs.map(r => new TextRun({ font: "Arial", size: 22, color: "333333", ...r }))
  });
}

function bulletItem(text, level = 0) {
  return new Paragraph({
    numbering: { reference: "bullets", level },
    spacing: { after: 60 },
    children: [new TextRun({ text, font: "Arial", size: 22, color: "333333" })]
  });
}

function richBullet(runs, level = 0) {
  return new Paragraph({
    numbering: { reference: "bullets", level },
    spacing: { after: 60 },
    children: runs.map(r => new TextRun({ font: "Arial", size: 22, color: "333333", ...r }))
  });
}

function emptyLine() {
  return new Paragraph({ spacing: { after: 80 }, children: [] });
}

// Build the document
const doc = new Document({
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [
          { level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } },
          { level: 1, format: LevelFormat.BULLET, text: "\u25E6", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1440, hanging: 360 } } } },
        ]
      },
      {
        reference: "numbers",
        levels: [
          { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } },
        ]
      }
    ]
  },
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 36, bold: true, font: "Arial", color: "1B4D6E" }, paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 28, bold: true, font: "Arial", color: "2E86AB" }, paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 24, bold: true, font: "Arial", color: "444444" }, paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 2 } },
    ]
  },
  sections: [
    // ======= COVER PAGE =======
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
        }
      },
      children: [
        emptyLine(), emptyLine(), emptyLine(), emptyLine(), emptyLine(), emptyLine(),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 200 },
          children: [new TextRun({ text: "FLOSSBYTE", font: "Arial", size: 56, bold: true, color: "1B4D6E" })]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 400 },
          children: [new TextRun({ text: "SEO Audit & Keyword Research Report", font: "Arial", size: 36, color: "2E86AB" })]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 100 },
          children: [new TextRun({ text: "Comprehensive Website Analysis", font: "Arial", size: 24, color: "666666" })]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 100 },
          children: [new TextRun({ text: "March 25, 2026", font: "Arial", size: 24, color: "666666" })]
        }),
        emptyLine(), emptyLine(), emptyLine(), emptyLine(), emptyLine(), emptyLine(),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 60 },
          border: { top: { style: BorderStyle.SINGLE, size: 2, color: "1B4D6E", space: 10 } },
          children: [new TextRun({ text: "Overall SEO Health Score", font: "Arial", size: 22, color: "666666" })]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 60 },
          children: [new TextRun({ text: "88 / 100", font: "Arial", size: 52, bold: true, color: "2E86AB" })]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Technical: 95  |  Content: 85  |  Meta & Social: 82  |  Linking: 87", font: "Arial", size: 20, color: "888888" })
          ]
        }),
      ]
    },

    // ======= MAIN CONTENT =======
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
        }
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            alignment: AlignmentType.RIGHT,
            children: [new TextRun({ text: "FlossByte SEO Audit Report  |  March 2026", font: "Arial", size: 16, color: "999999", italics: true })]
          })]
        })
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({ text: "Page ", font: "Arial", size: 16, color: "999999" }),
              new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 16, color: "999999" })
            ]
          })]
        })
      },
      children: [
        // === SECTION 1: REMAINING ISSUES ===
        heading1("1. Remaining SEO Issues"),
        para("All critical and medium issues from the previous audit have been fixed. Below are the remaining items organized by priority."),

        // HIGH PRIORITY TABLE
        heading2("High Priority"),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [500, 3800, 2560, 2500],
          rows: [
            new TableRow({ children: [headerCell("#", 500), headerCell("Issue", 3800), headerCell("Files Affected", 2560), headerCell("Fix", 2500)] }),
            new TableRow({ children: [cell("1", 500), cell("Homepage meta description too long (244 chars, ideal 150-160)", 3800), cell("index.html", 2560), cell("Trim to ~155 chars", 2500)] }),
            new TableRow({ children: [cell("2", 500), cell("36 city page meta descriptions too long (194-197 chars)", 3800), cell("All locations/*/*.html", 2560), cell("Trim each to ~155 chars", 2500)] }),
            new TableRow({ children: [cell("3", 500), cell("Logo images massively oversized (342-350KB each, should be <50KB)", 3800), cell("assets/ folder", 2560), cell("Compress or convert to SVG", 2500)] }),
            new TableRow({ children: [cell("4", 500), cell("CSS/JS not minified - index.css (39KB), components.js (28KB)", 3800), cell("Root files", 2560), cell("Minify for 20-30% savings", 2500)] }),
            new TableRow({ children: [cell("5", 500), cell("Google Fonts loaded via @import (render-blocking)", 3800), cell("index.css line 1", 2560), cell("Switch to <link rel=\"preload\"> + font-display: swap", 2500)] }),
          ]
        }),

        emptyLine(),
        heading2("Medium Priority"),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [500, 3800, 2560, 2500],
          rows: [
            new TableRow({ children: [headerCell("#", 500), headerCell("Issue", 3800), headerCell("Files Affected", 2560), headerCell("Fix", 2500)] }),
            new TableRow({ children: [cell("6", 500), cell("Blog index missing JSON-LD schema", 3800), cell("blog/index.html", 2560), cell("Add CollectionPage schema", 2500)] }),
            new TableRow({ children: [cell("7", 500), cell("City pages borderline thin content (400-500 words)", 3800), cell("36 city pages", 2560), cell("Expand with local context", 2500)] }),
            new TableRow({ children: [cell("8", 500), cell("Missing og:site_name on 8 core pages", 3800), cell("index, about, contact, services, pricing, faqs, hipaa, why-flossbyte", 2560), cell("Add og:site_name tag", 2500)] }),
            new TableRow({ children: [cell("9", 500), cell("Limited blog-to-location cross-linking", 3800), cell("Blog posts", 2560), cell("Add contextual links to location pages", 2500)] }),
          ]
        }),

        emptyLine(),
        heading2("Low Priority"),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [500, 5860, 3000],
          rows: [
            new TableRow({ children: [headerCell("#", 500), headerCell("Issue", 5860), headerCell("Fix", 3000)] }),
            new TableRow({ children: [cell("10", 500), cell("Missing explicit Twitter title/description/image tags (OG fallback works)", 5860), cell("Add if desired", 3000)] }),
            new TableRow({ children: [cell("11", 500), cell("External links (LinkedIn, Google Business) missing nofollow", 5860), cell("Add rel=\"nofollow\"", 3000)] }),
          ]
        }),

        // === SECTION 2: WHAT'S WORKING WELL ===
        new Paragraph({ children: [new PageBreak()] }),
        heading1("2. What's Working Well"),

        bulletItem("100% unique title tags and meta descriptions across 60 pages"),
        bulletItem("Perfect canonical URL implementation (HTTPS, absolute)"),
        bulletItem("Strong JSON-LD schema on 58/59 pages"),
        bulletItem("Clean URL structure with logical hierarchy"),
        bulletItem("Proper H1 > H2 > H3 heading hierarchy everywhere"),
        bulletItem("Solid mobile responsiveness with sticky CTA"),
        bulletItem("Clean robots.txt and complete sitemap.xml (59 URLs)"),
        bulletItem("Good redirect strategy (.htaccess + _redirects)"),
        bulletItem("Proper 404 page with noindex"),
        bulletItem("All OG + Twitter tags present on all 59 indexable pages"),
        bulletItem("Schema URL now correctly matches canonical on all location pages"),

        // === SECTION 3: COMPETITOR LANDSCAPE ===
        emptyLine(),
        heading1("3. Competitor Landscape"),

        para("FlossByte already appears on page 1 for \"dental IT support Bay Area\" via a blog post. The 39 location pages are a significant competitive advantage - most competitors only have 1-3 location pages.", { bold: true }),
        emptyLine(),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [2500, 1500, 5360],
          rows: [
            new TableRow({ children: [headerCell("Competitor", 2500), headerCell("Experience", 1500), headerCell("Key Strength", 5360)] }),
            new TableRow({ children: [cell("Pact-One Solutions", 2500), cell("20+ years", 1500), cell("Strong content, orthodontic niche pages, Bay Area presence", 5360)] }),
            new TableRow({ children: [cell("SRS Networks", 2500), cell("25+ years", 1500), cell("Established Bay Area dental IT, strong domain authority", 5360)] }),
            new TableRow({ children: [cell("Darkhorse Tech", 2500), cell("10+ years", 1500), cell("Controls \"best dental IT companies\" listicle rankings", 5360)] }),
            new TableRow({ children: [cell("Your IT Guys", 2500), cell("15+ years", 1500), cell("Individual pages for Dentrix, Eaglesoft, Open Dental", 5360)] }),
            new TableRow({ children: [cell("Veltec Networks", 2500), cell("15+ years", 1500), cell("Bay Area MSP with dental vertical focus", 5360)] }),
          ]
        }),

        emptyLine(),
        heading2("Competitor Gaps FlossByte Can Exploit"),
        bulletItem("Pact-One has orthodontic-specific pages; create specialty-specific pages"),
        bulletItem("Darkhorse controls \"best dental IT companies\" listicle; create comparison content"),
        bulletItem("No competitor has strong Bay Area-specific ransomware response content"),
        bulletItem("No competitor has dental IT cost/pricing transparency content"),
        bulletItem("No competitor targets \"switching IT provider\" keywords"),

        // === SECTION 4: KEYWORD RESEARCH ===
        new Paragraph({ children: [new PageBreak()] }),
        heading1("4. Keyword Research"),
        para("150+ keywords identified across 7 categories. Below are the highest-ROI opportunities organized by priority."),

        // 4.1 Software-Specific
        heading2("4.1 Software-Specific Keywords"),
        richPara([{ text: "Competition: ", bold: true }, { text: "LOW  |  " }, { text: "Intent: ", bold: true }, { text: "Transactional  |  " }, { text: "Priority: ", bold: true, color: "CC0000" }, { text: "MUST HAVE", bold: true, color: "CC0000" }]),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [3800, 1800, 3760],
          rows: [
            new TableRow({ children: [headerCell("Keyword", 3800), headerCell("Intent", 1800), headerCell("Target Page", 3760)] }),
            new TableRow({ children: [cell("Dentrix IT support", 3800), cell("Transactional", 1800), cell("NEW: /services/dentrix-support.html", 3760, { bold: true })] }),
            new TableRow({ children: [cell("Eaglesoft support near me", 3800), cell("Transactional", 1800), cell("NEW: /services/eaglesoft-support.html", 3760, { bold: true })] }),
            new TableRow({ children: [cell("Open Dental IT help", 3800), cell("Transactional", 1800), cell("NEW: /services/open-dental-support.html", 3760, { bold: true })] }),
            new TableRow({ children: [cell("Dentrix slow on network", 3800), cell("Problem-solving", 1800), cell("NEW blog post", 3760, { bold: true })] }),
            new TableRow({ children: [cell("Dentrix server requirements 2026", 3800), cell("Informational", 1800), cell("NEW blog post", 3760, { bold: true })] }),
            new TableRow({ children: [cell("Eaglesoft cloud migration", 3800), cell("Commercial", 1800), cell("NEW blog post", 3760, { bold: true })] }),
          ]
        }),

        // 4.2 Problem-Based
        emptyLine(),
        heading2("4.2 Problem-Based Keywords"),
        richPara([{ text: "Competition: ", bold: true }, { text: "LOW  |  " }, { text: "Intent: ", bold: true }, { text: "Transactional/Urgent  |  " }, { text: "Priority: ", bold: true, color: "CC0000" }, { text: "MUST HAVE", bold: true, color: "CC0000" }]),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [3800, 1800, 3760],
          rows: [
            new TableRow({ children: [headerCell("Keyword", 3800), headerCell("Intent", 1800), headerCell("Target Page", 3760)] }),
            new TableRow({ children: [cell("dental office ransomware attack", 3800), cell("Urgent", 1800), cell("NEW blog post", 3760, { bold: true })] }),
            new TableRow({ children: [cell("dental practice server crash", 3800), cell("Problem-solving", 1800), cell("Existing blog or new", 3760)] }),
            new TableRow({ children: [cell("HIPAA breach dental practice what to do", 3800), cell("Urgent", 1800), cell("NEW blog post", 3760, { bold: true })] }),
            new TableRow({ children: [cell("dental office network down", 3800), cell("Problem-solving", 1800), cell("Existing blog", 3760)] }),
            new TableRow({ children: [cell("Dentrix not connecting to server", 3800), cell("Problem-solving", 1800), cell("NEW blog post", 3760, { bold: true })] }),
          ]
        }),

        // 4.3 Location + Service
        emptyLine(),
        heading2("4.3 Location + Service Keywords"),
        richPara([{ text: "Competition: ", bold: true }, { text: "MEDIUM  |  " }, { text: "Intent: ", bold: true }, { text: "Commercial  |  " }, { text: "Priority: ", bold: true, color: "DD7700" }, { text: "SHOULD HAVE", bold: true, color: "DD7700" }]),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [3800, 1800, 3760],
          rows: [
            new TableRow({ children: [headerCell("Keyword", 3800), headerCell("Intent", 1800), headerCell("Target Page", 3760)] }),
            new TableRow({ children: [cell("dental IT support San Jose", 3800), cell("Commercial", 1800), cell("Existing city page (optimize)", 3760)] }),
            new TableRow({ children: [cell("HIPAA compliant IT San Francisco", 3800), cell("Commercial", 1800), cell("Existing city page", 3760)] }),
            new TableRow({ children: [cell("dental office cybersecurity Bay Area", 3800), cell("Commercial", 1800), cell("NEW service page", 3760, { bold: true })] }),
            new TableRow({ children: [cell("dental IT services near me", 3800), cell("Transactional", 1800), cell("Location pages (already targeting)", 3760)] }),
          ]
        }),

        // 4.4 Cost/Pricing
        new Paragraph({ children: [new PageBreak()] }),
        heading2("4.4 Cost/Pricing Keywords"),
        richPara([{ text: "Competition: ", bold: true }, { text: "LOW  |  " }, { text: "Intent: ", bold: true }, { text: "Commercial  |  " }, { text: "Priority: ", bold: true, color: "DD7700" }, { text: "SHOULD HAVE", bold: true, color: "DD7700" }]),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [3800, 1800, 3760],
          rows: [
            new TableRow({ children: [headerCell("Keyword", 3800), headerCell("Intent", 1800), headerCell("Target Page", 3760)] }),
            new TableRow({ children: [cell("dental IT support cost per month", 3800), cell("Commercial", 1800), cell("NEW blog post -> links to pricing", 3760, { bold: true })] }),
            new TableRow({ children: [cell("managed IT services dental pricing", 3800), cell("Commercial", 1800), cell("Existing pricing page (optimize)", 3760)] }),
            new TableRow({ children: [cell("how much does dental IT support cost", 3800), cell("Informational", 1800), cell("NEW blog post", 3760, { bold: true })] }),
          ]
        }),

        // 4.5 New Practice / Startup
        emptyLine(),
        heading2("4.5 New Practice / Startup Keywords"),
        richPara([{ text: "Competition: ", bold: true }, { text: "LOW  |  " }, { text: "Intent: ", bold: true }, { text: "Commercial  |  " }, { text: "Priority: ", bold: true, color: "DD7700" }, { text: "SHOULD HAVE", bold: true, color: "DD7700" }]),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [3800, 1800, 3760],
          rows: [
            new TableRow({ children: [headerCell("Keyword", 3800), headerCell("Intent", 1800), headerCell("Target Page", 3760)] }),
            new TableRow({ children: [cell("IT setup new dental practice", 3800), cell("Commercial", 1800), cell("NEW blog post or service page", 3760, { bold: true })] }),
            new TableRow({ children: [cell("dental office technology checklist", 3800), cell("Informational", 1800), cell("NEW blog post (lead magnet)", 3760, { bold: true })] }),
            new TableRow({ children: [cell("opening dental practice IT requirements", 3800), cell("Informational", 1800), cell("NEW blog post", 3760, { bold: true })] }),
          ]
        }),

        // 4.6 Switching/Comparison
        emptyLine(),
        heading2("4.6 Switching / Comparison Keywords"),
        richPara([{ text: "Competition: ", bold: true }, { text: "LOW  |  " }, { text: "Intent: ", bold: true }, { text: "Transactional  |  " }, { text: "Priority: ", bold: true, color: "2E86AB" }, { text: "NICE TO HAVE", bold: true, color: "2E86AB" }]),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [3800, 1800, 3760],
          rows: [
            new TableRow({ children: [headerCell("Keyword", 3800), headerCell("Intent", 1800), headerCell("Target Page", 3760)] }),
            new TableRow({ children: [cell("switch dental IT provider", 3800), cell("Transactional", 1800), cell("NEW blog post", 3760, { bold: true })] }),
            new TableRow({ children: [cell("dental IT vs general IT support", 3800), cell("Commercial", 1800), cell("Existing blog (already have similar)", 3760)] }),
            new TableRow({ children: [cell("signs you need better dental IT", 3800), cell("Informational", 1800), cell("NEW blog post", 3760, { bold: true })] }),
          ]
        }),

        // === SECTION 5: RECOMMENDED ACTION PLAN ===
        new Paragraph({ children: [new PageBreak()] }),
        heading1("5. Recommended Action Plan"),

        heading2("Immediate (This Week)"),
        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [500, 8860],
          rows: [
            new TableRow({ children: [headerCell("#", 500), headerCell("Task", 8860)] }),
            new TableRow({ children: [cell("1", 500), cell("Trim meta descriptions on homepage + 36 city pages to ~155 characters", 8860)] }),
            new TableRow({ children: [cell("2", 500), cell("Add og:site_name to 8 core pages (index, about, contact, services, pricing, faqs, hipaa, why-flossbyte)", 8860)] }),
            new TableRow({ children: [cell("3", 500), cell("Add CollectionPage JSON-LD schema to blog/index.html", 8860)] }),
            new TableRow({ children: [cell("4", 500), cell("Compress logo images from 350KB to <50KB each", 8860)] }),
          ]
        }),

        emptyLine(),
        heading2("Short-Term (Next 2 Weeks)"),
        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [500, 8860],
          rows: [
            new TableRow({ children: [headerCell("#", 500), headerCell("Task", 8860)] }),
            new TableRow({ children: [cell("5", 500), cell("Create 3 dedicated service pages: Dentrix Support, Eaglesoft Support, Open Dental Support", 8860)] }),
            new TableRow({ children: [cell("6", 500), cell("Write blog post: \"How Much Does Dental IT Support Cost?\"", 8860)] }),
            new TableRow({ children: [cell("7", 500), cell("Write blog post: \"Dental Office Ransomware: Prevention & Response Guide\"", 8860)] }),
            new TableRow({ children: [cell("8", 500), cell("Minify CSS/JS files and fix Google Fonts render-blocking loading", 8860)] }),
          ]
        }),

        emptyLine(),
        heading2("Medium-Term (Next Month)"),
        new Table({
          width: { size: 9360, type: WidthType.DXA },
          columnWidths: [500, 8860],
          rows: [
            new TableRow({ children: [headerCell("#", 500), headerCell("Task", 8860)] }),
            new TableRow({ children: [cell("9", 500), cell("Write blog post: \"IT Setup Guide for New Dental Practices\"", 8860)] }),
            new TableRow({ children: [cell("10", 500), cell("Write blog post: \"Dentrix Slow? Common Fixes for Dental Networks\"", 8860)] }),
            new TableRow({ children: [cell("11", 500), cell("Create dedicated cybersecurity service page", 8860)] }),
            new TableRow({ children: [cell("12", 500), cell("Expand city pages with unique local content (landmarks, dental associations, neighborhoods)", 8860)] }),
            new TableRow({ children: [cell("13", 500), cell("Improve blog-to-location page cross-linking with contextual anchor text", 8860)] }),
          ]
        }),

        // === SECTION 6: BIGGEST CONTENT GAPS ===
        emptyLine(),
        heading1("6. Biggest Content Gaps"),
        para("These are the most significant missing content pieces compared to competitors:"),

        richBullet([{ text: "No dedicated Dentrix/Eaglesoft/Open Dental pages", bold: true }, { text: " - competitors like Your IT Guys have individual pages for each software system, capturing high-intent searches" }]),
        richBullet([{ text: "No dedicated cybersecurity service page", bold: true }, { text: " - ransomware attacks on healthcare up 58% in 2025; this is a hot topic dentists actively search" }]),
        richBullet([{ text: "No data backup/disaster recovery service page", bold: true }, { text: " - this core service only exists as a blog post" }]),
        richBullet([{ text: "No \"new dental practice IT setup\" content", bold: true }, { text: " - Darkhorse Tech, Legend Networking, and Zenith all have this; captures high-value startup leads" }]),
        richBullet([{ text: "No dental IT cost/pricing blog post", bold: true }, { text: " - needed to support the pricing page and capture commercial-intent searches" }]),
        richBullet([{ text: "No \"switching IT provider\" content", bold: true }, { text: " - captures frustrated dental offices looking to leave bad providers" }]),

        emptyLine(), emptyLine(),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          border: { top: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC", space: 10 } },
          spacing: { before: 200 },
          children: [new TextRun({ text: "Report prepared for FlossByte  |  March 25, 2026", font: "Arial", size: 18, color: "999999", italics: true })]
        }),
      ]
    }
  ]
});

// Generate the file
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("C:\\Users\\Sarvbjeet\\Desktop\\flossbyteWeb\\website\\FlossByte-SEO-Audit-Report.docx", buffer);
  console.log("Document created: FlossByte-SEO-Audit-Report.docx");
});
