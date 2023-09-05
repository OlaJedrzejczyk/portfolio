from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title 