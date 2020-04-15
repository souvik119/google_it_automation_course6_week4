#!/usr/bin/env python3

import os
import reports
import emails

def get_info():
	path = '/home/student-03-71991c8ebe4c/supplier-data/descriptions'
	fruit_list = []
	for filename in os.listdir(path):
		if '.txt' in filename:
			fruit = {}
			with open(os.path.join(path, filename)) as f:
				line = f.readlines()
				fruit["name"] = line[0].strip('\n')
				fruit["weight"] = line[1].strip('\n').strip('lbs')
				fruit_list.append(fruit)
	return fruit_list

def main():
	fruits = get_info()
	reports.generate_report(fruits)
	from_text = 'automation@example.com'
	to_text = '@example.com'
	subject_text = 'Upload Completed - Online Fruit Store'
	body_text = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
	attachment_path = '/tmp/processed.pdf'
	message = emails.generate_email(from_text, to_text, subject_text, body_text, attachment_path)
	emails.send_email(message)

if __name__ == "__main__":
	main()
