from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='default content')  # Ensure this line is present

    def __str__(self):
        return self.title


class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.Register_Number


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.CharField(max_length=150)

    def str(self):
        return f'{self.name} - {self.email}'