from django import forms
from handler.models import ListedProduct

class ListedProductForm(forms.ModelForm):
    class Meta:
        model = ListedProduct
        fields = ['title', 'image', 'description', 'price', 'category', 'availability', 'condition', 'user']
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Add some description here...',
                    'rows': 4
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'custom-select',
                    'data-placeholder': 'Select a category'
                }
            ),
            'condition': forms.Select(
                attrs={
                    'class': 'custom-select',
                    'data-placeholder': 'Select a condition'
                }
            ),
            "user": forms.HiddenInput()
        }

