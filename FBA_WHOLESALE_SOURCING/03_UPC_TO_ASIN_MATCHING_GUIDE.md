# UPC-to-ASIN Reverse Matching Methodology

## Overview
This is the **MOST CRITICAL STEP** in wholesale sourcing. You must match wholesaler products to existing Amazon ASINs with 100% accuracy to ensure you're selling on established listings with existing reviews and demand.

**Golden Rule**: If you're not 100% certain it's an EXACT match, do NOT proceed. "Close enough" will get your account suspended.

---

## PHASE 1: GET WHOLESALER CATALOG DATA

### Method 1: Excel/CSV Product List (BEST)
**Request from wholesaler**:
- "Can you provide your product catalog in Excel or CSV format with UPC codes?"
- Ideal columns: SKU, Brand, Product Name, UPC/GTIN/EAN, Case Pack, Wholesale Price, MAP (if applicable)

### Method 2: PDF Catalog
- Download PDF catalog
- Use Jungle Scout Supplier Database or manual extraction to pull UPC codes
- Create your own spreadsheet

### Method 3: Online Catalog (B2B Portal)
- Request access to their B2B portal
- Use browser tools or manual copy/paste to extract:
  - Product names
  - Brand names
  - Model numbers
  - UPC/GTIN codes
  - Product images

### Method 4: Direct Inquiry
If catalog is limited:
- Email: "I'm interested in your [Brand Name] products for Amazon resale. Can you provide UPC codes for the following items: [list 10-20 items]?"

---

## PHASE 2: UPC-TO-ASIN LOOKUP

### Method A: Amazon Product Finder (Free, Manual)

1. **Go to Amazon.com**
2. **Paste the UPC into Amazon search bar**
3. **Look for EXACT match**:
   - Same brand
   - Same product name/title
   - Same packaging (single vs. multi-pack)
   - Same size/quantity
   - Same color/variant

4. **Copy the ASIN**:
   - From URL: amazon.com/dp/**B08EXAMPLE**
   - Or from product details section

5. **Verify with images**: Click through product images and compare to wholesaler's images

**Time**: ~2-3 minutes per product (manual)

---

### Method B: Jungle Scout Supplier Database (Paid - RECOMMENDED)

**If you have Jungle Scout subscription**:

1. **Go to Jungle Scout > Supplier Database**
2. **Upload your wholesaler's product list (CSV/Excel)**
3. **Map columns**:
   - UPC/EAN → UPC column
   - Product Name → Title
   - Brand → Brand

4. **Jungle Scout automatically matches UPCs to ASINs**
5. **Export results** with:
   - ASIN
   - Current Buy Box price
   - Estimated monthly sales
   - Number of sellers
   - BSR (Best Sellers Rank)

**Time**: Bulk upload = seconds per 100+ products

---

### Method C: InventoryLab or Seller Tools (if you have it)

**InventoryLab**:
- List items → UPC scan → Auto-matches to ASIN
- Shows profitability instantly

**SellerAmp SAS**:
- Chrome extension
- Bulk UPC search
- Shows profitability + restrictions

---

### Method D: Amazon Seller Central (if you have account)

1. **Login to Seller Central**
2. **Go to Inventory > Add a Product**
3. **Search by UPC**
4. **Amazon shows matching ASIN (if it exists)**

**Bonus**: You'll see immediately if the product is restricted/gated for your account

---

### Method E: Third-Party UPC Lookup Tools

**Free Tools**:
- **UPCitemdb.com**: Paste UPC → Shows Amazon link + product info
- **BarcodesInc.com**: UPC lookup
- **EAN-Search.org**: International barcode database

**Paid Tools**:
- **Keepa**: Has UPC-to-ASIN lookup API
- **ASINspector**: Chrome extension with UPC scan

---

## PHASE 3: VERIFICATION (CRITICAL - DO NOT SKIP)

### Step 1: Visual Confirmation
✅ **Compare wholesaler images to Amazon listing images**
- Same product angle
- Same packaging design
- Same label/branding
- Same included accessories

### Step 2: Specification Match
✅ **Check product details on both sides**:
| Wholesaler Catalog | Amazon Listing | Match? |
|--------------------|----------------|--------|
| Brand | Brand | ✅ |
| Model # | Model # | ✅ |
| UPC | UPC (in product details) | ✅ |
| Pack Count (1, 2, 6-pack?) | Pack Count | ✅ |
| Size/Dimensions | Dimensions | ✅ |
| Color/Variant | Color | ✅ |
| Weight | Shipping Weight | ✅ |

**Example**:
- ❌ Wholesaler: "Coffee Mug Set (4-pack)" → Amazon: "Coffee Mug (Single)"
- ❌ Wholesaler: "Model ABC-100" → Amazon: "Model ABC-200"
- ❌ Wholesaler: "12 oz" → Amazon: "16 oz"

### Step 3: UPC Verification on Amazon Listing
1. Scroll to "Product Information" section on Amazon
2. Look for:
   - **UPC**: 012345678901
   - **EAN**: (European Article Number - 13 digits)
   - **ISBN**: (for books only)

3. **Cross-reference** with wholesaler's UPC

**If UPC is NOT shown on Amazon listing**:
- Check Keepa data (sometimes has UPC history)
- Use Jungle Scout Product Database (shows UPC for most products)
- Contact Amazon Seller Support to confirm UPC for that ASIN

### Step 4: Brand Authorization Check
✅ **Is this brand restricted/gated on Amazon**?

**Test**:
1. Go to Seller Central > Inventory > Add a Product
2. Search for the ASIN
3. Try to create a listing
4. If you see:
   - ✅ "Sell this product" button → Ungated
   - ⚠️ "Request Approval" button → Gated (you'll need authorization)
   - ❌ "You are not approved to sell this brand" → Hard gated

**Common Gated Categories**:
- Grocery & Gourmet Food (most brands)
- Health & Personal Care (topical products)
- Beauty (major brands)
- Baby products (major brands)
- Toys & Games (during Q4)

---

## PHASE 4: DEMAND VALIDATION (Use Jungle Scout)

For each matched ASIN, check:

### A. Sales Volume
```
Jungle Scout Estimated Monthly Sales: _____ units
```
**Targets**:
- Minimum: 100 units/month
- Good: 200-500 units/month
- Excellent: 500+ units/month

### B. Sales Trend
```
Sales History (90 days):
- Month 1: _____ units
- Month 2: _____ units
- Month 3: _____ units
```
**Look for**:
- ✅ Stable or growing
- ⚠️ Seasonal (flag for further investigation)
- ❌ Declining (skip unless you know why)

### C. Price Stability
```
Price History (90 days):
- 90 days ago: $_____
- 60 days ago: $_____
- 30 days ago: $_____
- Today: $_____
```
**Red Flags**:
- ❌ Price dropped >15% in 90 days (price war)
- ❌ Volatile pricing (different every week)

### D. Competition Level
```
Number of Sellers on Listing: _____
```
**Targets**:
- ✅ 1-5 sellers: Low competition
- ⚠️ 6-10 sellers: Moderate competition
- ❌ 11+ sellers: High competition (only if margins are excellent)

### E. Best Sellers Rank (BSR)
```
BSR in Category: _____
```
**General Guidelines**:
- BSR < 10,000 in main category: Excellent sales velocity
- BSR 10,000-50,000: Good sales velocity
- BSR 50,000-100,000: Moderate sales velocity
- BSR > 100,000: Slower sales (evaluate carefully)

**Note**: BSR ranges vary by category. Pet Supplies BSR 50,000 ≠ Electronics BSR 50,000

---

## PHASE 5: KEYWORD VALIDATION (Use Helium 10 DataDive or Cerebro)

### A. Search Volume Check
1. **Get main keyword from ASIN title**
   - Example: "Stainless Steel Kitchen Tongs 12 Inch" → Main keyword = "kitchen tongs"

2. **Run DataDive search for that keyword**:
   ```
   Keyword: "kitchen tongs"
   Monthly Search Volume: _____
   Search Trend (12 months): _____
   ```

**Targets**:
- Minimum: 1,000 searches/month
- Good: 5,000-20,000 searches/month
- Excellent: 20,000+ searches/month

### B. Keyword Stability
**Check if keyword volume is**:
- ✅ Stable year-round
- ⚠️ Seasonal (Q4 spike for holidays, summer spike for outdoors, etc.)
- ❌ Trending/fad (sudden spike then drop)

### C. Relevance Check
**Use Cerebro (Helium 10) or Jungle Scout Keyword Scout**:
1. Enter the ASIN
2. See ALL keywords the listing ranks for
3. Verify:
   - ✅ Listing ranks for 50+ relevant keywords
   - ✅ Top 10 keywords have strong search volume
   - ❌ Listing ranks for irrelevant keywords (sign of poor listing quality or fake reviews)

---

## PHASE 6: DOCUMENT YOUR MATCHES

### Create a Master Spreadsheet with these columns:

| Wholesaler SKU | Wholesaler Product Name | Brand | UPC | ASIN | Amazon Title | Match Verified? | Buy Box Price | Est. Monthly Sales | # Sellers | BSR | Gated? | Notes |
|----------------|-------------------------|-------|-----|------|--------------|-----------------|---------------|-------------------|-----------|-----|--------|-------|
| ABC-123 | Kitchen Tongs 12" SS | ChefPro | 012345678901 | B08XYZ | ChefPro Stainless Steel Kitchen Tongs, 12-Inch | ✅ Yes | $22.99 | 300 | 7 | 15,432 | No | Stable demand |

---

## COMMON MATCHING MISTAKES TO AVOID

### ❌ Mistake #1: Pack Count Mismatch
**Wholesaler**: Sells 6-pack
**Amazon ASIN**: Single unit
**Result**: You'll lose money per unit + confuse customers + risk account suspension

**Solution**: Search for "6 pack" or "case of 6" on Amazon to find the correct multi-pack ASIN

---

### ❌ Mistake #2: Model Number Variation
**Wholesaler**: Model ABC-100 (2024 version)
**Amazon ASIN**: Model ABC-100 (2022 version)
**Result**: Customer complaints, returns, inauthentic claims

**Solution**: Verify model number + year + any version differences

---

### ❌ Mistake #3: Regional Variations
**Wholesaler**: US version (UPC)
**Amazon ASIN**: International version (EAN)
**Result**: Different packaging, different voltage, different language

**Solution**: Confirm region/market on both wholesaler and Amazon listing

---

### ❌ Mistake #4: Color/Size Variant Confusion
**Wholesaler**: "Blue, Large"
**Amazon**: ASIN for "Red, Medium"
**Result**: Wrong variant shipped → returns + complaints

**Solution**: Use Amazon's parent-child ASIN structure. Match to the specific child ASIN for that exact variant.

---

### ❌ Mistake #5: Bundles vs. Individual Items
**Wholesaler**: Sells individual item
**Amazon**: Listing is a "bundle" with multiple items
**Result**: Incomplete order + customer complaints

**Solution**: Read the full Amazon listing description + "What's in the box" section

---

## TOOLS SUMMARY

| Tool | Purpose | Cost | Link |
|------|---------|------|------|
| Amazon Search | Manual UPC lookup | Free | amazon.com |
| Jungle Scout Supplier Database | Bulk UPC-to-ASIN matching | $49-99/mo | junglescout.com |
| Keepa | Price + BSR history | Free (premium $19/mo) | keepa.com |
| Helium 10 DataDive | Keyword search volume | $29-99/mo | helium10.com |
| Helium 10 Cerebro | Reverse ASIN keyword lookup | Included in H10 | helium10.com |
| UPCitemdb.com | Free UPC lookup | Free | upcitemdb.com |
| Seller Central | Check restrictions/gating | Free (need account) | sellercentral.amazon.com |

---

## WORKFLOW SUMMARY

1. ✅ Get wholesaler product list with UPCs
2. ✅ Look up UPC → ASIN (bulk or manual)
3. ✅ Verify 100% exact match (images, specs, pack count)
4. ✅ Check Amazon listing for UPC confirmation
5. ✅ Run Jungle Scout demand analysis (sales + trend)
6. ✅ Run DataDive keyword validation (search volume + stability)
7. ✅ Check gating/restrictions
8. ✅ Calculate profitability (see Profitability Calculator doc)
9. ✅ Document in master spreadsheet
10. ✅ Proceed to supplier outreach (see Outreach Kit doc)

---

## NEXT STEPS

Once you have 20-50 verified matches:
1. Prioritize by profitability + demand
2. Request quotes from wholesaler for top 10-20 products
3. Place small test order (1-2 case packs per SKU)
4. List on Amazon (using existing ASIN)
5. Monitor performance for 30-60 days
6. Scale winners, cut losers
