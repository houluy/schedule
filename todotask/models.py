from django.db import models

class ToDoTasks(models.Model):
    username = models.CharField(max_length=16, primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title

