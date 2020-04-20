from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreateUserForm
from .forms import TaskForm
from .models import *

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
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('board')
            else:
                messages.error(request, 'Invalid login or password')
        else:
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'accounts/home.html')

@login_required(login_url='home')
def boardsPage(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('board'))
    else:
        form = TaskForm()
        

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/todo.html', context)

@login_required(login_url='home')
def updateTask(request, index):
    task = Task.objects.get(id=index)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('board')
    return render(request, 'tasks/update_todo.html', {'form': form})

@login_required(login_url='home')
def deleteTask(request, index):
    task = Task.objects.get(id=index)
    if request.method == 'POST':
        task.delete()
        return redirect('board')

    context = {'task': task}
    return render(request, 'tasks/todo.html', context)