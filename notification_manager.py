import os
import smtplib
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.mail = os.getenv("mail")
        self.password = os.getenv("password")

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

    def send_email(self,email_list,email_body):

        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=self.mail, password=self.password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.mail,
                    to_addrs=email,
                    msg=email_body
                )




