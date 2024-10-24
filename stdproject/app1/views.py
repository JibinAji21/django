from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

student_details=[]

# Create your views here.

def fun1():
    return HttpResponse("welcome")

def disp_std(req):
    data=student.objects.all()
    return render(req,'display_std.html',{'data':data})

def add_std(req):
    if req.method=='POST':
        roll=req.POST["roll_no"]
        std_name=req.POST['name']
        std_age=req.POST['age']
        std_email=req.POST['email']
        std_phone=req.POST['phone']
        data=student.objects.create(roll_no=roll,name=std_name,age=std_age,email=std_email,phone=std_phone)
        data.save()
        return redirect(disp_std)
    else:
        return redirect(disp_std)
    
def edit_std(req,id):
    data=student.objects.get(pk=id)
    if req.method=='POST':
        roll=req.POST['roll_no']
        std_name=req.POST['name']
        std_age=req.POST['age']
        std_email=req.POST['email']
        std_phone=req.POST['phone']
        student.objects.filter(pk=id).update(roll_no=roll,name=std_name,age=std_age,email=std_email,phone=std_phone)
        return redirect(disp_std)
    else:
        return render(req,'edit_std.html',{'data':data})
       

