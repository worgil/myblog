from django import forms
from .models import Contact
class ContactFrom(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'placeholder': 'Name'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Mail Address'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': '+954301234567'
                }
            ),
            'message': forms.TextInput(
                attrs={
                    'placeholder': 'Message'
                }
            )
        }