from django.urls import path
from .views import cadastre_task, list_tasks, list_edit, delete_task

urlpatterns = [
    path('cadastre_task', cadastre_task, name='cadastre_task'),
    path('list_tasks', list_tasks, name='list_tasks'),
    path('list_edit/<int:pk>', list_edit, name='list_edit'),
    path('delete_task/<int:pk>/', delete_task, name='delete_task'),
]
