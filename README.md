# whatsMapp
RowdyHacks 2020 Project
By Daniel Kong(DanDan#9134), Brett Landau(blands89#8127), and Julie Wang(Pikachi#8489)

## Inspiration
Have you ever gotten lost, but don't have enough data to run Google Maps or no internet signal? whatsMapp aims to eliminate that problem by giving you another way to access directions the old-fashioned way: step by step directions. Throwback to the days of printing step by step directions from Google Maps BEFORE leaving the house. And now, these directions can be delivered to you by text when you need it!

## What it does
It allows a user to text for step by step directions between place A and place B using their messaging service instead of data. 

## How we built it
Our application is hosted on Google App Engine and is written in Python. We used Twilio for the messaging and response capabilities. We are using the Google Maps Directions API to extract the step by step directions between places.

## Challenges we ran into
* Designing the control flow
* How to parse the json
* Enabling and connecting everything

## Accomplishments that we're proud of
* Directions are provided quickly and in a readable format
* There is no limitation for length of route

## What we learned
* Learned how to use App Engine and Twilio
* Learned how to parse json and utilize Google Maps API

## What's next for whatsMapp
* Allow users to search for points of interest if they don't yet know where they're going

## Built With
Google Maps API, Google Cloud App Engine, Python, Flask, Twilio API
