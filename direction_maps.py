### pip install -U googlemaps

import googlemaps, os
from datetime import datetime

gmaps = googlemaps.Client(key=os.getenv('gmapsAPI'))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Oradell Public School",
                                     "683 Briarwood Ct Oradell NJ",
                                     mode="driving",
                                     departure_time=now,
                                     alternatives=False, 
                                     optimize_waypoints=True)
print(directions_result)
