import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd3_poject_django.settings')

app = Celery('d3_poject_django')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
