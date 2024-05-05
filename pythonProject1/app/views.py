from django.shortcuts import render, get_object_or_404, redirect
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


def list_edit(request, pk):
    task = get_object_or_404(Tasks, pk=pk)

    if request.method == "POST":
        task_form_edit = TaskForm(request.POST, instance=task)
        if task_form_edit.is_valid():
            task_form_edit.save()

    else:
        task_form_edit = TaskForm(instance=task)

    return render(request, 'list_edit.html', {'task_form_edit': task_form_edit})


def delete_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('list_tasks')

    return render(request, 'confirm_delete_task.html', {'task': task})