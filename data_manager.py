import os
import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    #to update the sheet

    def __init__(self):
        self.token = os.getenv("token")
        self.sheety_url = os.getenv("sheety_url")
        self.sheety_header = {
        "Authorization": f"Bearer {self.token}"}
        self.destination_data = {}

    def get_destination_data(self):
        sheety_response = requests.get(url=self.sheety_url, headers=self.sheety_header)
        sheety_result = sheety_response.json()
        sheet_data = sheety_result["prices"]
        self.destination_data = sheet_data

        return sheet_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{self.sheety_url}/{city['id']}",json=new_data,headers=self.sheety_header)
            result = response.json()
            print(result)
