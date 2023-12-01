from typing import Any
from django import forms  
from myapp.models import Student  
  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  
    
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() # for creating file input  