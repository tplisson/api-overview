import googlemaps
from datetime import datetime
import os
import json

MY_API_KEY = os.environ["GMAPS_KEY"]

ADDRESS = '1600 Amphitheatre Parkway, Mountain View, CA'
GPS_COORDINATE = (40.714224, -73.961452)
ORIGIN = "Sydney Town Hall"
DESTINATION = "Parramatta, NSW"
MODE = "transit"

gmaps = googlemaps.Client(key=MY_API_KEY)

# Geocoding an address
geocode_result = gmaps.geocode(ADDRESS)
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print(geocode_result)
print("---------------------------------------------------------------------------\n")

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode(GPS_COORDINATE)
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
print(reverse_geocode_result)
print("---------------------------------------------------------------------------\n")

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions(ORIGIN, DESTINATION, mode=MODE, departure_time=now)
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
print(directions_result)

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)
print(directions_result)
print("---------------------------------------------------------------------------\n")

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)
print(addressvalidation_result)
print("---------------------------------------------------------------------------\n")