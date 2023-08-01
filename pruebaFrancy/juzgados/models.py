from django.db import models


# Create your models here.

class TipoDocumento(models.Model):
    nombre = models.CharField('tipo identificacion', max_length=10)

    class Meta:
        verbose_name = 'tipo identificacion'
        verbose_name_plural = 'tipos identificacion'

    def __str__(self):
        return self.nombre


class TipoPersona(models.Model):
    nombre = models.CharField('tipo persona', max_length=60)

    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    identificacion = models.CharField('Numero de identificación', max_length=10)
    tipoIdentificacion = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    nombres = models.CharField('Nombres completos', max_length=80)
    apelllidos = models.CharField('Apellidos completos', max_length=80)
    fechaNaciemiensto = models.DateField('Fecha naciemiento')
    ciudadResidencia = models.CharField('Ciudad residencia', max_length=80)
    direccion = models.CharField('Dirección', max_length=50)
    telefono = models.CharField('Teléfono', max_length=10)
    celular = models.CharField('Celular', max_length=10)
    tipoPersona = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.identificacion


class Juzgado(models.Model):
    nombre = models.CharField('Nombre del juzgado', max_length=80)
    direccion = models.CharField('Dirección', max_length=80)
    telefono = models.CharField('Teléfono', max_length=12)

    class Meta:
        verbose_name = 'juzgado'
        verbose_name_plural = 'juzgados'

    def __str__(self):
        return self.nombre


class Caso(models.Model):
    NumeroCaso = models.CharField('numero del caso', max_length=12)
    IdPersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    IdJuzgado = models.ForeignKey(Juzgado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Caso'
        verbose_name_plural = 'Casos'

    def __str__(self):
        return self.NumeroCaso