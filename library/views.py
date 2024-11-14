from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def cached_books_list(request):
    cache_key = "books_list"
    books = cache.get(cache_key)
    if not books:
        books = Book.objects.select_related('author').all()  # Database থেকে data নিন
        cache.set(cache_key, books, timeout=60*15)  # 15 মিনিটের জন্য cache এ রাখুন
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

