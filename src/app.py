from flask import Flask , request
import pandas as pd
from utils.openai_helper import chat_completion ,transcript_audio
from utils.twilio_helper import send_twilio_message, send_twilio_photo
from utils.campaigns import *
from utils.chating_with_user import ret_chat
from utils.campaigns import run_campaign
import time
app =Flask(__name__)


@app.route('/')
def handle_home():
    return  'ok',200

@app.route('/twilio', methods=['POST'])
def handle_twilio():
    data = request.form.to_dict()
    sender_id = data['From']
    # if 'MediaUrl0' in data.keys():
    #     print('media url :',data['MediaUrl0'])
    #     query = transcript_audio(data['MediaUrl0'])
    #     response = chat_completion(query)
    #     send_twilio_message(response, sender_id)

    query = data['Body']
    if query=='run camp':
        run_campaign()

    else:
        response = ret_chat(query)
        print(response)
        send_twilio_message(response, sender_id)

    return 'OK', 200


