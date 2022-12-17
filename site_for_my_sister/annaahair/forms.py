from .models import Annaahair_review
from django.forms import ModelForm, TextInput, Textarea


class Annaahair_reviewForm(ModelForm):
    class Meta:
        model = Annaahair_review
        fields = ['title1', 'review1']
        widgets = {
            'title1': TextInput(attrs={
                'class': 'form',
                'placeholder': 'Введите свое имя:',
            }),
            'review1': Textarea(attrs={
                'class': 'form',
                'placeholder': 'Введите комментарий:',
            }),
        }
