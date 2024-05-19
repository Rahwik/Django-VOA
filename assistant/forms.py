from django import forms
from .models import RememberedMessage

class RememberMessageForm(forms.ModelForm):
    class Meta:
        model = RememberedMessage
        fields = ['message']
