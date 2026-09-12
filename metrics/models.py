from django.db import models
from django.contrib.auth.models import User



class WeightEntry(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="weight_entries",
    )

    date = models.DateField()

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    notes = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.weight} kg on {self.date}"