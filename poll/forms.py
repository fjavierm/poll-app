from django import forms

from .models import *


class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = (
            'question', 'choice_1', 'choice_2', 'choice_3'
        )
        widgets = {
            'question': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'choice_1': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'choice_2': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'choice_3': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
