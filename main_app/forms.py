from django import forms
from .models import Translation

class TranslationForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = ['language', 'translated_text']
