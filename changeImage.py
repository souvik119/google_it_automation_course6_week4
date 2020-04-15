#!/usr/bin/env python3

from PIL import Image
import os

path = '/supplier-data/images'
for filename in os.listdir(path):
	if filename.endswith('.tiff'):
		name = (filename.strip(".tiff")) + '.jpeg'
		img = Image.open(os.path.join(path, filename))
		img.resize((600,400)).convert('RGB').save("/supplier-data/images/{}".format(name))
