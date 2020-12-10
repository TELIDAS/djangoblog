from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
