from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact

        fields = [
            "name",
            "email",
            "phone",
            "subject",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ismingiz",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email manzilingiz",
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Telefon raqamingiz",
            }),

            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Mavzu",
            }),

            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Xabaringizni yozing...",
            }),

        }