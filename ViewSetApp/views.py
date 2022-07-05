from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        #know the some basic details than use the following oprations like "self.basename","self.action"
        print("**********LIST***********")
        print("Basename : ",self.basename)
        print("Action : ",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)

        stu = Student.objects.all()
        serializer = StudentSerializers(stu,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        #know the some basic details than use the following oprations like "self.basename","self.action"
        print("**********Retrieve***********")
        print("Basename : ",self.basename)
        print("Action : ",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)
        id=pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializers(stu)
        return Response(serializer.data)
    
    def create(self, request):
        #know the some basic details than use the following oprations like "self.basename","self.action"
        print("**********Create***********")
        print("Basename : ",self.basename)
        print("Action : ",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        #know the some basic details than use the following oprations like "self.basename","self.action"
        print("**********Update***********")
        print("Basename : ",self.basename)
        print("Action : ",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)
        id=pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializers(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        print("**********Partial Update***********")
        print("Basename : ",self.basename)
        print("Action : ",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Partialy Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        print("**********Destroy***********")
        print("Basename : ",self.basename)
        print("Action : ",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name : ",self.name)
        print("Description : ",self.description)
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Delered'}, status=status.HTTP_200_OK)
