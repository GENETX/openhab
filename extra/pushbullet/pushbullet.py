#!/usr/bin/python3
import sys
from pushbullet import PushBullet

pb = PushBullet("key")
if len(sys.argv) > 1:
	s = ""
	for i in range(1, len(sys.argv)):
		if i>1:
			s += " "
		s += str(sys.argv[i])
	pb.push_note("OpenHAB", s)