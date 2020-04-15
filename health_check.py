#!/usr/bin/env python3

import emails
import shutil
import psutil
import socket


from_text = 'automation@example.com'
to_text = 'student-03-71991c8ebe4c@example.com'
body_text = 'Please check your system and resolve the issue as soon as possible.'

cpu_percent = psutil.cpu_percent(1)
du = shutil.disk_usage('/')
disk_percent_free = 100 * du.free / du.total
mem_free_gb = du.free / 2**30
mem_free_mb = mem_free_gb / 1000
IP = socket.gethostbyname('localhost')

if cpu_percent > 80:
	subject_text = 'Error - CPU usage is over 80%'
	message = emails.generate_error_email(from_text, to_text, subject_text, body_text)
	email.send_email(message)

elif disk_percent_free < 20:
	subject_text = 'Error - Available disk space is less than 20%'
	message = emails.generate_error_email(from_text, to_text, subject_text, body_text)
        email.send_email(message)

elif mem_free_mb < 500:
	subject_text = 'Error - Available memory is less than 500MB'
	message = emails.generate_error_email(from_text, to_text, subject_text, body_text)
        email.send_email(message)

elif IP != '127.0.0.1':
	subject_text = 'Error - localhost cannot be resolved to 127.0.0.1'
	message = emails.generate_error_email(from_text, to_text, subject_text, body_text)
        email.send_email(message)
