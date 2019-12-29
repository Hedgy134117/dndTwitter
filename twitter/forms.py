from django import forms
from . import models

class CreateTweet(forms.ModelForm):
    class Meta:
        model = models.Tweet
        fields = ['content']

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['content']