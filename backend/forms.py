from django import forms
from backend.models import Employee

class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

        widgets = {
            'emp_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
                'style':'width:200px'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                "placeholder":'email Id'
            }),
            "department":forms.TextInput(attrs={
            'class':'form-control',
            
            })}

        