from datetime import datetime

from django.core.exceptions import ValidationError


def correct_year(value):
    if not value <= datetime.today().year:
        raise ValidationError("Нельзя предсказывать будущие произведения")
