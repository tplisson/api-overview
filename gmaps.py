import googlemaps
from datetime import datetime
import os
import json

MY_API_KEY = os.environ["GMAPS_KEY"]
gmaps = googlemaps.Client(key=MY_API_KEY)

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print(geocode_result)
print("---------------------------------------------------------------------------\n")
# json_object = json.loads(geocode_result)
# json_formatted_str = json.dumps(json_object, indent=2)
# print(json_formatted_str)

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
print(reverse_geocode_result)
print("---------------------------------------------------------------------------\n")
# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
print(directions_result)

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)
print(addressvalidation_result)
print("---------------------------------------------------------------------------\n")