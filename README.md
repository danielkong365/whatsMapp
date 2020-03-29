# WhatsMapp
RowdyHacks 2020 Project
By Daniel Kong(DanDan#9134), Brett Landau(blands89#8127), and Julie Wang(Pikachi#8489)

## Inspiration
Have you ever gotten lost, but didn't have enough data to run Google Maps or any WiFi signal around? whatsMapp aims to eliminate that problem by giving you another way to access directions the old-fashioned way: step by step directions. Throwback to the days of printing step by step directions from Google Maps BEFORE leaving the house. And now, these directions can be delivered to you by text when you need it!

## What it does
It allows a user to text for step by step directions between place A and place B using their messaging service instead of data. 

## How we built it
Our application is hosted on Google App Engine using Python as our backend. We used Twilio for the messaging and response capabilities. We are using the Google Maps Directions API to extract the step by step directions between places.

## Challenges we ran into
* Parsing the JSON recieved from Google Maps API to look nice. 
* How to send multiple, long text messages to the same user, in order.

## Accomplishments that we're proud of
* Getting the text messages to look formatted
* Getting the server to actually respond to the requests
* Getting long directions to send to the same user over multiple texts.

## What we learned
* How to design a control flow for Twilio
* How to host a Python backend on Google App Engine
* How to enable APIs for use in Google Cloud Platform

## What's next for whatsMapp
* Using the Places API to enable a preliminary 'Search for what's near me' type of service
* Using the Maps Static API and the Twilio MMS API to send a picture of the directions

## Built With
Google Maps Directions API, Google Cloud App Engine, Python, Twilio API

## Try it out
Check out our video link demo for the instructions on how to test it out!
