from django.urls import path
from .views import cadastre_task, list_tasks

urlpatterns = [
    path('cadastre_task', cadastre_task, name='cadastre_task'),
    path('list_tasks', list_tasks, name='list_tasks')
]
