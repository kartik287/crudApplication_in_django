from django import forms
from django.forms import fields
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name *'
        self.fields['message'].widget.attrs['placeholder'] = 'Your Message *'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email *'
        self.fields['contact_no'].widget.attrs['placeholder'] = 'Your Phone No. *'
        for field in self.fields.values():
            field.widget.attrs["class"]="form-control"