import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.environ.get("APP_NAME")
BROKER_URL = os.environ.get("BROKER_URL")
AWS_REGION = os.environ.get("AWS_REGION")
SQS_QUEUE_URI = os.environ.get("SQS_QUEUE_URI")
RESULT_BACKEND_URI = os.environ.get("RESULT_BACKEND_URI")

app = Celery(APP_NAME, broker=BROKER_URL)

# Celery configuration
app.conf.update(
    broker_transport_options={
        'region': AWS_REGION,
        'predefined_queues': {
            'celery': {
                'url': SQS_QUEUE_URI,
            },
        },

    },
    task_routes={'tasks.add': {'queue': 'celery'}},
    result_backend=RESULT_BACKEND_URI,
)

@app.task
def add(x, y):
    return x + y
