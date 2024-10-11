from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_de_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_de_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
