from django.shortcuts import render
from django.http import HttpResponse

def signupPage(request):
    return render(request, 'accounts/signup.html')

def home(request):
    #return HttpResponse('<h1>Home</h1>')
    return render(request, 'accounts/home.html')

def loginPage(request):
    return render(request, 'accounts/login.html')