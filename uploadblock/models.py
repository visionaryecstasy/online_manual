from django.db import models

# Create your models here.
class file(models.Model):
    filename = models.FileField()