from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        widgets = {
            "data": forms.DateInput(attrs={'type': 'date'})
        }