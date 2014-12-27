#!/usr/bin/python
import sys
import requests
from evohomeclient import EvohomeClient

setpoint = requests.get('http://192.168.1.11:8080/rest/items/CV_Current/state')
client = EvohomeClient('email', 'password')
client.set_temperature('Kamer', setpoint.text)

for device in client.temperatures():
	requests.put('http://localhost:8080/rest/items/CV_Temperature/state', data=str(device['temp']))
	requests.put('http://localhost:8080/rest/items/CV_Setpoint/state', data=str(device['setpoint']))
