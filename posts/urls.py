from django.urls import path
from .views import get_posts, get_profile
urlpatterns = [
    path('posts', get_posts),
    path('profile/', get_profile),
]
