from   flask             import Flask, request, jsonify
import json
import requests
import time

import Routes.Constants         as Routes
import Errors.Constants         as Errors

import CMX.API.Location         as CMXLocation
import CMX.API.Map              as CMXMap



app = Flask(__name__)

def pretty_print(data):
  print (json.dumps(data, indent=4, separators=(',', ': ')))

def validate_cmx_request(request):
  if request.method != 'POST' or request.headers["content-type"] != "application/json":
    body = jsonify(**Errors.INVALID_REQUEST)
    return(body, 400)
  else:
    data = request.get_json()
    if data["token"] != "2alkdjf9k3rdjfasdfn":
      body = jsonify(**Errors.INVALID_REQUEST)
      return(body, 400)
    else:
      return True

@app.route(Routes.SNAPSHOT_URL, methods=['POST'])
def snapshot_url():
  if request.method != 'POST' or request.headers["content-type"] != "application/json":
    body = jsonify(**Errors.INVALID_REQUEST)
    return(body, 400)


@app.route(Routes.CMX_AP_STATS_URL, methods=['POST'])
def cmx_ap_stats():
  valid = validate_cmx_request(request)
  if valid != True:
    return valid
  else:
    res               = CMXLocation.get_all()
    LocationResource  = CMXLocation.LocationResource(res)
    res               = LocationResource.ap_stats()
    body              = jsonify(**res)
    return(body, 200)

@app.route(Routes.CMX_MAP_INFO_URL, methods=['POST'])
def cmx_map_info():
  valid = validate_cmx_request(request)
  if valid != True:
    return valid
  else:
    data = request.get_json()
    res  = CMXMap.info(data["floorInfo"])
    body = jsonify(**res)
    return(body, 200)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8082)