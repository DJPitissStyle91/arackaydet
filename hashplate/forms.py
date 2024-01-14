from django import forms
from .models import UserInput

class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['field_one', 'field_two']
        labels = {
            'field_one': 'Plakanız',
            'field_two': 'T.C. Kimlik Numaranız',
        }
