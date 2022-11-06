from django.forms import ModelForm, EmailInput, TextInput, Textarea
from . models import ContactMessage


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = {'first_name', 'last_name', 'email', 'phone_number', 'message'}

        widgets = {
            'first_name': TextInput(attrs={'class': 'half', 'placeholder': 'First name'}),
            'last_name': TextInput(attrs={'class': 'half', 'placeholder': 'Last name'}),
            'email': EmailInput(attrs={'class': 'half', 'placeholder': 'Your email address'}),
            'phone_number': TextInput(attrs={'class': 'half', 'placeholder': 'Your phone number'}),
            'message': Textarea(attrs={'class': 'full', 'placeholder': 'Type your message here', 'rows':'5'}),
        }

        