from geopy.geocoders import Nominatim
from geopy.distance import distance

import certifi
import urllib
import ssl

#here, we pass the certifi certificates into the urlopen method to avoid errors of no certifications
def uo(args, **kwargs):
    # We create an ssl context to fetch the certificate provided by the local server without performing validation of
    # the certificate
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    return urllib.request.urlopen(args, context=ssl_context)

geolocator = Nominatim(user_agent="Golf Caddie App")
#print(uo)
geolocator.urlopen = uo

location1 = geolocator.geocode(input("Enter your current location address (Where is the ball?):"))
print("Point A: ", location1.address)
print("latitude is :-" ,location1.latitude,"\nlongtitude is:-" ,location1.longitude,"\n")
location1_coord = location1.latitude, location1.longitude

location2 = geolocator.geocode(input("Enter your destination address (Where is the hole?): "))
print("Point B:", location2.address)
print("latitude is :-" ,location2.latitude,"\nlongtitude is:-" ,location2.longitude,"\n")
location2_coord = location2.latitude, location2.longitude

# Uses Vincenty’s formulae by default
d = distance(location1_coord, location2_coord)

print("Your distance is: ", d)

