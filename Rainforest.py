import requests
import time
from functools import wraps

# Constants
API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key
RAINFOREST_API_ENDPOINT = 'https://api.rainforestapi.com/request'


def search_price(upc):
    """ Function to find ASIN info based on UPC using Rainforest API. """
    params = {
        'api_key': API_KEY,
        'type': 'product',
        'amazon_domain': 'amazon.com',
        'gtin': upc
    }

    try:
        response = requests.get(RAINFOREST_API_ENDPOINT, params)
        response.raise_for_status()  # Raise an error for bad status codes
        parsed_data = response.json()

        # Ensure safe extraction of product price
        return parsed_data.get('product', {}).get('variants', [{}])[0].get('price', {}).get('value')

    except requests.RequestException as e:
        print(f"Request error: {e}")
    except KeyError:
        print("Error in data extraction")
    return None

def main():
    """ Main script execution function. """
    start_time = time.time()

    upc = input("Enter UPC Code: ")
    price = search_price(upc)
    if price is not None:
        print(f"Product Price: {price}")
    else:
        print("Price not found or error in retrieving data.")

    elapsed_time = time.time() - start_time
    print(f"The code took {elapsed_time} seconds to run.")


if __name__ == "__main__":
    main()
