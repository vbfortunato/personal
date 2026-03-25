# Shopify Peptides Store Blueprint (Modeled on primalpharma.org)

## 1) Brand & Positioning
- **Working brand name:** Primal Peptides
- **Tagline:** *Perfection is expected*
- **Primary value props:**
  - Third-party lab results
  - Fast shipping thresholds
  - Bulk order discount tiers
  - Clean, science-forward product pages

## 2) Important Compliance First (US)
Before launch, confirm legal counsel review for:
- Federal + state requirements for peptide sales in your target markets.
- Marketing claims (avoid disease-treatment claims unless you have legal clearance).
- Payment processor and Shopify policy compatibility for your catalog.
- Required disclaimers and age-gating if applicable.

Recommended baseline pages:
- Terms of Service
- Privacy Policy
- Refund Policy
- Shipping Policy
- Contact page with business email and response SLA

## 3) Shopify Setup (Step-by-step)
1. Create Shopify account and choose a theme (Dawn is fine to start).
2. Configure **Settings → Markets** for countries you can legally ship to.
3. Configure **Settings → Shipping and delivery**:
   - Free shipping threshold (example: $150)
   - Carrier rates + delivery windows
4. Configure **Settings → Taxes and duties** based on nexus.
5. Configure **Settings → Payments** (Shopify Payments/third-party based on category approval).
6. Configure **Settings → Checkout**:
   - Customer contact method
   - Optional account login
   - Fraud filters / manual review rules
7. Install essential apps:
   - Product reviews
   - Upsells / bundles
   - Email + SMS (Klaviyo or Shopify Email)
   - Heatmaps/session replay (optional)

## 4) Site Architecture (based on the reference site structure)
Main navigation:
- Home
- Shop
- Lab Results
- Contact

Footer links:
- FAQ
- Shipping Policy
- Refund Policy
- Terms
- Privacy
- COA / Lab Verification

## 5) Homepage Wireframe
### Top announcement bars
- “20% OFF orders above $500”
- “Free shipping for orders above $150”
- “No order minimums”

### Hero section
- Headline: **Primal Peptides**
- Subheadline: **Perfection is expected**
- CTA: **Shop now**

### Trust blocks
- “Third-party tested”
- “Batch-level documentation”
- “Secure checkout”

### Featured collections
- Best Sellers
- New Arrivals
- Bundles

### Educational section
- “How to read lab results (COA)”
- “Storage and handling FAQ”

## 6) Product Page Template
For each product:
- Product title + concentration/format
- Price + volume discounts
- Batch selector (if needed)
- Short technical summary
- COA/Lab result link for exact batch
- Handling/storage notes
- Shipping estimate
- FAQ accordion

### Product page conversion modules
- Quantity discounts (3+, 5+, 10+)
- Related products
- Recently viewed
- Sticky add-to-cart on mobile

## 7) Lab Results / COA Workflow
Create a dedicated **Lab Results** page with:
- Search by product name and batch ID
- Upload PDFs for each batch
- “Last updated” date

Operational workflow:
1. New inventory arrives.
2. COA is verified and uploaded.
3. Batch metadata is added to Shopify metafields.
4. Product page auto-links to the right COA.

## 8) Recommended Shopify Data Model
Use metafields:
- `custom.batch_id`
- `custom.purity`
- `custom.storage_temp`
- `custom.lab_pdf`
- `custom.disclaimer`

Use tags:
- `best-seller`
- `new`
- `bundle-eligible`
- `requires-signature`

## 9) Launch Content Pack (starter copy)
### Announcement bar
- “20% OFF orders above $500 • Free shipping over $150 • No order minimums”

### Hero copy
- **H1:** Precision peptides. Trusted quality.
- **Body:** Built for customers who expect transparent testing, dependable fulfillment, and consistent standards.
- **CTA:** Shop now

### Trust row
- Third-party tested
- Transparent COAs
- Fast fulfillment

## 10) 30-Day Go-live Plan
### Week 1
- Legal/policy review
- Theme setup
- Navigation + page skeleton

### Week 2
- Add first 10–20 SKUs
- Upload COAs
- Build collection filtering

### Week 3
- Email flows (welcome, cart abandon, post-purchase)
- Pixel + analytics setup
- On-site QA (mobile + checkout)

### Week 4
- Soft launch to small audience
- Review fraud/chargeback signals
- Optimize best-selling PDPs and bundles

## 11) KPI Dashboard (first 90 days)
- Conversion rate
- Average order value
- Returning customer rate
- Checkout completion rate
- Chargeback rate
- Gross margin after shipping + discounts

## 12) Next Step
If you want, I can turn this into:
1. A **ready-to-paste Shopify page copy set** (Home, Product template, Lab Results, FAQ), and
2. A **theme section-by-section build checklist** tailored to Dawn.
