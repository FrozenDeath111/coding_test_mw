from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task.views import Taskapi, Userapi

router = DefaultRouter()
router.register("Task", Taskapi)
router.register("User", Userapi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),
    path('db/', include(router.urls)),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('task.urls')),
]
