# Comparison of Amazon Price Scraping APIs

## Overview
This project aims to identify the lowest Amazon price for products using UPC codes from barcode scanners. We progressed through three API versions, each tackling unique challenges in price scraping.

### Version 1.0: ScraperAPI

**Challenges:**
1. **Amazon's Unique Identifiers**:
   - Issue: Amazon doesn't primarily use UPC codes for product identification, leading to frequent search failures.
   - Solutions:
     - **Fallback to Product Name**: If UPC search fails, re-search with the product's name obtained from BarcodeLookup.
     - **UPC to ASIN Conversion**: Convert UPC to Amazon's ASIN numbers for more accurate searches.

2. **Inaccuracy in Product Retrieval**:
   - Product name searches sometimes return unrelated products.
   - Potential Solution: Refine the search algorithm or manually verify results.

### Version 2.0: RainforestAPI

**Improvements:**
- Utilizes the GTIN parameter for better UPC to ASIN matching.

**Cons:**
- **Cost**: $59.99/month for 10,000 requests. [Pricing Details](https://www.rainforestapi.com/pricing/).
- **Speed**: Slower than ScraperAPI, providing extensive data like reviews, which are unnecessary for this project.

### Version 3.0: AsinscopeAPI

**Improvements:**
- Efficient UPC to ASIN conversion.
- Faster than RainforestAPI and provide the lowest Amazon price in result.

**Cost**: $25/month for 1,000 products/day. [Pricing Details](https://asinscope.com/en/asin-to-upc-api).


## Future Tasks:

- [ ] Test the accuracy of the three APIs using sample UPC codes.
- [ ] Compare the speed of results from each API.