from django.urls import path,include
from . import views

urlpatterns = [
    path('employee/',views.employee_form),
    path('',views.employee_form,name = 'emp_insert'), #get and post req for insert operations
    path('<int:id>/',views.employee_form,name = 'employee_update'), #get and post req for update operations
    path('list/',views.employee_list,name = 'emp_list'),#get req to retrieve and display all records
    path('employee/',views.read_file),
]