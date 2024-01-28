# Amazon Price Scraper

## Description
This project aims to scrape the lowest price on Amazon using a UPC number received from a barcode scanner. The project has evolved through different versions, each addressing specific challenges encountered in the scraping process.


**_Version 1.0 (Using ScraperAPI):_**

Problems Encountered: 

1) Amazon's Unique Identifier System:
- Amazon does not use UPC numbers as unique identifiers for their products. As a result, direct UPC code searches often fail to return relevant product data.
- **Solution1**:
  If there are no results when searching by UPC code, the script re-searches using the product name corresponding to the UPC number. This product name is obtained via BarcodeLookup.
- **Solution2**:
Utilize ASIN Scope to convert UPC numbers to ASIN numbers before conducting a product search on Amazon. This is done using the [ASIN API](https://asinapi.com/).


2) Inaccuracy in Information Retrieval:
- Searching by product name can sometimes yield different or unrelated products.
- Solution: Further refinement of the search algorithm or manual verification might be necessary.


**_Version 2.0 (Using RainforestAPI):_**

Improvements:
The RainforestAPI is used in this version. It utilizes the [GTIN parameter](https://www.rainforestapi.com/docs/product-data-api/parameters/product) to match the UPC number with the ASIN number, providing more accurate product information.

Cost: RainforestAPI offers 10,000 requests for $59.99 per month. For detailed pricing, visit their [pricing page](https://www.rainforestapi.com/pricing/)

