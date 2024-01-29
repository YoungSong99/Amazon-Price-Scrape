import requests
from bs4 import BeautifulSoup
import json
import time

# Constants
API_KEY = 'YOUR_API_KEY'
SCRAPERAPI_BASE_URL = 'https://api.scraperapi.com'
AMAZON_SEARCH_ENDPOINT = '/structured/amazon/search'
BARCODE_LOOKUP_URL = 'https://www.barcodelookup.com/'



def get_json_response(url, params):
    try:
        response = requests.get(url, params=params)
        return response.json()
    except (requests.RequestException, json.JSONDecodeError):
        return None


def search_amazon_price(product_search_term):
    payload = {
        'api_key': API_KEY,
        'query': product_search_term,
        'country': 'us',
    }
    json_response = get_json_response(f'{SCRAPERAPI_BASE_URL}{AMAZON_SEARCH_ENDPOINT}', payload)
    results = json_response.get('results', []) if json_response else []

    return results[0].get('price') if results else None


def lookup_barcode(barcode):
    payload = {
        'api_key': API_KEY,
        'url': f'{BARCODE_LOOKUP_URL}{barcode}',
    }
    response = requests.get(SCRAPERAPI_BASE_URL, params=payload)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        product_name_element = soup.select_one(".product-details h4")
        return product_name_element.get_text().strip() if product_name_element else None
    return None


def main():
    start_time = time.time()

    product = input("Enter UPC Code: ")
    price = search_amazon_price(product)

    if price:
        print(f"Price found: {price}")
    else:
        print("Price not found. Trying barcode lookup...")
        new_product_name = lookup_barcode(product)

        if new_product_name:
            print(f"Product Name Found: {new_product_name}")
            new_price = search_amazon_price(new_product_name)

            if new_price:
                print(f"Price for {new_product_name}: {new_price}")
            else:
                print("Price not found for the new product name.")
        else:
            print("Product name not found.")


    elapsed_time = time.time() - start_time
    print(f"The code took {elapsed_time} seconds to run.")


if __name__ == "__main__":
    main()
