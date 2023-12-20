from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import Task
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def showTask(request, user):
    task = Task.objects.filter(title__contains=user)
    return render(request, 'show-task.html', {
        'task': task,
    })


def addTask(request, user):
    submitter = False
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        creation_date = request.POST['creation_date']
        due_date = request.POST['due_date']
        priority = request.POST['priority']
        mark = request.POST['mark']
        user = request.POST['user']
        images = request.FILES.getlist('images')
        for image in images:
            pass
    return render(request, 'add-task.html', {})


def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was an error, Try again")
            return redirect('login')

    else:
        return render(request, 'login.html', {})


def logoutUser(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('home')


def registerUser(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Registration success")
                return redirect('home')
            else:
                messages.success(request, "Registration failed")
                return redirect('register')
        else:
            messages.success(request, "Not Valid")
            return redirect('register')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {
            'form': form
        })
