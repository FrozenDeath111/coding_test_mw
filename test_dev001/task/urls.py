from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('show-task/<str:user>', views.showTask, name="show-task"),
    path('add-task/<str:user>', views.addTask, name="add-task"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),
]
