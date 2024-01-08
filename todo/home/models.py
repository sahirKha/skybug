from django.db import models

# Create your models here.
class Todo(models.Model):
    Title = models.CharField(max_length=300)
    Description = models.TextField()
    Completed = models.BooleanField(default=True)
