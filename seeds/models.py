from django.db import models

# Create your models here.

class Events(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    img=models.ImageField(null=True,blank=True,upload_to="images/")
    date=models.DateField()

class Startups(models.Model):
    name=models.CharField(max_length=20)
    year=models.PositiveIntegerField()
    owner=models.CharField(max_length =15)
    description=models.CharField(max_length=200)

class GovernBdy(models.Model):
    name=models.CharField(max_length =20)
    position=models.CharField(max_length=20)
    photo=models.ImageField(null=True,blank=True,upload_to="images/")

class About(models.Model):
    mission=models.CharField(max_length=100)
    vision=models.CharField(max_length=100)
    objectives=models.CharField(max_length=100)




