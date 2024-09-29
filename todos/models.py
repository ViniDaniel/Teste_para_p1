from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    due_date = models.DateField()
    priority = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High')))
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# Create your models here.
