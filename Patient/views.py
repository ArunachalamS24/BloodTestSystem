from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from Lab.models import *
from Lab.forms import *


# Create your views here.

def Register(request):
    if request.method=='POST':
        a = UserRegister()
        a.name=request.POST['name']
        a.gender=request.POST['gender']
        a.age=request.POST['age']
        a.email=request.POST['email']
        a.password=request.POST['password']
        a.phnNo=request.POST['phnNo']
        a.address=request.POST['address']
        b = UserRegister.objects.filter(email = request.POST['email'])
        if b:
            return render(request, 'register.html',{'already':'user already exists'} )
        else:
            a.save()
            return redirect('index')
    else:
        return render(request, 'register.html')
    
def Login(request):
    if request.method=='POST':
        try:
            a=UserRegister.objects.get(email = request.POST['email'])
            if request.POST['password'] == a.password:
                request.session['UserId'] = a.pk
                request.session['ACTIVE'] = a.email
                return redirect('index')
            else:
                return render(request, 'login.html', {'wrong':'Wrong Password entered'})
        except:
            return render(request, 'login.html',{'wrong1':'user doesnt exist'})
    else:
        return render(request,'login.html')
    
def Logout(request):
    if 'ACTIVE' in request.session:
        del request.session['ACTIVE']
        return redirect('login')
    return redirect('login')


def Index(request):
    if 'ACTIVE' in request.session:
        a = UserRegister.objects.get(id = request.session['UserId'])
        b = Test_category.objects.filter(email = request.session['ACTIVE'])
        return render(request,'index.html',{'USER':a , 'TEST':b})
    else:
        return redirect('login')

def UserProfile(request):
    if 'ACTIVE' in request.session.keys():
        a = UserRegister.objects.get(id = request.session['UserId'])
        if request.POST:
            Name = request.POST['name']
            Email = request.POST['email']
            Passcode = request.POST['password']
            CP = request.POST['confirmPassword']
            a.name=Name
            a.email=Email
            if Passcode != CP:
                return render(request, 'UserProfile.html',{'Wrong':'Passwords dont match'})
            else:
                a.password = Passcode
                a.save()
                return redirect('index')
        else:
            return render(request,'UserProfile.html',{'n':a})
    else:
        return redirect('login')
    

import datetime
from django.utils.dateparse import parse_datetime

def bookAppointment(request):
    if 'ACTIVE' in request.session.keys():
        a=Name_category.objects.all()
        b=UserRegister.objects.get(id=request.session['UserId'])
        form = appointmentform(request.POST)
        if form.is_valid():
            c=Appointment.objects.filter(email=request.POST['email'])  & Appointment.objects.filter(status='pending')
            if len(c)<=0:
                cDate = datetime.datetime.today()
                print(cDate)
                postDate = request.POST['schedule']
                print(postDate)
                postDateArray = postDate.split("T")
                print(postDateArray)
                cDateArray = str(cDate).split(" ")
                print(cDateArray)
                if parse_datetime(postDateArray[0]) >= parse_datetime(cDateArray[0]):    
                    form.save()
                    messages.success(request,'Your appoinement is booked.')
                    return redirect('bookAppointment')
                else:
                    return render(request,'bookAppointment.html',{'form':form,'a':a,'b':b,'m':'select future date only'})
            else:
                return render(request,'bookAppointment.html',{'form':form,'a':a,'b':b,'m':'appointment alredy booked'})
        else:
            return render(request,'bookAppointment.html',{'form':form,'a':a,'b':b})
    else:
        return redirect('login')
    

def appointmentStatus(request):
    if 'ACTIVE' in request.session.keys():
        b=Appointment.objects.filter(email=request.session['ACTIVE'])
        return render(request,'appointmentStatus.html',{'b':b})
    else:
        return redirect('login')

def deleteAppointment(request,id):
    if 'UserId' in request.session.keys():
        obj=Appointment.objects.get(pk=id)
        obj.delete()
        return redirect('appointmentStatus')
    return redirect('login')

def Feedback(request):
    if 'ACTIVE' in request.session.keys():
        c=UserRegister.objects.get(id=request.session['UserId'])
        if request.POST:
            Username=request.POST['name']
            Useremail=request.POST['email']
            feedback=request.POST['Feedback']
            a=UserFeedback()
            a.name=Username
            a.email=Useremail
            a.feedback=feedback
            a.save()
            return redirect('index')
        return render(request,'feedback.html',{'n':c})
    else:
        return redirect('login')


def viewTest(request,id):
    if 'ACTIVE' in request.session.keys():
        b=Test_category.objects.get(pk=id)
        c=UserRegister.objects.get(email=b.email)
        
        return render(request,'viewTest.html',{'b':b,'c':c})
    else:
        return redirect('login')