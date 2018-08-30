from flask import Flask, Response

from collections import defaultdict
from itertools import chain

import json
import requests
import pprint

app = Flask(__name__)

@app.route("/")
def index():
    api_token = 'xxxxx'
    api_url_base = 'https://oslobysykkel.no/api/v1/stations'
    api_url_base_avail = 'https://oslobysykkel.no/api/v1/stations/availability'
    headers = { 'Client-Identifier': api_token }

    html = ''

    stations = {}
    stations2 = {}

    response = requests.get(api_url_base, headers=headers)
    walkon = False
    
    if response.status_code == 200:
        walkon = True
        json_object = json.loads(response.content.decode('utf-8'))
        for element in json_object['stations']:
                stations.update({ str(element['id']):{
                             "Sted" : str(element['title']),
                             "Beskrivelse" : str(element['subtitle'])
                           }
                           })
            
    if (walkon):
        response = requests.get(api_url_base_avail, headers=headers)
        if response.status_code == 200:
            json_object = json.loads(response.content.decode('utf-8'))
            for element in json_object['stations']:
                stations2.update({ str(element['id']): {'Ledige sykler': str(element['availability']['bikes']), 'Antall sykler totalt': str(element['availability']['locks'])}})
        else:
            walkon = False
                
    if (walkon):
        dictnew = defaultdict(list)
        for k, v in chain(stations.items(), stations2.items()):
            dictnew[k].append(v)

        for k, v in dictnew.items():
            line = str(v)[1:]
            line = line[:-1]
            html = html +  line + ' <br />'

        #pp = pprint.PrettyPrinter(indent=2)
        #pp.pprint(stations2)
        
        return Response(html), 200
    else:
        return Response('Error ' + response.status_code), 200

if __name__ == "__main__":
    app.run(debug=True)
