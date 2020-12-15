from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='posts/', null=True)
    description = models.TextField()
    text = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.description} {self.date_added}'

class Profile(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=15)
    age = models.IntegerField()
    hobby = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    about = models.TextField(null=True)

    def __str__(self):
        return f'{self.name} {self.sex} {self.age} {self.hobby}'
