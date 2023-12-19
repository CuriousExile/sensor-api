import glob
import time
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.models import TemperatureData
from home.serializers import TemperatureDataSerializer
from rest_framework import generics
from datetime import datetime

class TemperatureDataViewSet(viewsets.ModelViewSet):
    queryset = TemperatureData.objects.all()
    serializer_class = TemperatureDataSerializer


class TemperatureDataView(APIView):
        
    def get(self, request):
        current_temperature = 22
        temperature_data = TemperatureData(sourcename='garnele', temperature=current_temperature)
        temperature_data.save()

        serializer = TemperatureDataSerializer(temperature_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class TemperatureDataListView(generics.ListAPIView):
    serializer_class = TemperatureDataSerializer

    def get(self, request, *args, **kwargs):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        queryset = TemperatureData.objects.filter(timestamp__range=[start_date, end_date])
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class TemperatureDataCreateView(generics.CreateAPIView):
    serializer_class = TemperatureDataSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        queryset = TemperatureData.objects
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class LatestTemperatureView(generics.RetrieveAPIView):
    serializer_class = TemperatureDataSerializer

    def get_object(self):
        return TemperatureData.objects.latest('timestamp')
