from django.shortcuts import render
from .forms import TaskForm
from .models import Tasks


# Create your views here.

def cadastre_task(request):
    if request.method == "POST":
        form_task = TaskForm(request.POST)
        if form_task.is_valid():
            form_task.save()
    else:
        form_task = TaskForm()
    return render(request, 'form_cadastro.html', {'form_task': form_task})


def list_tasks(request):
    tarefas = Tasks.objects.all()
    return render(request, 'list_task.html', {'tarefas': tarefas})
