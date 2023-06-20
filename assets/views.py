from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Company, Employee, Device
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer

@api_view(['GET'])
def company_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def employee_list(request, company_id):
    employees = Employee.objects.filter(company__id=company_id)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def device_list(request, company_id):
    devices = Device.objects.filter(company__id=company_id)
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)
