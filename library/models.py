from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from django.utils import timezone

class User(AbstractUser):
  username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  email = models.EmailField()
  date_of_birth = models.DateField(null=True,blank=True)
  
  def __str__(self):
      return self.username



class Book(models.Model):
	title = models.CharField(max_length=250,null=True,blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='book')
	published_date = models.DateField()
	is_archived = models.BooleanField(default=False)

	def __str__(self):
		return self.title