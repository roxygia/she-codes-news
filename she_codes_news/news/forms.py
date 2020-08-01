from django import forms
from django.forms import ModelForm
from .models import NewsStory
from .models import *

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content', 'image_url']
        widgets = {
            'pub_date': forms.DateInput(
                format=('%m/%d/%Y'), 
                attrs={
                    'class':'form-control', 
                    'placeholder':'Select a date',
                    'type':'date'})
        }

    