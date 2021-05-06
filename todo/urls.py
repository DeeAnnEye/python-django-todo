from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /tasks/
    path('tasks/', views.tasks, name='tasks'),
     # ex: /add_task/
    path('addtask/', views.addtask, name='addtask'),
]