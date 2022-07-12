from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task_title', 'description', 'due_date', 'status']
        labels = {
            'task_title': 'Title',
            'description': 'Description',
            'due_date': 'Due Date',
        }
        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
