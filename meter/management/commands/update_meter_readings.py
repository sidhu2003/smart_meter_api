from django.core.management.base import BaseCommand
from meter.models import MeterReading
from random import uniform
from django.utils import timezone

class Command(BaseCommand):
    help = 'Update meter readings'

    def handle(self, *args, **kwargs):
        # Simulate a reading between 0.1 and 5.0 kWh
        reading = uniform(0.1, 5.0)
        MeterReading.objects.create(reading=reading, timestamp=timezone.now())
        self.stdout.write(self.style.SUCCESS('Successfully updated meter reading'))
