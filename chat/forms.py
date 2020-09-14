from django import forms
from .models import Room, Message

class RoomForm(forms.ModelForm):
  class Meta:
    model = Room
    fields = ('name', 'users')

class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ('content', 'image')
