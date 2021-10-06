from django.db import models
from django.utils import timezone

class TaskList(models.Model):
     name = models.CharField(max_length = 100)
     taskid = models.IntegerField()

class Record(models.Model):
     name = models.CharField(verbose_name="process name",max_length=40)

    # 市町村名
     start_time = models.DateTimeField(verbose_name="time process start",default=timezone.now)
     
     #start_date = models.DateField()
     status = models.CharField(verbose_name="process status",max_length = 10)

     QT = models.CharField(verbose_name="query sets", max_length=100)