from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('task', views.TaskList.as_view()),
    path('task/<int:pk>', views.TaskDetail.as_view()),
    path('show-task', views.showTask, name="show-task"),
    path('add-task', views.addTask, name="add-task"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),
]
