from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .forms import RegisterForm, TaskForm
from .models import Task
from .serializers import UserSerializer, TaskSerializer


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


class TaskList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        #print(serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Task Added successfully")
            return render(request, 'add-task.html', {})
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def addTask(request):
    return render(request, 'add-task.html', {})


def showTask(request):
    user = request.user
    tasks = Task.objects.filter(user=user.id).values()
    return render(request, 'show-task.html', {
        'tasks': tasks,
    })


def detailsTask(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'details-task.html', {
        'task': task,
    })


def updateTask(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return render(request, 'details-task.html', {
            'task': task,
        })

    return render(request, 'update-task.html', {
        'task': task,
        'form': form
    })


def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect("show-task")


def searchTask(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        user = request.user
        tasks = Task.objects.filter(title__contains=searched).filter(user=user.id).values()

        return render(request, 'search-task.html', {
            'searched': searched,
            'tasks': tasks
        })

    else:
        return render(request, 'search-task.html', {})


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


#Class based view
class Taskapi(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class Userapi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
