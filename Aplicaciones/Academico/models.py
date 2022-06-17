from django.db import models
from django.utils.html import format_html
from .ChoicesSexo import sexo

# Create your models here.

class Docente(models.Model):
    apellido_paterno=models.CharField(verbose_name="Apellido Paterno", max_length=20)
    apellido_materno = models.CharField(verbose_name="Apellido Materno", max_length=20)
    nombre=models.CharField(verbose_name="Nombre",max_length=20)
    fecha_nacimiento=models.DateField(verbose_name="Fecha Nacimiento")
    sexo=models.CharField(verbose_name="Sexo",max_length=1,choices=sexo)

    class Meta:
        db_table="Docente"
        verbose_name="Docente"
        verbose_name_plural="Docentes"
        ordering=['apellido_paterno', '-apellido_materno']

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno}, {self.nombre}"

class Curso(models.Model):
        docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True, blank=True)
        nombre = models.CharField(max_length=30)
        creditos = models.PositiveSmallIntegerField(default=3)

        def __str__(self):
            return f"{self.nombre}  ({self.creditos})"

        class Meta:
            db_table = "Curso"

        def coloreado(self):
            return format_html('<span style="color: Blue;">{0}</span>'.format(self.nombre))

        def colorearCreditos(self):

            if (self.creditos > 3):

                return format_html('<span style="color: blue;"> {0} </span>'.format(self.creditos))
            else:
                return format_html('<span style="color: red;"> {0} </span>'.format(self.creditos))
