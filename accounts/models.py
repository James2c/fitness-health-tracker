from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    UNIT_CHOICES = [
        ("metric", "Metric"),
        ("imperial", "Imperial"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    unit_system = models.CharField(
        max_length=10,
        choices=UNIT_CHOICES,
        default="metric"
    )

    def __str__(self):
        return self.user.username

