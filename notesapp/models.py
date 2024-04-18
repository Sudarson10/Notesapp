from django.db import models

class Task(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=1000)
    created=models.DateTimeField(auto_now_add=True)

