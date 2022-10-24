from django.forms import fields
from django import forms
from django import forms
from employee.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields= "__all__"