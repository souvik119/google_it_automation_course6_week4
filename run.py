#! /usr/bin/env python3

import os
import requests

path = '/home/student-03-71991c8ebe4c/supplier-data/descriptions'
url = 'http://35.226.174.87/fruits'

fruit = {}
for filename in os.listdir(path):
	if '.txt' in filename:
		fruit.clear()
		with open(os.path.join(path, filename), 'rb') as f:
			line = f.readlines()
			description = ""
  			for i in range(2,len(line)):
    				description = description+line[i].strip('\n')
			fruit["description"] = description
			fruit["weight"] = int(line[1].strip('\n').strip('lbs'))
			fruit["name"] = line[0].strip('\n')
			fruit["image_name"] = (filename.strip(".txt")) + ".jpeg"
			print(fruit)
			response = requests.post(url, json=fruit)
			print(response.status_code)
