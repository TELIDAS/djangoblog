from django.urls import path
from .views import get_real_profile, get_real_profile_detail

urlpatterns = [
    path('profile', get_real_profile),
    path('profile/<int:pk>/', get_real_profile_detail),
]
