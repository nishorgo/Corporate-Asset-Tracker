
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Company, DeviceType, Device, Employee, DeviceAssignment
from .serializers import CompanySerializer, DeviceTypeSerializer, DeviceSerializer, DeviceAssignmentSerializer, EmployeeSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser]


class DeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
    permission_classes = [IsAdminUser]


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.select_related('company').all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['company']



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('company').all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['company']


class DeviceAssignmentViewSet(viewsets.ModelViewSet):
    queryset = DeviceAssignment.objects.prefetch_related('device', 'employee').all()
    serializer_class = DeviceAssignmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['device', 'employee', 'device__company', 'device__device_type']
    search_fields = ['device', 'employee']
    ordering_fields = ['checkout_date', 'return_date']

    def perform_create(self, serializer):
        device = serializer.validated_data['device']
        if device.company != serializer.validated_data['employee'].company:
            raise serializer.ValidationError("Device and employee must belong to the same company.")
        serializer.save()
