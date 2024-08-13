from rest_framework import generics
from .models import MeterReading
from .serializers import MeterReadingSerializer

class MeterReadingListCreate(generics.ListCreateAPIView):
    queryset = MeterReading.objects.all()
    serializer_class = MeterReadingSerializer
