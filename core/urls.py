from django.urls import path, include
from rest_framework import routers
from . import views 

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Asset Tracker API",
        default_version='v1',
    ),
    public=True, 
    permission_classes=[permissions.AllowAny], 
)


router = routers.DefaultRouter()
router.register('companies', views.CompanyViewSet)
router.register('employees', views.EmployeeViewSet)
router.register('device-types', views.DeviceTypeViewSet)
router.register('device', views.DeviceViewSet)
router.register('device-assignment', views.DeviceAssignment)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]