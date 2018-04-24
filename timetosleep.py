#!/usr/bin/env python3

import time
import sys
import datetime
import pytz
from dateutil import parser
import requests

# Cmd args:
#    offset in minutes (pos or neg intger)
#    event 'sunset', 'sunrise', 'midnight'

## Constants ##
ams = pytz.timezone('Europe/Amsterdam')
lat, lon = '52.070498', '4.300700'
api_url = 'https://api.sunrise-sunset.org/json?lat={}&lng={}&formatted=0'.format(lat, lon)

## Command line args ##
offset = 0 if len(sys.argv) < 2 else int(sys.argv[1])
event = 'sunset' if len(sys.argv) < 3 else sys.argv[2]

## API call to json ##
if event in ['sunset', 'sunrise']:
  json_data = requests.get(url=api_url).json()
# print([s for s in json_data['results']])

## Time difference ##
cur_time = ams.localize(datetime.datetime.now())
if event == 'midnight':
  sns_time = ams.localize(datetime.datetime(cur_time.year, cur_time.month, cur_time.day, 23, 59, 59))
else:
  sns_time = parser.parse(json_data['results'][event])
unt_time = sns_time + datetime.timedelta(minutes=offset)
dif_time = unt_time-cur_time

# print status
# print('Current time : {}'.format(cur_time))
# print('Sunset time  : {}'.format(sns_time))
# print('wait until   : {}'.format(unt_time))
# print('Offset (mins): {}'.format(offset))
# print('Time to wait : {}'.format(dif_time_offs))

## Wait module ##
seconds_to_wait = dif_time.total_seconds()
# Sanity checks (no real exception catching)
if seconds_to_wait > 24*60*60:
 seconds_to_wait = 0
if seconds_to_wait < 0:
 seconds_to_wait = 0


# Main access
print(int(seconds_to_wait))

# time.sleep(seconds_to_wait)

