import asyncio

import CMX.client
import CMX.API.APS    as CMXAPS


def get_all():
  params = None
  client = CMX.client.new("/api/contextaware/v1/location/clients", params=params)
  return client.get_it()

class LocationResource(object):
    def __init__(self, content={}):
      self.content = content
      self.aps     = {}

    def ap_stats(self):
      self.aps = {}
      if self.content["Locations"]:
        for client in self.content["Locations"]["entries"]:
          if client["apMacAddress"] not in self.aps:
            self.aps[client["apMacAddress"]] = {
              "connectedDeviceCount": 1,
              "floorInfo": client["MapInfo"]["mapHierarchyString"].replace('>', '/'),
              "connectedDevices": [{
                "ip": client["ipAddress"],
                "ssId": client["ssId"],
                "mapCoordinate": client["MapCoordinate"]
              }]
            }
          else:
            self.aps[ client["apMacAddress"] ]["connectedDeviceCount"] += 1
            self.aps[ client["apMacAddress"] ]["connectedDevices"].append({
              "ip": client["ipAddress"],
              "ssId": client["ssId"],
              "mapCoordinate": client["MapCoordinate"]
            })
      aps_list = sorted(self.aps.items(), key=lambda x: x[1]['connectedDeviceCount'], reverse=True)
      return {
        "results": aps_list
      }
      #apMacAddresses = []
      #for apMacAddress in self.aps:
      #  apMacAddresses.append(apMacAddress)
      #loop = asyncio.new_event_loop()
      #asyncio.set_event_loop(loop)
      #loop.run_until_complete(self.get_ap_info(apMacAddresses))

    async def get_ap_info(self, apMacAddresses):
      loop    = asyncio.get_event_loop()
      futures = []
      res     = []
      for macAddress in apMacAddresses:
        futures.append( loop.run_in_executor(None, CMXAPS.get, macAddress) )
      for future in futures:
        res.append(await future)
      for result in res:
        print(result.content)
