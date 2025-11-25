from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
 
 #ModelViewSet automatically provides all CRUD operations:

#list() → GET
#retrieve() → GET by id
#create() → POST
#update() → PUT
#destroy() → DELETE

