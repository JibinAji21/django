from django.shortcuts import render
from django.http import HttpResponse
from .models import *

student_details=[]

# Create your views here.

def fun1():
    return HttpResponse("welcome")

def disp_std(req):
    data=student.objects.all()
    return render(req,'display_std.html',{'data':data})

def form(req):
    return render(req,'stdform.html')


