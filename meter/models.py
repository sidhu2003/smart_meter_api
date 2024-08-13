from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class MeterReading(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    reading = models.FloatField()
    unit = models.CharField(max_length=10, default='kWh')

    def __str__(self):
        return f"{self.timestamp}: {self.reading} kWh"
