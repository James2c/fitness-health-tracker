from django import forms

from .models import WeightEntry


class WeightEntryForm(forms.ModelForm):

    class Meta:
        model = WeightEntry

        fields = [
            "date",
            "weight",
            "notes",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),

            "weight": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "e.g. 85.50",
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Optional notes...",
                }
            ),
        }