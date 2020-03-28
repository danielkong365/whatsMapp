### pip install -U googlemaps

import googlemaps, os
from datetime import datetime

gmaps = googlemaps.Client(key=os.getenv('gmapsAPI'))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="driving",
                                     departure_time=now,
                                     alternatives=False, 
                                     optimize_waypoints=True)
print(directions_result)
