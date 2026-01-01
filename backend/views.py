from django.shortcuts import render

# Create your views here.
def show_data(request):
    return render(request,"index.html")

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Employee, Department
# from .serializers import EmployeeSerializer, DepartmentSerializer

# @api_view(['POST'])
# def add_employee(request):
#     serializer = EmployeeSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




