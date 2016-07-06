#### Location.py will have methods for interacting with the /location endpoint
import CMX.client

def get(ap_mac):
  params = None
  client = CMX.client.new("/api/config/v1/aps/" + ap_mac, params=params)
  return client.get()