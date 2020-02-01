from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="todo-home"),
    path('register/', views.register, name='register'),
    path('update_todo/<str:pk>/', views.update_todo, name="todo-update"),
    path('delete/<str:pk>/', views.delete, name="todo-delete"),
    path('about/', views.about, name="todo-about")
]
