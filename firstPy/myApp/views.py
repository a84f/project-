from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Contactt, Users
# Create your views here.
def home(request):
    return render(request,'home.html')
def news(request):
    return render (request,'News.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        message = request.POST.get('message')

        # Create an instance of the Contact model
        contacts = Contactt(name=name, email=email, password=password, message=message)
        contacts.save()
        messages.success(request,  'Your message is sent successfully!')
        return redirect('contact')

    return render(request, 'contact.html')






def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Create an instance of the Contact model
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "login successfully!")
            #return redirect('/login')
        else:
            messages.error(request, 'login failed')
    return render(request, 'login.html')






def about(request):
    return render (request,'about.html')
def my(request):
    return render (request,'my.html')

def why(request):
    return render (request,'why.html')



