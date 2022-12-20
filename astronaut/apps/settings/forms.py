from django import forms
from .models import Post

class FormContactForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ["title", "content",]