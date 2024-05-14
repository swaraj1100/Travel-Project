from django.db import models

# Create your models here.

class place(models.Model):
    objects = None
    location=models.CharField(max_length=100)
    description=models.TextField()
    pic=models.ImageField(upload_to='pics')






