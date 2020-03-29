from app import app
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
import googlemaps, os
from datetime import datetime
import json
import re

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

@app.route("/directions", methods=['GET'])
def getDirections():
	start = request.args.get('start')
	end = request.args.get('end')

	gmaps = googlemaps.Client(key=os.getenv('gmapsAPI'))


	now = datetime.now()
	directions_result = gmaps.directions(start,
										 end,
										 mode="driving",
										 departure_time=now,
										 alternatives=False, 
										 optimize_waypoints=True)
	legs = directions_result[0]['legs'][0]
	total_distance = legs['distance']['text']
	total_time = legs['duration']['text']

	steps = legs['steps']
	step_directions = []
	step_directions.append("Total Travel: {} ({})".format(total_distance, total_time))
	clean = re.compile('<.*?>')
	div_clean = re.compile('<div.*?>')
	tag = "for"
	for step in steps:
		distance = step['distance']['text']
		time = step['duration']['text']
		instruction = step['html_instructions']
		instruction = re.sub(div_clean, '\n', instruction)
		instruction = re.sub(clean, '', instruction)
		parsed_step = "In {} ({}), {}".format(distance, time, instruction)
		step_directions.append(parsed_step)
		print(parsed_step)
		print("\n")
	step_directions.append("You have arrived!")
	step_directions = {i : step_directions[i] for i in range(0,len(step_directions))}
	return json.dumps(step_directions)

