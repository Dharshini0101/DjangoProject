from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields= ('emp_id','emp_name','designation','no_of_days_worked','daily_salary')
        labels = {
            'emp_id':'EMP. Id',
            'emp_name':'EMP. Name',
            'designation':'Designation',
            'no_of_days_worked':'Working Days',
            'daily_salary':'Daily Salary',
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['designation'].empty_label = "Select"
        self.fields['emp_id'].required = False