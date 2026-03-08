import os
from twilio.rest import Client

class NotificationManager:

    #This class is responsible for sending notifications with the deal flight details.
    def send_whatsapp(self,body):
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        account_sid = os.getenv("TWILIO_SID")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        messaging_service_sid=os.getenv("messaging_service_sid"),
        body=body,
        from_=os.getenv("from_"),
        to=os.getenv("to"),
        )




