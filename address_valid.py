import googlemaps
import json
import csv

api_key = 'API-KEY-HERE!'
gmaps = googlemaps.Client(key = api_key)

with open('Bad File.csv', 'rb') as file:
    f = csv.reader(file)
    list = list(f)

def find_address(city, state, company):
    address = company + city + state
    d = json.loads(json.dumps(gmaps.places(address)))
    try:
        full_address = d["results"][0]["formatted_address"]
    except:
        full_address = 'ZERO RESULTS for ' + company + ' in ' + city + ', ' + state
    return full_address

add_list = []
for l in list[1:]:
    city = l[3]
    st = l[4]
    comp = l[8]
    final = find_address(city, st, comp)
    add_list.append([comp, final])
    print len(add_list)

with open('Full Address.csv', 'wb') as finalfile:
    writer = csv.writer(finalfile)
    writer.writerows(add_list)