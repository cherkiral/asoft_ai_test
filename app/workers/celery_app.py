from celery import Celery
from app.bot.config import settings

celery = Celery(
    "tasks",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery.autodiscover_tasks(["app.workers"])

celery.conf.task_routes = {
    "app.workers.tasks.*": {"queue": "default"},
}
