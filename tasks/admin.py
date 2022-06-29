from django.contrib import admin

from tasks.models import Task
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','description','completed','created']