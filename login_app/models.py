from django.db import models

class User_info(models.Model):
    username = models.CharField(max_length=16, primary_key=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32, default='')
    birth = models.DateTimeField('Birthday', default='1990-1-1')
    def __str__(self):
        return self.username


