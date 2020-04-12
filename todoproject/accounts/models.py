from django.db import models
from django.utils import timezone


class Category(models.Model):
    pass

class Task(models.Model):
    #user = models.ForeignKey(Category, null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title