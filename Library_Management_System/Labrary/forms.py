from django import forms
from .models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['book_name',]
        widgets={
            'book_name': forms.TextInput(attrs={'class':'form-control'}),
        }


