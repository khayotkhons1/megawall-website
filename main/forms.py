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

        labels = {
            "name": "",
            "email": "",
            "phone": "",
            "subject": "",
            "message": "",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ismingiz",
                    "autocomplete": "name",
                    "maxlength": "100",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email manzilingiz",
                    "autocomplete": "email",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Telefon raqamingiz",
                    "autocomplete": "tel",
                    "maxlength": "20",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Mavzu",
                    "maxlength": "200",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Xabaringizni yozing...",
                    "maxlength": "5000",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.label = ""
            field.widget.attrs.setdefault("autocomplete", "off")

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "").strip()

        if phone:
            phone = phone.replace(" ", "")

        return phone

    def clean_name(self):
        return self.cleaned_data.get("name", "").strip()

    def clean_subject(self):
        return self.cleaned_data.get("subject", "").strip()

    def clean_message(self):
        return self.cleaned_data.get("message", "").strip()