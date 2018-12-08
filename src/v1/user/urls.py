from django.urls import path
from .views.user import UserView
from .views.login import LoginView

urlpatterns = [
    path('users/', UserView.as_view(), name='user-create'),
    path('login/', LoginView.as_view(), name='user-login'),
]