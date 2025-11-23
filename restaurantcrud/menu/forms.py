from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'category', 'price', 'description', 'is_available']
