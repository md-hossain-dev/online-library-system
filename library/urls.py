from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views  # Make sure to import your views module if not already


router = routers.DefaultRouter()
urlpatterns = []


urlpatterns += [
    path('', include(router.urls)),
    path('books/', views.cached_books_list, name='cached_books_list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
