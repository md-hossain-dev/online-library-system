from django.conf import settings
from django.db import models
from library.models import User
class UserActivity(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='activity_user',blank=True, null=True)
    activity_type = models.CharField(max_length=255, blank=True, null=True)
    model_name = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)  # e.g., 'CREATE', 'UPDATE', 'DELETE'
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.model_name} - {self.action}"




