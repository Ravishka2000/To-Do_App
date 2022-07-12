from django.shortcuts import render
from .models import Todo


def index(request):
    return render(request, 'task/index.html', {
        'todos': Todo.objects.all()
    })
