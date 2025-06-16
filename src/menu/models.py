from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='childrens',
        null=True,
        blank=True,
    )
