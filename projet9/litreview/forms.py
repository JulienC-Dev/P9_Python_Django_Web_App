from .models import Ticket, Review
from django.forms import ModelForm
from django import forms


class CreateTicket(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']


class ModifiedTicket(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']


class CreateCritique(ModelForm):
    class Meta:
        model = Review
        exclude = ['ticket', 'user', 'answer_review']
        CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
        widgets = {
            'rating': forms.RadioSelect(choices=CHOICES)
        }







