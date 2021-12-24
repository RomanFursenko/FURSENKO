from django.db import models

class Md(models.Model):
    engword = models.CharField(max_length=20, verbose_name='Слово на английском')
    rusword = models.CharField(max_length=20, verbose_name='Слово на русском')
    content = models.TextField(null=True, blank=True, db_index=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Словарь'
        verbose_name = 'Словарь'
        ordering = ['-published']

class Post(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.title