from asyncio import Task
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    # def __init__(self,user, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['user'].initial = user
    class Meta:
        model = Task
        exclude = ['user']

        