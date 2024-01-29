import requests
import time

# Constants
ASIN_API_KEY = 'YOUR_API_KEY'
ASIN_LOOKUP_URL = 'https://api.asinscope.com/products/lookup'

def fetch_lowest_new_price(upc):
    """ Fetches the lowest new price of a product based on UPC. """
    params = {
        'key': ASIN_API_KEY,
        'upc': upc,
        'domain': 'com'
    }

    try:
        response = requests.get(ASIN_LOOKUP_URL, params=params)
        response.raise_for_status()
        parsed_data = response.json()

        if 'items' in parsed_data and parsed_data['items']:
            return parsed_data['items'][0].get('lowestNewPrice'), None
        return None, "No items found in the response."

    except requests.RequestException as e:
        return None, f"Request error: {e}"
    except KeyError:
        return None, "Error in data extraction"

def main():
    """ Main function to execute the script. """
    start_time = time.time()

    upc = input("Enter UPC Code: ")
    price, error = fetch_lowest_new_price(upc)

    if price is not None:
        print(f"Product Price: {price}")
    else:
        print(error or "Price not found or error in retrieving data.")

    elapsed_time = time.time() - start_time
    print(f"The code took {elapsed_time} seconds to run.")

if __name__ == "__main__":
    main()
