from django.utils.timezone import now
from .models import MeterReading
from random import uniform

def update_meter_reading():
    # Simulate a reading between 0.1 and 5.0 kWh
    reading = uniform(0.1, 5.0)
    MeterReading.objects.create(reading=reading)
