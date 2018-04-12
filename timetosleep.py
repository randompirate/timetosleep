#!/usr/bin/env python3

import sys
from datetime import datetime, timedelta
import pytz
from dateutil import parser
import time
import requests

# Cmd args:
#    offset in minutes (pos or neg intger)
#    event 'sunset', 'sunrise'

## Constants ##
TIMEZONE_AMS = pytz.timezone('Europe/Amsterdam')
lat, lon = '52.070498', '4.300700'
api_url = 'https://api.sunrise-sunset.org/json?lat={}&lng={}&formatted=0'.format(lat, lon)

## Command line args ##
offset = 0 if len(sys.argv) < 2 else int(sys.argv[1])
event = 'sunset' if len(sys.argv) < 3 else sys.argv[2]
nowait = True if '-n' in sys.argv else False

## API call to json ##
json_data = requests.get(url=api_url).json()
# print([s for s in json_data['results']])

## Time difference ##
cur_time = datetime.now(tz=TIMEZONE_AMS)
sns_time = parser.parse(json_data['results'][event]) + timedelta(minutes=offset)
unt_time = sns_time + timedelta(minutes=offset)
dif_time = unt_time-cur_time

# print status
print('Current time : {}'.format(cur_time))
print('Sunset time  : {}'.format(sns_time))
print('wait until   : {}'.format(unt_time))
print('Offset (mins): {}'.format(offset))
# print('Time to wait : {}'.format(dif_time_offs))

## Wait module ##
seconds_to_wait = dif_time.total_seconds()
# Sanity check
if seconds_to_wait > 24*60*60:
 print('error')
if seconds_to_wait < 0:
 exit()

if not nowait:
  time.sleep(seconds_to_wait)

