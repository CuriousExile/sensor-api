from django.contrib import admin
from django.urls import path, include
from temperature.views import TemperatureDataViewSet
from rest_framework.routers import DefaultRouter
from temperature.views import TemperatureDataView, TemperatureDataListView, TemperatureDataCreateView, LatestTemperatureView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/temperature/create', TemperatureDataCreateView.as_view(), name='create-temperature-data'),
    path('v1/temperature/now', TemperatureDataView.as_view(), name='temperature-data'),
    path('v1/temperature/range', TemperatureDataListView.as_view(), name='temperature-list-date-range'),
    path('v1/temperature/latest', LatestTemperatureView.as_view(), name='latest-temperature')
]