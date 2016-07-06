import json
import APIBase

def new(uri, body={}, token=None, params=None, headers=None):
  if headers == None:
    headers = {
      'Authorization': 'Basic bGVhcm5pbmc6bGVhcm5pbmc=',
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
  return APIBase.Client("https://msesandbox.cisco.com", uri, headers, body={}, verify=False, params=params)