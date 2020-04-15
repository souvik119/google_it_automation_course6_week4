# google_it_automation_course6_week4
This is the week 4 assignment for course Automating Real-World Tasks with Python in the Google IT professional Certificate learning path

## Following files implement specific functionality:

### changeImage.py 
Looks for all the files ending with .tiff extension in /supplier-data/images directory and changes the files to required resolution and extension (.jpeg). Saves all the files in the same directory

### supplier_image_upload.py 
Uploads all the jpeg images to specified URL using requests library

### report_email.py
Formats fruit name and weight data from descriptions folder as a list of dictionaries and passes it to generate_report method in reports.py file to generte PDF report file. It also calls generate_email and send_email methods in the emails.py file to generate and send the report email.

### reports.py
Takes list of dictionaries as argument and creates a pdf file called 'processed.pdf'. Uses reportlab library to accomplish this task.

### emails.py  
Generates and sends emails as required by other modules.

### run.py
Processes jpeg images files in /description folder as a dictionary and uploads fruit information in json format

### health_check.py
Runs system checks and generates appropriate error/warning email.    
 

