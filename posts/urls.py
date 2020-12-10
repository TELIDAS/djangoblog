from django.urls import path
from .views import get_posts, get_profile
urlpatterns = [
    path('', get_posts),
    path('profile/', get_profile),
]
