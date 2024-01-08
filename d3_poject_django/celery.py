import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd3_project_django.settings')

app = Celery('d3_project_django')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()