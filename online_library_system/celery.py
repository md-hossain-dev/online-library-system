from celery import shared_task
from .models import Book
from django.utils import timezone

@shared_task
def archive_old_books():
    ten_years_ago = timezone.now().date().replace(year=timezone.now().year - 10)
    Book.objects.filter(published_date__lt=ten_years_ago, is_archived=False).update(is_archived=True)
