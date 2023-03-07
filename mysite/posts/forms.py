from django import forms

from .models import Posts


class PostForms(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('text', 'image')