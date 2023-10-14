import glob
import time
from django.http import Http404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from temperature.models import TemperatureData
from temperature.serializers import TemperatureDataSerializer
from rest_framework import generics
from django.utils.datetime_safe import datetime

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

class TemperatureDataViewSet(viewsets.ModelViewSet):
    queryset = TemperatureData.objects.all()
    serializer_class = TemperatureDataSerializer


class TemperatureDataView(APIView):

    def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp():
        lines = TemperatureDataView.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = TemperatureDataView.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c
        
    def get(self, request):
        current_temperature = TemperatureDataView.read_temp()
        temperature_data = TemperatureData(sourcename='garnele', temperature=current_temperature)
        temperature_data.save()

        serializer = TemperatureDataSerializer(temperature_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class TemperatureDataListView(generics.ListAPIView):
    serializer_class = TemperatureDataSerializer

    def get(self):
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

class LatestTemperatureView(generics.RetrieveAPIView):
    serializer_class = TemperatureDataSerializer

    def get_object(self):
        return TemperatureData.objects.latest('timestamp')