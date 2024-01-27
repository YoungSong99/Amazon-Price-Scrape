import requests
from bs4 import BeautifulSoup
import json


# Function to search for the price of a product
def search_price(product_search_term):
    payload = {
        'api_key': 'YOUR_API_KEY',
        'query': product_search_term,
        'country': 'us',
    }
    r = requests.get('https://api.scraperapi.com/structured/amazon/search', params=payload)
    results = json.loads(r.text).get('results', [])

    if results:
        first_item = results[0]
        return first_item.get('price')
    else:
        return None


# Main part of the script
product = input("Enter UPC Code: ")
price = search_price(product)

if price:
    print(f"Price found: {price}")
else:
    print("Price not found. Trying barcode lookup...")

    # Alternative lookup if price is not found
    payload = {
        'api_key': 'YOUR_API_KEY',
        'url': f'https://www.barcodelookup.com/{product}',
    }
    response = requests.get('https://api.scraperapi.com', params=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.select(".product-details h4")

    if elements:
        new_product_name = elements[0].get_text().strip()
        print(f"Product Name Found: {new_product_name}")

        new_price = search_price(new_product_name)
        if new_price:
            print(f"Price for {new_product_name}: {new_price}")
        else:
            print("Price not found for the new product name.")
    else:
        print("Product name not found.")
