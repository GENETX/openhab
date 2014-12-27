#!/bin/bash
curl --header "Content-Type: text/plain" --request PUT --data "idle" http://localhost:8080/rest/items/XBMC_State/state > /dev/null 2>&1 &
