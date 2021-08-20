from django.db import models

# Create your models here.

class Comment(models.Model):
    flowerId = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    message = models.TextField()
    name = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title