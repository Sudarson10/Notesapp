from.models import Task
from django.forms import ModelForm
from django import forms
class Taskform(ModelForm):
    class Meta:
        model=Task
        fields="__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title','style':'display: block;width: 1200px; height: 50px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description','style':'display: block; width: 1200px; height:200px;'}),
        }