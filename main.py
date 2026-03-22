import time
from datetime import timedelta, datetime

from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from dotenv import load_dotenv
from notification_manager import NotificationManager

load_dotenv()

ORIGIN = "SFO"

data_manager_obj = DataManager()
flight_search_obj = FlightSearch()
sheet_data = data_manager_obj.get_destination_data()
users_data = data_manager_obj.get_customer_emails()
email_list =  []

for user in users_data:
    email = user["whatIsYourEmail?"]
    email_list.append(email)

flight_data_obj = FlightData(None,ORIGIN,None,None,None)
notification_manager_obj = NotificationManager()

# for row in sheet_data:
#     row["iataCode"] = flight_search_obj.get_destination_code(row["city"])
#     time.sleep(2)
# data_manager_obj.destination_data = sheet_data
# data_manager_obj.update_destination_code()


tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=180)
print("sheet_data",sheet_data)
for destination in sheet_data:
    if destination["iataCode"] != "Not found":
        flights = flight_search_obj.check_flights(
        origin=ORIGIN,iata_code=destination["iataCode"],tomorrow=tomorrow,six_months_from_now=six_months_from_now
    )

        print("flights",flights)
        cheapest_flight = flight_data_obj.find_cheapest_flight(flights)#obj
        time.sleep(2)

        if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
            print("low price")
            body = f"LOW PRICE ALERT!!! ONLY ${cheapest_flight.price} TO TRAVEL FROM {cheapest_flight.origin_airport_code} TO {cheapest_flight.destination_airport_code}!!! FROM {cheapest_flight.departure_date} UNTIL {cheapest_flight.return_date}!!!"
            notification_manager_obj.send_whatsapp(body=body)
            print("whatsapp sent")
            notification_manager_obj.send_email(email_body=body,email_list=email_list)






