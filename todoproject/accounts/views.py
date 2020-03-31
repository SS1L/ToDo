from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm

def signupPage(request):
    form = CreatUserForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def home(request):
    #return HttpResponse('<h1>Home</h1>')
    return render(request, 'accounts/home.html')

def loginPage(request):
    return render(request, 'accounts/login.html')

def boardsPage(request):
    return render(request, 'tasks/board.html')