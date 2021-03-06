from django import forms
from .models import Orders, Customers, Products
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['customer', 'product', 'status']  # not required created_date because auto required


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'emil', 'mobile']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'category', 'description']
