from django import forms
from .models import product   # ← your model name is lowercase "product"

class ProductForm(forms.ModelForm):
    class Meta:
        model = product      # ← THIS WAS MISSING
        fields = ['name', 'price', 'quantity']   # <-- include all fields

        fields = ['name','category','price','quantity','description']
        