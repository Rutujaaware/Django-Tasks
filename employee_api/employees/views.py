from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


# Create your views here.


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-hire_date')
    serializer_class = EmployeeSerializer
