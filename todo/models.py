from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)