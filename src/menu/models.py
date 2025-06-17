from django.db import models
from django.urls import reverse


def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ë': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'x': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ъ': '', 'ы': 'i', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))


class Category(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField(default=0)
    url = models.TextField(unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    def save(self, *args, **kwargs):
        translated_name = translit_to_eng(self.name)

        if (parent := self.parent) is not None:
            self.url = f"{parent.url}/{translated_name}"
            self.level = parent.level + 1
        else:
            self.url = translated_name

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('path', kwargs={'path': self.url})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
