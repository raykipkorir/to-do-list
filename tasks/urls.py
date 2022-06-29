from django.urls import path
from . import views

app_name  = "tasks"
urlpatterns = [
    path('',views.TaskList.as_view(), name = "task_list"),
    path('taskdetail/<int:pk>/',views.TaskDetail.as_view(),name = "task_detail"),
    path('taskcreate/',views.TaskCreate.as_view(),name = "task_create"),
    path('taskupdate/<int:pk>/', views.TaskUpdate.as_view(), name = "task_update"),
    path('taskdelete/<int:pk>/', views.TaskDelete.as_view(), name = "task_delete"),
    

]
