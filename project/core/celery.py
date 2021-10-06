import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

def get_at():
    i = app.control.inspect()
    print(i.active())
    tasks = app.control.inspect().registered()

    print("tasks",tasks)
    logger.debug('Log whatever you want')
    return tasks