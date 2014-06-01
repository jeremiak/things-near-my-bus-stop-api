import json
from os import environ

from bottle import get, request, run
import requests

stops_from_route_id_url = 'http://gtfs-api.herokuapp.com/api/stops/metro-st-louis/%s'
#fsq_url = 'https://api.foursquare.com/v2/venues/search?radius=500&oauth_token='+environ.get('FOURSQUARE_KEY')+'&v=20140531&ll=%s,%s&query=%s'

def get_stops(stop_url):
  r = requests.get(stop_url)
  if r.status_code == 200:
    return r.json()
  else:
    return False

def locations_near_stop(stop_geo_coords, query_term):
  url = fsq_url % (stop_geo_coords[1], stop_geo_coords[0], query_term)
  print url
  r = requests.get(url)

  if r.status_code == 200:
    return r.json()['response'].get('venues')
  else:
    return False

@get('/routes/<route_id>')
def return_bars_for_route_id(route_id):
  fs_query = request.params.get('query', 'bar')
  stops = get_stops(stops_from_route_id_url % route_id)
  route_venues = []

  for stop in stops:
    if type(stop) != type(None):
      print 'Making request for %s' % stop['stop_id']
      stop_venues = [] #locations_near_stop(stop['loc'], fs_query)
      stop_with_venue = { 'id': stop['stop_id'],
        'stop_location':
          {'lat': stop['loc'][1],'long': stop['loc'][0]},
          'venues': stop_venues
        }  
      route_venues.append(stop_with_venue)

  return json.dumps(route_venues)

if __name__ == '__main__':
  run(host='0.0.0.0', port=environ.get('PORT', 5000), reloader=True)
