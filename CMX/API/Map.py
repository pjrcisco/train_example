#### Location.py will have methods for interacting with the /location endpoint
import CMX.client

def info(floor_info):
  params = None
  client = CMX.client.new("/api/contextaware/v1/maps/info/" + floor_info, params=params)
  return client.get_it()

def image_source(image_name):
  headers = {'Authorization': 'Basic bGVhcm5pbmc6bGVhcm5pbmc='}
  client = CMX.client.new("/api/contextaware/v1/maps/imagesource/" + image_name, headers=headers)
  return client.get()
