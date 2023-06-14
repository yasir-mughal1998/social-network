from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')

app = Celery('social_network')

app.conf.broker_url = 'amqp://guest@localhost//'

app.autodiscover_tasks()
