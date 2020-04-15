#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime

def generate_report(fruits):
  filename = '/tmp/processed.pdf'
  title = 'Processed Update on {}'.format(datetime.date.today().strftime("%B %d, %Y"))
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  empty_line = Spacer(1,20)
  report_content = [report_title, empty_line]
  for fruit in fruits:
    report_content.append(Paragraph('\n', styles["BodyText"]))
    report_content.append(empty_line)
    report_content.append(Paragraph('name: {}'.format(fruit['name']), styles["BodyText"]))
    report_content.append(empty_line)
    report_content.append(Paragraph('weight: {} lbs'.format(fruit['weight']), styles["BodyText"]))
    report_content.append(empty_line)
  report.build(report_content)
