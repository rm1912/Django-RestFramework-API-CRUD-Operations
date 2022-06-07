from django.db import models

# Create your models here.
 
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    email = models.CharField(max_length=500)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.createdAt)