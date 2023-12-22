from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField('Title', max_length=120)
    description = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)
    creation_date = models.DateField('Creation Date')
    due_date = models.DateField('Due Date')
    priority = models.CharField('Priority', max_length=20, blank=True)
    mark = models.CharField('Mark', max_length=20, blank=True)
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class UserList(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.name
