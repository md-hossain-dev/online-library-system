# Generated by Django 3.1.8 on 2024-11-14 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='user',
            new_name='author',
        ),
    ]