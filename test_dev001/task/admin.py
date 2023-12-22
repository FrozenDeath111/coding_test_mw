from django.contrib import admin
from .models import Task, UserList

# Register your models here.
#admin.site.register(Task)
admin.site.register(UserList)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'mark')
    ordering = ('priority',)
    search_fields = ('creation_date', 'due_date', 'title')
