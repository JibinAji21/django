from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.

def normal_form_fun(req):
    if req.method=='POST':
        form1=normal_form(req.POST)
        if form1.is_valid():
            name=form1.cleaned_data['name']
            age=form1.cleaned_data['age']
            email=form1.cleaned_data['email']
            data=Project_user.objects.create(name=name,age=age,email=email)
            data.save()

    form=normal_form()
    return render(req,'normal_form.html',{'form':form})
    