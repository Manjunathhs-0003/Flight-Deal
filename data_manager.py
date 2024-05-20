from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d259d5981f795d062d17c541afbe4273/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/d259d5981f795d062d17c541afbe4273/flightDeals/users" 

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.headers = {
            "Authorization": "Bearer your_token_here"  # Replace 'your_token_here' with your actual token
        }

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            if "prices" in data:
                self.destination_data = data["prices"]
                return self.destination_data
            else:
                print("Response does not contain 'prices' key:", data)
        else:
            print("Failed to fetch destination data. Status code:", response.status_code)
        return None


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

# Example usage
if __name__ == "__main__":
    data_manager = DataManager()

    # Get destination data
    destinations = data_manager.get_destination_data()
    pprint(destinations)

    # Update destination codes
    data_manager.update_destination_codes()

    # Get customer emails
    customers = data_manager.get_customer_emails()
    pprint(customers)
