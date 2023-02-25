import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')

app = Celery('news')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'news_monday_8am': {
        'task': 'news.task.news_monday',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}