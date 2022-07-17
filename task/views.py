from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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


def updatetask(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'task/updatetask.html', context)


def changestatus(request, pk):
    todo = Todo.objects.get(id=pk)

    if todo.status:
        todo.status = False
    else:
        todo.status = True
    todo.save()

    return redirect('index')
