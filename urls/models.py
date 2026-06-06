from django.db import models

# Create your models here.
class URL(models.Model):
    url_original = models.URLField(max_length=2000)
    codigo_curto = models.CharField(max_length=6, unique=True)
    data_de_criacao = models.DateTimeField(auto_now_add=True)