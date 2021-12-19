from django import forms
from django.forms import fields
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['emp_id'].widget.attrs['placeholder'] = 'Employee ID *'
        self.fields['name'].widget.attrs['placeholder'] = 'Full Name *'
        self.fields['address'].widget.attrs['placeholder'] = 'Address *'
        self.fields['email'].widget.attrs['placeholder'] = 'Email *'
        self.fields['mobile_no'].widget.attrs['placeholder'] = 'Phone Number *'
        for field in self.fields.values():
            field.widget.attrs["class"]="form-control"