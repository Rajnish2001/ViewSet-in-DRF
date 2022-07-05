from django.shortcuts import render
from ViewSetApp.models import Student
from ViewSetApp.serializers import StudentSerializers
from rest_framework import viewsets

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers