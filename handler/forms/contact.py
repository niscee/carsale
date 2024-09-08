from django import forms
from handler.models import ContactUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name", "phone", "email", "message"]
