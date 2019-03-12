from django.urls import path

from src.v1.user.views.profile import ProfileView, ProfileDetail
from .views.user import UserView
from .views.login import LoginView
from .views.logout import LogoutView


urlpatterns = [
    # Login / logout
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),

    # Profiles
    path('profiles', ProfileView.as_view(), name='profile-list'),
    path('profiles/<int:profile_id>/', ProfileDetail.as_view(), name='profile-specific'),

    # Users
    path('users/', UserView.as_view(), name='user-create'),
]
