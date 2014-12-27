#!/usr/bin/python
import sys
import requests
from evohomeclient2 import EvohomeClient

client = EvohomeClient('email', 'password')

for device in client.temperatures():
	requests.put('http://localhost:8080/rest/items/CV_Temperature/state', data=str(device['temp']))
    	requests.put('http://localhost:8080/rest/items/CV_Setpoint/state', data=str(device['setpoint']))

