#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
path = "/home/student-03-71991c8ebe4c/supplier-data/images"

for filename in os.listdir(path):
	if ".jpeg" in filename:
		with open(os.path.join(path, filename), 'rb') as opened:
			r = requests.post(url, files={'file': opened})
