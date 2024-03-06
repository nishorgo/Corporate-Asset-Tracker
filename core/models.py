from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)


class DeviceType(models.Model):
    name = models.CharField(max_length=50)


class Device(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.PROTECT)
    serial_number = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class DeviceAssignment(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    condition_out = models.TextField(blank=True)
    condition_in = models.TextField(blank=True)
