from .models import File
from celery import shared_task


@shared_task
def check_processed(file_id):
    try:
        file_processed = File.objects.get(id=file_id)
        file_processed.processed = True
        file_processed.save()
        return f"File {file_id}  as processed."


    except File.DoesNotExist:
        return f"File {file_id} does not exist."
