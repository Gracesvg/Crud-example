from django import forms
from employ.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
