from django.contrib.auth.forms import UserCreationForm
from .models import OrderComment
from .models import CustomUser
from django import forms

class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = OrderComment
        fields = ['content']


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']