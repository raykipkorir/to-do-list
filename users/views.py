from django.shortcuts import redirect, render

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from users.forms import SignUpForm
from django.views.generic.edit import CreateView,FormView

# def sign_up(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             redirect("tasks:task_list")

#     else:
#         form = SignUpForm()

#     context = {"form":form}
#     return render(request,"users/sign_up.html", context)

class RegisterView(FormView):
    template_name = "users/sign_up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("tasks:task_list")
    def form_valid(self,form):
        user = form.save()
        if user:
            login(self.request,user)
        return super().form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tasks:task_list")
        return super().get(*args,**kwargs)
        