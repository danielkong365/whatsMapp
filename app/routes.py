from app import app
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
import googlemaps, os
from datetime import datetime
from random import seed
from random import randint
seed(1234)
import json
import re
import shutil

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
	step_directions = ""
	step_directions += "Total Travel: {} ({})\n\n".format(total_distance, total_time)
	clean = re.compile('<.*?>')
	div_clean = re.compile('<div.*?>')
	tag = "for"
	for step in steps:
		distance = step['distance']['text']
		time = step['duration']['text']
		instruction = step['html_instructions']
		instruction = re.sub(div_clean, '\n', instruction)
		instruction = re.sub(clean, '', instruction)
		parsed_step = "In {} ({}), {}\n\n".format(distance, time, instruction)
		step_directions += parsed_step
		print(parsed_step)
	step_directions += "You have arrived!"
	fName = str(randint(1000,9999))
	op = open(fName,"w")
	op.write(step_directions)
	op.close()
	return fName


@app.route("/getnext", methods=['GET'])
def getNext():
	id = request.args.get('id')
	myfile = id
	temp = "temp"
	src = open(myfile,"r")
	dest = open(temp,"w")
	shutil.copyfileobj(src,dest)
	src.close()
	dest.close()
	src = open(temp,"r")
	dest = open(myfile,"w")
	output = src.read(1000)
	shutil.copyfileobj(src,dest)
	src.close()
	dest.close()
	return output
