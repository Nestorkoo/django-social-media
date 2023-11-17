from django import forms
from django.forms import FileInput, ModelForm, Textarea, TextInput

from .models import AddPost


class AddPostForm(ModelForm):
    class Meta:
        model = AddPost
        fields = [
            'title',
            'image',
            'full_text',
        ]
        
        widgets = {
            'title': TextInput(attrs={
                'class': 'title',
                'placeholder': 'Назва аккаунту',
            }),
            'image': FileInput(),  # Замінюємо ImageField на FileInput

            'full_text': Textarea(attrs={
                'class': 'full_text',
                'placeholder': 'Опис',
            }),

            
        }