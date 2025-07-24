from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Нова'),
        ('in_progress', 'В процесі'),
        ('done', 'Завершена'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    is_important = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.due_date > timezone.now().date():
            raise ValidationError("Дата не може бути в майбутньому!")
        if len(self.description) > 500:
            raise ValidationError("Опис не може бути довшим за 500 символів.")
