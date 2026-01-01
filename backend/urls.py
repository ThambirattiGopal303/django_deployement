from django.urls import path
from backend.views import show_data,show_employee,add_student

urlpatterns = [
    path('show',show_data,name='show'),
    path('employee',show_employee,name='employee'),
    path('student',add_student)

    # path('add',add_employee,name="add")
   
]