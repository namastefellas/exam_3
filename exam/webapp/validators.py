from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class ScoreValidator(BaseValidator):
    message = 'Введите корректную оценку (от 1 до 5)'
    code = 'invalid_score_range'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)