#!/usr/bin/python
import sys
import requests
from evohomeclient import EvohomeClient

client = EvohomeClient('email', 'password')
client.cancel_temp_override('Kamer')

for device in client.temperatures():
	requests.put('http://localhost:8080/rest/items/CV_Temperature/state', data=str(device['temp']))
	requests.put('http://localhost:8080/rest/items/CV_Setpoint/state', data=str(device['setpoint']))