from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_tasks'] = self.model.objects.filter(user = self.request.user).order_by('completed')
            context["count"]  = self.request.user.task_set.filter(completed = False).count()

            search_input = self.request.GET.get("search-area") 
            if search_input:
                context['user_tasks'] = self.request.user.task_set.filter(title__icontains = search_input)

            context['search_input'] = search_input
            return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = "task"

class TaskCreate(LoginRequiredMixin,CreateView):
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task_list")

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    context_object_name = "task"
    form_class = TaskForm

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks:task_list")

