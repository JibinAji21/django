from django import forms
from .models import Project_user

class normal_form(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()

class Model_form(forms.ModelForm):
    class Meta:
        model=Project_user
        fields='__all__'