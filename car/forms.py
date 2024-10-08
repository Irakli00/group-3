from django import forms
from .models import  Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["producer","series","made_in","production_date","technical_details"]
        widgets = {
            'production_date': forms.DateInput(attrs={'type': 'date'})
        }
