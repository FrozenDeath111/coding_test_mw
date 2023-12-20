from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('task.urls')),
]
