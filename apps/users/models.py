from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class RegionChoices(models.TextChoices):
        Chuy = "Chuy", "Чуй"
        Osh = "Osh", "Ош"
        Jalal_Abad = "Jalal_Abad", "Джалал-Абад"
        Naryn = "Naryn", "Нарын"
        Issyk_Kyl = "Issyk_kyl", "Иссык_кул"
        Batken = "Batken", "Баткен"
        Talas = "Talas", "Талас"

    groups = None
    first_name = None
    last_name = None
    user_permissions = None

    display_name = models.CharField(
        max_length=50,
        verbose_name="Никнейм",
    )
    avatar = models.ImageField(
        upload_to="users/",
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name="Номер телефона",
        validators=[
            # MaxValueValidator(13),
            # MinValueValidator(13),
        MaxLengthValidator(13),
        MinLengthValidator(13),
        ]
    )

    region = models.CharField(
        max_length=10,
        choices=RegionChoices.choices,
        verbose_name="Регионы",
    )

    def __str__(self):
        return self.username
