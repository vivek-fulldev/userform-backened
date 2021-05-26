from django.urls import path
from .views import UserCreateAPI

urlpatterns = [
    path('user-form', UserCreateAPI.as_view(),name='user'),
]
