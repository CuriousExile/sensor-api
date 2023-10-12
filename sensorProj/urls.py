from django.contrib import admin
from django.urls import path, include
from temperature.views import TemperatureDataViewSet
from rest_framework.routers import DefaultRouter
from temperature.views import TemperatureDataView, TemperatureDataListView

router = DefaultRouter()
router.register(r'temperature', TemperatureDataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/temperature/now', TemperatureDataView.as_view(), name='temperature-data'),
    path('api/temperature/selection/', TemperatureDataListView.as_view(), name='temperature-list-date-range')
]