from django.shortcuts import render,redirect
from .models import *
from Patient.models import *
from .forms import *

# Create your views here.

def LabRegistration(request): 
    obj=LabRegisterform(request.POST,request.FILES)
    if obj.is_valid():
        data=LabRegister.objects.all().filter(LabEmail=request.POST['LabEmail'])
        print(len(data))
        if len(data)<=0: 
            obj.save()
            return redirect('LabLogin')
        else:
            return render(request,'LabRegister.html',{'messagekey':"User Already Exists"})
    return render(request,'LabRegister.html')


def LabLogin(request):
    if request.method=="POST":
        print(request.POST['LabEmail'])
        try:
            m = LabRegister.objects.get(LabEmail=request.POST['LabEmail'])
            if m.LabPassword == request.POST['LabPassword']:
                request.session['LabId'] = m.LabEmail
                request.session['Lab'] = m.LabName
                request.session['Doc'] = m.DocName

                return redirect('LabIndex')
            else:
                return render(request,'LabLogin.html',{'m':'Password incorrect'})
        except:
            return render(request,'LabLogin.html',{'n':'Lab not found'})
    return render(request,'LabLogin.html')


def LabIndex(request):
    if 'LabId' in request.session:
        a=LabRegister.objects.get(LabEmail=request.session['LabId'])
        b=Test_category.objects.all()
        return render(request,'LabIndex.html',{'a':a,'b':b,'c':len(b)})
    else:
        return redirect('LabLogin')


def LabLogout(request):
    if 'LabId' in request.session:
        del request.session['LabId']
        return redirect('LabLogin')
    else:
        return redirect('LabLogin')

    
def LabProfile(request):
    if 'LabId' in request.session:
        a=LabRegister.objects.get(LabEmail=request.session['LabId'])
        if request.POST:
            name=request.POST['name']
            password=request.POST['passowrd']
            CP=request.POST['CP']
            a.LabName=name
            if password==CP:
                a.LabPassword=password
                a.save()
                return redirect('LabIndex')
            else:
                return render(request, 'LabProfile.html', {'Wrong':'Passwords dont match'})
        else:
            return render(request,'LabProfile.html',{'n':a})
    else:
        return redirect('LabLogin')
    

def PatientAppointment(request):
    results=Appointment.objects.filter(status='pending')
    return render(request,'PatientAppointment.html',{'book':results})
    

def EditAppointment(request,id):
    if 'LabId' in request.session.keys():
        a=LabRegister.objects.get(LabEmail=request.session['LabId'])
        book=Appointment.objects.get(pk=id)
        if request.POST:
            book.status=request.POST['booked']
            book.save()
            return redirect('PatientAppointment')
        return render(request,'EditAppointment.html',{'book':book,'owner_data':a})
    else:
        return redirect('LabLogin')
    

def approvedAppointment(request):
    if 'LabId' in request.session:
        b=Appointment.objects.filter(status='approved') & Appointment.objects.filter(appointment_booked=False)
       
        return render(request,'approvedAppointment.html',{'b':b})
    else:
        return redirect('LabLogin')
    

def takeTest(request,id):
    if 'LabId' in request.session:
        a=request.session['Doc']
        c=request.session['Lab']
        b=Appointment.objects.get(pk=id)
        form =Testform(request.POST)
        if form.is_valid():
            b.appointment_booked=request.POST['test']   
            form.save()
            b.save()            
            return redirect('LabIndex')
        return render(request,'takeTest.html',{'a':a,'b':b,'c':c})
    else:
        return redirect('LabLogin')


def viewCat(request):
    if 'LabId' in request.session:
        b=Name_category.objects.all()
        return render(request,'viewCat.html',{'b':b})
    else:
        return redirect('LabLogin')


def addCat(request):
    a=Name_category.objects.all()
    if 'LabId' in request.session:
        if request.POST:
            name=request.POST['name']
            b=Name_category()
            b.category_name=name
            b.save()
            return redirect('viewCat')
        return render(request,'addCat.html',{'n':a})
    else:
        return redirect('LabLogin')


def editCat(request,id):
    if 'LabId' in request.session:
        a=Name_category.objects.get(pk=id)
        if request.POST:
            name=request.POST['name']
            a.category_name=name
            a.save()
            return redirect('viewCat')
        return render(request,'editCat.html',{'n':a})
    else:
        return redirect('LabLogin')
    

def deleteCat(request,id):
    if 'LabId' in request.session:
        obj=Name_category.objects.get(pk=id)
        obj.delete()
        return redirect('viewCat')
    return redirect('LabLogin')


def viewFeedback(request):
    if 'LabId' in request.session:
        obj=UserFeedback.objects.all()
        return render(request,'viewFeedback.html',{'b':obj})
    return redirect('LabLogin')


def showFeedback(request,id):
    if 'LabId' in request.session:
        obj=UserFeedback.objects.get(id=id)
        return render(request,'showFeedback.html',{'b':obj})
    return redirect('LabLogin')


def viewTestLab(request,id):
    if 'LabId' in request.session:
        b=Test_category.objects.get(pk=id)
        c=UserRegister.objects.get(email=b.email)        
        return render(request,'viewTestLab.html',{'b':b,'c':c})
    else:
        return redirect('LabLogin')


def deleteTest(request,id):
    if 'LabId' in request.session:
        obj=Test_category.objects.get(pk=id)
        obj.delete()
        return redirect('LabIndex')
    return redirect('LabLogin')