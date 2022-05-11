import googlemaps
import requests
from pprint import pprint
from datetime import datetime
import google_streetview.api
import google_streetview.helpers

apiKey = open("apikey.txt", "r").read()
gmaps = googlemaps.Client(key=apiKey)

geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
result = gmaps.directions("Bellamy",
                                     "Louisville, KY",
                                     mode="driving",
                                     alternatives=True,
                                     departure_time=now)
steps = result[0]["legs"][0]["steps"]
numOfSteps = len(steps)
stepLocations = []

for step in steps:
    stepLocations.append(step["start_location"])

allLatLngs = ""
for i in range(0, len(stepLocations)):
    lat = str(stepLocations[i]["lat"])
    lng = str(stepLocations[i]["lng"])
    if (i == 0):
        string = lat + "," + lng
    else:
        string = ";" + lat + "," + lng
    latLng = string.strip()
    allLatLngs += latLng

print(allLatLngs)



params = {
    'size': '600x300', # max 640x640 pixels
    'location': allLatLngs,
    'heading': '151.78',
    'pitch': '-0.76',
    'key': apiKey
}

api_list = google_streetview.helpers.api_list(params)

results = google_streetview.api.results(api_list)
results.download_links('stepimages')



















                            