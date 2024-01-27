import requests


# Function to find ASIN info based on UPC
def search_price(upc):
    api_key = 'YOUR_API_KEY',  # Replace with your API key
    params = {
        'api_key': api_key,
        'type': 'product',
        'amazon_domain': 'amazon.com',
        'gtin': upc
    }

    try:
        # Make the HTTP GET request to Rainforest API
        response = requests.get('https://api.rainforestapi.com/request', params)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the JSON response
        parsed_data = response.json()

        # Extract product price (ensure this path exists in your JSON response)
        product_price = parsed_data['product']['variants'][0]['price']['value']
        return product_price

    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
    except KeyError:
        print("Error in data extraction")
        return None


# Main script
if __name__ == "__main__":
    upc = input("Enter UPC Code: ")
    price = search_price(upc)
    if price is not None:
        print(f"Product Price: {price}")
    else:
        print("Price not found or error in retrieving data.")
