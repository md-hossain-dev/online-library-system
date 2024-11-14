from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Book
from django.core.cache import cache

@receiver(post_save, sender=Book)
def book_created(sender, instance, created, **kwargs):
    if created:
        print(f"Book '{instance.title}' by {instance.author.name} was created.")

@receiver(post_delete, sender=Book)
def book_deleted(sender, instance, **kwargs):
    print(f"Book '{instance.title}' by {instance.author.name} was deleted.")




@receiver(post_save, sender=Book)
def clear_books_cache_on_save(sender, instance, **kwargs):
    
    cache.delete('books_list')

@receiver(post_delete, sender=Book)
def clear_books_cache_on_delete(sender, instance, **kwargs):
    
    cache.delete('books_list')
