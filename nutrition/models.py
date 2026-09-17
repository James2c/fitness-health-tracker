from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class NutritionEntry(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="nutrition_entries",
    )

    date = models.DateField()

    food_name = models.CharField(max_length=150)

    serving_size = models.CharField(
        max_length=100,
        blank=True,
    )

    calories = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(10000),
        ]
    )

    protein = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000),
        ],
    )

    carbohydrates = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000),
        ],
    )

    fat = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000),
        ],
        )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-created_at"]


    def __str__(self):
        return f"{self.user.username} - {self.food_name} - {self.date}"


class NutritionGoal(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="nutrition_goal",
    )

    daily_calories = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(10000),
        ]
    )

    daily_protein = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000),
        ],
    )

    daily_carbohydrates = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000),
        ],
    )

    daily_fat = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000),
        ],
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username} - Nutrition Goals"