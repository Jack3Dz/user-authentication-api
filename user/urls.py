from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserCreate.as_view(), name='user-create'),
]