from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def signupPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def loginPage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Email or password is inncorect')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    #return HttpResponse('<h1>Home</h1>')
    return render(request, 'accounts/home.html')



def boardsPage(request):
    return render(request, 'tasks/todo.html')