from rest_framework import serializers
from home.models import TemperatureData

class TemperatureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureData
        fields = ['sourcename', 'temperature', 'timestamp']
