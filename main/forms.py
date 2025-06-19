from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Ismingiz"}),
            'email': forms.EmailInput(attrs={'placeholder': "Email manzilingiz"}),
            'subject': forms.TextInput(attrs={'placeholder': "Mavzu"}),
            'message': forms.Textarea(attrs={'placeholder': "Xabaringizni yozing..."}),
        }