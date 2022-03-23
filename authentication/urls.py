from django.urls import path
from django.contrib.auth import urls

from . import views

urlpatterns = [
    path('register/', views.SignUpCreateView.as_view(), name='register'),
]