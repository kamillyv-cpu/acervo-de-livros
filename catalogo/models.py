from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Autores"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Gêneros"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    ano_publicacao = models.PositiveIntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='livros')
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name='livros')

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return self.titulo