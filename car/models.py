from django.db import models

# Create your models here.

class Car(models.Model):
    producer = models.CharField(max_length=25)
    series = models.TextField()
    img = models.ImageField(upload_to='imgs/', blank=True)
    made_in = models.CharField(max_length=55)
    production_date = models.DateField()
    technical_details = models.TextField()
