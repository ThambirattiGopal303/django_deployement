# from rest_framework import serializers
# from backend.models import Employee,Department



# class EmployeeMiniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['id', 'name', 'email']


# class DepartmentDetailSerializer(serializers.ModelSerializer):
#     employees = EmployeeMiniSerializer(many=True, read_only=True)

#     class Meta:
#         model = Department
#         fields = ['id', 'dept_name', 'employees']
