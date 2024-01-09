from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_institute(request):
    io=input()
    bo=input()
    IO=Institute.objects.get_or_create(inst_name=io,branch=bo)[0]
    IO.save()
    return HttpResponse(request,'data inserted')

def insert_trainer(request):
    to=input()
    ti=input()
    TO=Trainer.objects.get_or_create(tname=to,tid=ti)[0]
    TO.save()
    return HttpResponse(request,'data inserted')

def insert_student(request):
    sn=input()
    si=input()
    sm=input()
    sf=input()
    SO=Student.objects.get_or_create(sname=sn,sid=si,smob=sm,sfee=sf)
    return HttpResponse(request,'data inserted')

def insert_course(request):
    cn=input()
    io=input()
    to=input()
    so=input()
    IC=Institute.objects.get(inst_name=io)
    TC=Trainer.objects.get(tid=to)
    SC=Student.objects.get(sid=so)
    CO=Course.objects.get_or_create(cname=cn,inst_name=IC,tid=TC,sid=SC)[0]
    CO.save()
    return  HttpResponse(request,'data inserted')

def display_institute(request):
    DI=Institute.objects.all()
    d={'institute':DI}
    return render(request,'display_institute.html',d)

def display_trainer(request):
    DT=Trainer.objects.all()
    d={'trainer':DT}
    return render(request,'display_trainer.html',d)

def display_student(request):
    DS=Student.objects.all()
    d={'student':DS}
    return render(request,'display_student.html',d)

def display_course(request):
    DC=Course.objects.all()
    d={'course':DC}
    return render(request,'display_course.html',d)