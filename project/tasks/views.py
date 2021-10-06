#from django.db.models.query_utils import QueryWrapper
from celery.result import AsyncResult
from django.http import JsonResponse
from django.core.serializers import serialize

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult
import logging
from tasks.sample_tasks import NewOne,Demo, create_task
from tasks.models import TaskList, Record
from celery.task.control import inspect 
import yaml
from django.shortcuts import render
import random
from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView
#from datatables_view.views import DatatablesView

from .models import Record
import os 

logger = logging.getLogger("tasks")

class RecordJsonView(BaseDatatableView):
    # モデルの指定
    model = Record
    # 表示するフィールドの指定
    columns = ["id", "name", "start_time", "status", "QT"]
    def render_column(self, row, column):
        # ボタンに色を付ける
        if column == 'QT':
            return '<button class="button is-danger" >%s</button>' % row.QT
        else:
            return super().render_column(row, column)
    # 検索方法の指定：部分一致
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

def home(request):
    return render(request, "home.html")

# デモtaskを実行する
@csrf_exempt
def run_task(request):
    print("run task called!!")
    print()
    print("request is ",request)
    print(request.POST.get("id"))
    if request.POST:
        task_type = request.POST.get("type")
        task = create_task.delay(int(task_type))
        print("run task")
        NewOne()
        return JsonResponse({"task_id": task.id}, status=202)

# 設定ファイルを受け取って、パラメータを抜き出してからタスクを非同期実行する
@csrf_exempt
def file_task(request):
    print("file task")
    if request.method=="POST":
        req_file = request.FILES.getlist('upfile', None)
        print("filename",req_file)
        # make record
        a = yaml.load(req_file[0])
        print("a",a)
        name = a["QUERY"]
        status = "PENDING"
        qqq = "Not yet"
        b = Record(name=name, status = status, QT= qqq)
        b.save()
        id_record= b.id

        # make file
        SAMPLE_DIR = "MOL"
        if not os.path.exists(SAMPLE_DIR):
            os.makedirs(SAMPLE_DIR)
        with open(SAMPLE_DIR + "/"+str(b.id)+".csv","w"):
            pass
        ra = Record.objects.all()[:2]
        # taskを実行する
        #data = serialize("json", ra)
        taskbool = Demo.delay(id_record)
        logger.info(a)

    return JsonResponse({"ok":"ok"}, status=202)


# タスクの状態を取得する
@csrf_exempt
def get_status(request, task_id):
    print("get task")
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status, 
        "task_result": task_result.result
    }
    logger.debug(request)
    return JsonResponse(result, status=200)


# データを取得する
@csrf_exempt
def dbget(request):
    x = random.randint(1,10000)
    b = TaskList(name="test", taskid=x)
    b.save()
    ra = TaskList.objects.all()[:50]
    #first_50_clubs=1
    #eturn JsonResponse({"directory.html":first_50_clubs})
    print(ra)
    return render(request, "home.html",{"tasklist":ra})

@csrf_exempt
def recordwrite(request):
    print("Add record function called")
    ra = Record.objects.all()[:2]
    data = serialize("json", ra)
    print("serialized data before", data)
    print()
    name = "sampleprocess"
    status = "PENDING"
    qqq= "Cancer"
    b = Record(name=name, status = status,QT=qqq)
    b.save()
    ra = Record.objects.all()[:50]
    print("add record finished")
    print("record in db", ra)
    data = serialize("json", ra)
    print("serialized data", data)
    print()
    print()
    return JsonResponse(data, status=200,safe=False)
from wsgiref.util import FileWrapper

from django.http import HttpResponse
chunksize = 8 * (1024 ** 2)
import csv

# 終了したタスクの出力csvをダウンロードする
@csrf_exempt
def download_csv(request):
    #path = os.path.join(SETTING_DIR)
    filename = "./MOL/"+request.GET.get("fileid")+".csv"
    filewrapper = FileWrapper(open(filename, 'rb'))
    response = HttpResponse(filewrapper, content_type='text/csv')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename="9.csv"'

    return response

#
#
#@csrf_exempt
#def pack_task(request):
#    #print("",a)
#    #tasks = current_app.tasks.keys()
#    #i = app.control.inspect()
#
#    #print(i.active())
#
#    #tasks = app.control.inspect().registered()
#
#    #print("tasks",tasks)
#    #logger.debug('Log whatever you want')
#    #logger.debug(tasks)
#    tasks = inspect().registered_tasks()
#    i=inspect()
#    #print(dir(i))
#    #print("schedule",i.scheduled())
#    #print("+++++++++++++++++++")
#    #print("istat",i.stats())
#    #print("++++++++++++")
#    #print("querytask",i.query_task)
#    #print(inspect()())
#    return JsonResponse(tasks, status=200)