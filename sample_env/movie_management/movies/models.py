from django.db import models

# Create your models here.
#MovieIno is amodel cls which is inheriting the 'Model' class. models is a module. it has a class called Model

class MovieInfo(models.Model):
    name = models.CharField(max_length=50,null=True)
    year = models.IntegerField(null=True)
    summary = models.TextField()
