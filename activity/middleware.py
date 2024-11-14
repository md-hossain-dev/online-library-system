from django.utils.deprecation import MiddlewareMixin
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import UserActivity
from library.models import User

class ActivityMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            self.request = request

    def process_response(self, request, response):
        try:
            if hasattr(self, 'request') and self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
                if self.request.path != 'token/refresh/':
                    activity_type = f"{self.request.method} {self.request.path}"
                    model_name = self.request.resolver_match.app_name  # Assuming each view belongs to an app
                    action = self.request.method
                    ip = self.request.headers.get('CF-Connecting-IP', None)
                    if ip:
                        ip_address = ip
                    else:
                        ip_address = self.request.META.get('REMOTE_ADDR', None)
                    UserActivity.objects.create(
                        user=request.user,
                        activity_type=activity_type,
                        model_name=model_name,
                        action=action,
                        ip_address=ip_address
                    )
        except Exception as e:
            print(str(e))
        return response


@receiver(post_save)
def on_post_save(sender, instance, created, **kwargs):
    l = ['UserActivity', 'Record']
    try:
        if sender.__name__ not in l:  # Avoid logging UserActivity itself
            activity_type = f"Saved {sender._meta.verbose_name} {instance}"
            request = getattr(instance, 'request', None)
            # if request:
            ip_address = request.META.get('REMOTE_ADDR', None) if request else "Login IP"
            UserActivity.objects.create(
                user=instance.user,
                activity_type=activity_type,
                model_name=sender.__name__,
                action='CREATE' if created else 'UPDATE',
                ip_address=ip_address
            )
    except Exception as e:
        print(str(e))

@receiver(post_delete)
def on_post_delete(sender, instance, **kwargs):
    l = ['UserActivity', 'Record']
    try:
        if sender.__name__ not in l:  # Avoid logging UserActivity itself
            activity_type = f"Deleted {sender._meta.verbose_name} {instance}"
            request = getattr(instance, 'request', None)
            ip_address = request.META.get('REMOTE_ADDR', None) if request else "Login IP"
            # ip_address = request.META.get('REMOTE_ADDR', None)
            UserActivity.objects.create(
                user=instance.user,
                activity_type=activity_type,
                model_name=sender.__name__,
                action='DELETE',
                ip_address=ip_address
            )
    except Exception as e:
        print(str(e))