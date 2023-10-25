from django import forms
from .models import Message, User, Category, Response


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["title", "content", "category"]

    category = forms.ModelChoiceField(queryset=Category.objects.all())


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ["content"]


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "password": forms.PasswordInput
        }
