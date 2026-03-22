import os
import requests

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_API_SECRET")
        self.token = self._get_new_token()

    def get_destination_code(self,city_name):
        query = {
            "keyword":city_name,
            "max":2,
            "include":"AIRPORTS"
        }
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.get(url=IATA_ENDPOINT,headers=headers,params=query)

        try:
            code = response.json()["data"][0]["iataCode"]
            print("iata coderes", code)
        except IndexError:
            return "N/A"
        except KeyError:
            return "Not found"
        return code

    def _get_new_token(self):
        URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret,
        }

        response = requests.post(url=URL, headers=header, data=body)
        access_token = response.json()["access_token"]
        return access_token

    def check_flights(self, origin, iata_code , tomorrow, six_months_from_now):

        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "originLocationCode":origin,
            "destinationLocationCode":iata_code,
            "departureDate":tomorrow.strftime("%Y-%m-%d"),
            "returnDate":six_months_from_now.strftime("%Y-%m-%d"),
            "adults":1,
            "nonStop":"true",
            "currencyCode":"USD",
            "max":"10",
        }
        response = requests.get(url=FLIGHT_ENDPOINT,headers=headers,params=query)
        return response.json()

