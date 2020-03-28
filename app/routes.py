from app import app
from flask import request
from twilio.twiml.messaging_response import MessagingReponse

@app.route('/')
@app.route('/index')
def index():
	return "Welcome to WhatsMapp!"

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)

