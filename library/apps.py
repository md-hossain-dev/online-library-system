from django.apps import AppConfig

class LibraryConfig(AppConfig):
    name = 'books'

    def ready(self):
        import books.signals  # Import signals to activate them
