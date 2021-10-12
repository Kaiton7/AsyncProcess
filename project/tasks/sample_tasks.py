# project/tasks/sample_tasks.py

import time

from celery import shared_task

import csv
from tasks.models import  Record

@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True

@shared_task
def Demo(id_record):
    # update process status PROCESSING
    s = Record.objects.filter(id=id_record).first()
    s.status = "PROCESSING"
    s.save()
    with open("MOL/"+str(id_record)+".csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([id_record])
        writer.writerow("demo!!")
    time.sleep(10)
    # update process status SUCCESS
    s = Record.objects.filter(id=id_record).first()
    s.status = "SUCCESS"
    s.save()
    # update Download botton
    s = Record.objects.filter(id=id_record).first()
    s.QT = "DOWNLOAD"
    s.save()
    return True
