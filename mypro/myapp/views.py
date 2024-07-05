from django.shortcuts import render,redirect
from .models import *

def home(request):
    return render(request,'index.html')


def education(request):
    return render(request,'education.html')

def skills(request):
    return render(request,'skills.html')

def experience(request):
    info=IE.objects.all()
    work=WE.objects.all()
    return render(request,'experience.html',{'info':info},)
    return render(request,'experience.html',{'work':work})

def projects(request):
    info=MP.objects.all()
    return render(request,'projects.html',{'info':info})

def cont(request):
    
       a=request.POST.get('user') 
       b=request.POST.get('email')
       c=request.POST.get('number')
       d=request.POST.get('message')
       info=contact(name=a,email=b,phone=c,message=d)
       info.save();

       return redirect('con')  
   
def con(request):
     return render(request,'contact.html')