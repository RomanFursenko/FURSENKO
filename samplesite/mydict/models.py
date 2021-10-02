from django.db import models

class Md(models.Model):
    engword = models.CharField(max_length=20)
    rusword = models.CharField(max_length=20)
    content = models.TextField(null=True, blank=True, db_index=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Словарь'
        verbose_name = 'Словарь'
        ordering = ['-published']
