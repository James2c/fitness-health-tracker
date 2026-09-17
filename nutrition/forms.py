from django import forms

from .models import NutritionEntry, NutritionGoal



class NutritionEntryForm(forms.ModelForm):

    class Meta:
        model = NutritionEntry
        fields = [
            "date",
            "food_name",
            "serving_size",
            "calories",
            "protein",
            "carbohydrates",
            "fat",
            "notes",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "food_name": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Chicken breast"
                }
            ),
            "serving_size": forms.TextInput(
                attrs={
                    "placeholder": "e.g. 150 g"
                }
            ),
            "calories": forms.NumberInput(
                attrs={
                    "placeholder": "e.g. 250"
                }
            ),
            "protein": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "e.g. 46.50"
                }
            ),
            "carbohydrates": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "e.g. 0.00"
                }
            ),
            "fat": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "e.g. 5.00"
                }
            ),
            "notes": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Optional notes..."
                }
            ),
        }

    def clean_calories(self):
        calories = self.cleaned_data.get("calories")

        if calories is not None and calories > 10000:
            raise forms.ValidationError(
                "Calories cannot exceed 10,000."
            )

        return calories

    def clean_protein(self):
        protein = self.cleaned_data.get("protein")

        if protein is not None and protein > 1000:
            raise forms.ValidationError(
                "Protein cannot exceed 1,000 g."
            )

        return protein

    def clean_carbohydrates(self):
        carbohydrates = self.cleaned_data.get("carbohydrates")

        if carbohydrates is not None and carbohydrates > 1000:
            raise forms.ValidationError(
                "Carbohydrates cannot exceed 1,000 g."
            )

        return carbohydrates

    def clean_fat(self):
        fat = self.cleaned_data.get("fat")

        if fat is not None and fat > 1000:
            raise forms.ValidationError(
                "Fat cannot exceed 1,000 g."
            )

        return fat


class NutritionGoalForm(forms.ModelForm):

    class Meta:
        model = NutritionGoal
        fields = [
            "daily_calories",
            "daily_protein",
            "daily_carbohydrates",
            "daily_fat",
        ]

        widgets = {
            "daily_calories": forms.NumberInput(
                attrs={
                    "placeholder": "e.g. 2000"
                }
            ),
            "daily_protein": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "e.g. 150"
                }
            ),
            "daily_carbohydrates": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "e.g. 250"
                }
            ),
            "daily_fat": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "e.g. 65"
                }
            ),
        }

    def clean_daily_calories(self):
        calories = self.cleaned_data.get("daily_calories")

        if calories is not None and calories > 10000:
            raise forms.ValidationError(
                "Daily calories cannot exceed 10,000."
            )

        return calories

    def clean_daily_protein(self):
        protein = self.cleaned_data.get("daily_protein")

        if protein is not None and protein > 1000:
            raise forms.ValidationError(
                "Daily protein cannot exceed 1,000 g."
            )

        return protein

    def clean_daily_carbohydrates(self):
        carbohydrates = self.cleaned_data.get(
            "daily_carbohydrates"
        )

        if carbohydrates is not None and carbohydrates > 1000:
            raise forms.ValidationError(
                "Daily carbohydrates cannot exceed 1,000 g."
            )

        return carbohydrates

    def clean_daily_fat(self):
        fat = self.cleaned_data.get("daily_fat")

        if fat is not None and fat > 1000:
            raise forms.ValidationError(
                "Daily fat cannot exceed 1,000 g."
            )

        return fat