from django import forms
from .models import ChatMessage


class ChatForm(forms.Form):
    model = ChatMessage
    userInput = forms.CharField(required=False)
