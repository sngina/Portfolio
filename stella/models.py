from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=30)
    description= models.TimeField()
    url=models.URLField(max_length=200)
    tools = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    img_name= models.CharField(max_length=100)

    def __str__(self):
        return self.title