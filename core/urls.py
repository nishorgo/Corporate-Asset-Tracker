from django.urls import path, include
from rest_framework import routers
from . import views 


router = routers.DefaultRouter()
router.register('companies', views.CompanyViewSet)
router.register('employees', views.EmployeeViewSet)
router.register('device-types', views.DeviceTypeViewSet)
router.register('device', views.DeviceViewSet)
router.register('device-assignment', views.DeviceAssignment)

urlpatterns = [
    path('', include(router.urls)),
]