#!/usr/bin/env python3

import os, sys
from datetime import datetime as dt
#import emails
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def process_paragraph(dir):
    report_data = []
    for f in sorted(os.listdir(dir)):
        with open(os.path.join(dir, f), 'r') as desc:
            lines = desc.read().strip().splitlines()
            dict = {'name': lines[0], 'weight': lines[1]}
            report_data.append(str('name: {}<br/>weight: {}'.format(dict['name'], dict['weight'])))
    return '<br/><br/>'.join(report_data)

def generate_report(filename, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 10)
    report.build([report_title, empty_line, report_info])

def main(argv):
    title = 'Processed Update on {}/{}/{}'.format(dt.today().month, dt.today().day, dt.today().year)
    path_exists = os.path.exists('../tmp/')
    if not path_exists:
        os.mkdir('../tmp/', mode=0o777, dir_fd = None)
    paragraph = process_paragraph(argv[1])
    generate_report('/tmp/processed.pdf', title, paragraph)

if __name__ == "__main__":
    main(sys.argv)
