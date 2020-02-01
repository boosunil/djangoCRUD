from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created and you are able to login')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def home(request):
    todos = Todo.objects.all()

    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'todos': todos, 'form': form}

    return render(request, 'todo/home.html', context)


@login_required
def update_todo(request, pk):
    todos = Todo.objects.get(id=pk)

    form = TodoForm(instance=todos)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todos)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}

    return render(request, 'todo/update_todo.html', context)


@login_required
def delete(request, pk):

    item = Todo.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item': item}

    return render(request, 'todo/delete.html', context)


def about(request):

    return render(request, 'todo/about.html')
