from django.contrib.auth.forms import UserCreationForm
from .models import OrderComment, CustomUser, Order
from django import forms

class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = OrderComment
        fields = ['content']


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car', 'deadline']
        widgets = {'deadline': forms.DateInput(attrs={'type': 'datetime-local'})}


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car', 'deadline', 'status']
        widgets = {'deadline': forms.DateInput(attrs={'type': 'datetime-local'})}