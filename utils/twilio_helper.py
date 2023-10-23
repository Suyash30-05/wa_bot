import os
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
client = Client(account_sid, auth_token)
client.auth

def send_twilio_message(message: str, sender_id: str) -> None:
    print(sender_id)
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=sender_id
    )
    print(message.sid)
    return None


def send_twilio_photo(message: str, sender_id: str, media_url: str) -> None:
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=sender_id,
        media_url=media_url
    )
    print(message.sid)
    return None


if __name__=="__main__":

    print(client.auth)
    send_twilio_photo('ok','whatsapp:+919822155190','https://i.ibb.co/SXQjRz4/hl-interest.jpg')

    # https: //
    #
    # <a href="https://imgbb.com/"><img src="" alt="hl-interest" border="0"></a>ibb.co / vDBdfDP
    # https: // ibb.co / x8my1Tn
    # https: // ibb.co / JRx159w
    # https: // ibb.co / fXYJxLw


