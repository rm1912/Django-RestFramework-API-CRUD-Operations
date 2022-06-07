from django.urls import path
from . import views

urlpatterns = [
    path('new/',views.taskcreate, name='Task Create'),
    path('all/',views.taskList, name='Task List'),
]