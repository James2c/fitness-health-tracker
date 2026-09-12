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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = None

    def clean_date(self):

        date = self.cleaned_data.get("date")

        if not date or not self.user:
            return date

        existing_entry = WeightEntry.objects.filter(
            user=self.user,
            date=date,
        ).exclude(
            pk=self.instance.pk,
        ).exists()

        if existing_entry:
            raise forms.ValidationError(
                "You already have a weight entry for this date."
            )

        return date