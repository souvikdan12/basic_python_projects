from twilio.rest import Client


ACCOUNT_SID = "xxxxxxxxxxxxx" 
AUTH_TOKEN = "90777aff00574xxxxxxxxxxxxxxxx146c" 

TWILIO_NUMBER = "+13xxxxxxx881431"  # virtual number by Twilio
RECEIVER_NUMBER = "+919204150780" # verified phone number

client = Client(ACCOUNT_SID, AUTH_TOKEN)

try:
    message = client.messages.create(
        body="Hello! This is an automated SMS sent from Python. 🚀",
        from_=TWILIO_NUMBER,
        to=RECEIVER_NUMBER
    )
    print("SMS Sent Successfully!")
    print("Message ID:", message.sid)

except Exception as e:
    print("Error:", e)