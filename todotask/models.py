from django.db import models

class ToDoTasks(models.Model):
    username = models.CharField(max_length=16)
    index = models.IntegerField(default=0, null=False)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    note = models.CharField(max_length=100, default='', null=True, blank=True)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title

