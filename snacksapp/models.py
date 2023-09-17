from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class SnacksCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class SnackImage(models.Model):
    image = models.ImageField(storage=S3Boto3Storage(), default="www.google.com")

class SnackItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SnacksCategory, on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    image = models.ImageField(storage=S3Boto3Storage(), default="www.google.com")


    def __str__(self):
        return self.name