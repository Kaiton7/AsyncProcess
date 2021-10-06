from django.contrib import admin
from django.urls import path

from tasks.views import RecordJsonView, download_csv, recordwrite, get_status, home, run_task, file_task, dbget

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recordwrite/",recordwrite, name="recordwrite"),
    path("tasks/<task_id>/", get_status, name="get_status"),
    #path("tasks/", run_task, name="run_task"),
    #path("alltask/", pack_task, name="pack_task"),
    path("tasks/file", file_task, name="file_task"),
    path("dbget/", dbget, name="dbget"),
    path("record/", RecordJsonView.as_view(), name="RecordJsonView"),
    path("DC/", download_csv, name="download_csv"),
    
    path("", home, name="home"),
]
