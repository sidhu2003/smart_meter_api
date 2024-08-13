from django.urls import path
from .views import MeterReadingListCreate

urlpatterns = [
    path('api/readings/', MeterReadingListCreate.as_view(), name='meter_readings'),
]
