from django.shortcuts import render
from .models import Todo

# Create your views here.


def index(request):
    return render(request, 'task/index.html', {
        'todos': Todo.objects.all()
    })
