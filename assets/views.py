from rest_framework.viewsets import ModelViewSet
from .models import Company, Employee, Device
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        company_id = self.kwargs.get('company_id') 
        if company_id:
            queryset = queryset.filter(company_id=company_id)
        return queryset

class DeviceViewSet(ModelViewSet):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        queryset = Device.objects.all()
        company_id = self.kwargs.get('company_id') 
        if company_id:
            queryset = queryset.filter(company_id=company_id)
        return queryset