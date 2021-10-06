# project/tasks/sample_tasks.py

import time

from celery import shared_task

import csv
import urllib
from bs4 import BeautifulSoup
from tasks.models import  Record

#import pandas as pd
@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True

@shared_task
def Demo(id_record):
    print("demo kicked")
    s = Record.objects.filter(id=id_record).first()
    s.status = "PROCESSING"
    s.save()
    with open("MOL/"+str(id_record)+".csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([id_record])
        writer.writerow("demo!!")
    time.sleep(10)

    s = Record.objects.filter(id=id_record).first()
    s.status = "SUCCESS"
    s.save()
    s = Record.objects.filter(id=id_record).first()
    s.QT = "DOWNLOAD"
    s.save()
    print("task finished")
    return True

@shared_task
def NewOne():
    url = "https://en.wikipedia.org/wiki/List_of_cities_in_Japan"
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all("table")
    for tab in table:
        table_className = tab.get("class")
        if table_className[0] == "wikitable":
            with open("logs/test.csv", "w", encoding='utf-8') as file:
                writer = csv.writer(file)
                rows = tab.find_all("tr")
                for row in rows:
                    csvRow = []
                    for cell in row.findAll(['td', 'th']):
                        csvRow.append(cell.get_text())
                    writer.writerow(csvRow)
            break