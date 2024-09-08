from django import forms
from handler.models import Purchase, CustomPurchase, ListedProductPurchase


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ["product", "user", "notes"]
        widgets = {
            "product": forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "notes": forms.Textarea(
                attrs={"placeholder": "Add any notes here...", "rows": 4}
            ),
        }

class ListedProductPurchaseForm(forms.ModelForm):
    class Meta:
        model = ListedProductPurchase
        fields = ["product", "user", "notes"]
        widgets = {
            "product": forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "notes": forms.Textarea(
                attrs={"placeholder": "Add any notes here...", "rows": 4}
            ),
        }


class CustomPurchaseForm(forms.ModelForm):
    class Meta:
        model = CustomPurchase
        fields = ["product_image", "user", "notes"]
        widgets = {
            "user": forms.HiddenInput(),
            "notes": forms.Textarea(
                attrs={"placeholder": "Add any notes here...", "rows": 4}
            ),
        }
