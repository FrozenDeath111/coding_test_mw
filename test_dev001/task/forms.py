from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Task
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'creation_date', 'due_date', 'image', 'priority', 'mark')

        priority_choices = (
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High')
        )

        mark_choices = (
            ('Due', 'Due'),
            ('Done', 'Done')
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'creation_date': forms.DateInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-select'}, choices=priority_choices),
            'mark': forms.Select(attrs={'class': 'form-select'}, choices=mark_choices)
        }
