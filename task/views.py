from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Todo
from .forms import TodoForm


def index(request):
    return render(request, 'task/index.html', {
        'todos': Todo.objects.all()
    })


def view_tasks(request, id):
    todo = Todo.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def updatetask(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=id)
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return render(request, 'task/updatetask.html',{
                'form': form,
                'success': True,
            })
        else:
            todo = Todo.objects.get(pk=id)
            form = TodoForm(instance=todo)
        return render(request, 'task/updatetask.html', {
            'form': form,
        })
