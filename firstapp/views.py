from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages as m


# Create your views here.
# def home(request):
    # return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request,'gallery.html')


def result(request):
    return render(request,'result.html')


def courses(request):
    return render(request,'courses.html')

def student_enquiry(request):
    return render(request,'student_enquiry.html')

def signup(request):
    if request.method=='POST':
        f=RegistrationForm(request.POST)
        if f.is_valid():
            f.save()
            
            return redirect('login')
        else:
            m.warning(request, '')
            

    else:
        
        f= RegistrationForm()
        
    return render(request,'signup.html',{'form': f})





def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passd= request.POST.get('password')
        user=authenticate(request,username=uname,password=passd)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('studentenquiry')
        
            
        else:
             m.warning(request,'')
             return render(request,'login.html')
    return render(request,'login.html')
   


def gallery(request):
    gallery=Gallery.objects.all()
    context={'gallery':gallery}
    return render(request,'gallery.html',context)

def result(request):
    result=Result.objects.all()
    context={'result':result}
    return render(request,'result.html',context)


def index(request):
    index=Notice.objects.all()
    context={'notice':index}
    return render(request,'index.html',context)


from django.shortcuts import render, redirect
from .models import Review

@login_required(login_url=signup)
def review_rate(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        rate = request.POST.get('rate')
        if rate and comment:
            review = Review(user=request.user, comment=comment, rate=rate)
            review.save()
            
        else:
           
            return redirect('about')  # Redirect to a success page or return a success message
    
    return render(request, 'about.html')  # Render the form for GET requests

    
from .models import Review

def index(request):
    reviews = Review.objects.all()
    return render(request, 'index.html', {'reviews': reviews})


from datetime import datetime
@login_required(login_url=signup)
def student_enquiry(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        date= request.POST.get('dob')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        board=request.POST.get('board')
        std=request.POST.get('std')
        sclname=request.POST.get('sclname')
        scltime=request.POST.get('scltime')
        marks=request.POST.get('marks')

        sten=Enquiry(name=name,date=date,email=email,mobile=mobile,gender=gender,address=address,board=board,std=std,sclname=sclname,scltime=scltime,marks=marks)
        sten.save()
    return render(request, 'student_enquiry.html')


def contactus(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')
        

        contactus=Contact(name=name,email=email,message=message)
        contactus.save()
    return render(request, 'contact.html')

def logout_view(request):
    logout(request)
    return redirect('/')