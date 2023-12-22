from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('task', views.TaskList.as_view()),
    path('task/<int:pk>', views.TaskDetail.as_view()),
    path('details-task/<int:pk>', views.detailsTask, name="details-task"),
    path('update-task/<int:pk>', views.updateTask, name="update-task"),
    path('delete-task/<int:pk>', views.deleteTask, name="delete-task"),
    path('show-task', views.showTask, name="show-task"),
    path('add-task', views.addTask, name="add-task"),
    path('search-task', views.searchTask, name="search-task"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),
]
