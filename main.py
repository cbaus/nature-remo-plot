#!/usr/bin/env python3
from remo import NatureRemoAPI
import json
from tinydb import TinyDB, Query
import time
import pandas as pd

config = json.load(open("config.json"))
api = NatureRemoAPI(config['access_token'])
db = TinyDB('db.json')

#user = api.get_user()
#print(user)
device = None

def get_device():
    global device
    devices = api.get_devices()
    device = devices[config["device_id"]]

def get_temp():
    return device.newest_events['te'].val

def get_humi():
    return device.newest_events['hu'].val

def get_motion():
    return device.newest_events['mo'].val

def get_illumination():
    return device.newest_events['il'].val

while True:
    now = time.time()
    now_str = str(pd.to_datetime(now, unit='s'))
    try:
        get_device()
        db.insert({'time': now,
                   'temperature':get_temp(),
                   "humidity": get_humi(),
                   "illumination": get_illumination(),
                   "motion": get_motion()})
        print(f"{now_str} inserted values")
    except Exception as ex:
        print(f"{now_str} Error: {ex})")
    time.sleep(60)
