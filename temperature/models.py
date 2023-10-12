from django.db import models

class TemperatureData(models.Model):
    sourcename = models.CharField(max_length=255, default='unknown')
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)