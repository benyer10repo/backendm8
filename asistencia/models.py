from django.db import models

from django.contrib.auth.models import User
from datetime import date
from smart_selects.db_fields import ChainedForeignKey
from .validators import validation_emple_telefo
from .validators import validation_emple_direccion

#modulo pais
class countries(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    country_name = models.CharField(max_length=100, verbose_name="Pais")

    def __str__(self):
        return self.country_name

class departamento(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    departamento_name = models.CharField(max_length=30, verbose_name="Departamento")
    countries_id = models.ForeignKey(countries, verbose_name="Pais",on_delete=models.CASCADE)

    def __str__(self):
            return self.departamento_name

class provincia(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    provincia_name = models.CharField(max_length=70, verbose_name="Provincia")
    departamento_id = models.ForeignKey(departamento, verbose_name="Departamento",on_delete=models.CASCADE)

    def __str__(self):
            return self.provincia_name

class distrito(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    distrito_name = models.CharField(max_length=70, verbose_name="Distrito")
    provincia_id = models.ForeignKey(provincia, verbose_name="Provincia",on_delete=models.CASCADE)

    def __str__(self):
            return self.distrito_name

class documento(models.Model):
    countries_id = models.ForeignKey(countries, verbose_name="Pais",on_delete=models.CASCADE)
    documento_name = models.CharField(max_length=30, verbose_name="Documento")

    def __str__(self):
            return self.documento_name

class empresa(models.Model):
    empresa_ruc = models.CharField(max_length=11, verbose_name="RUC")
    empresa_name = models.CharField(max_length=40, verbose_name="Razon Social")
    pais = models.ForeignKey(countries, verbose_name="Pais",on_delete=models.CASCADE)
    departamento = ChainedForeignKey(
        departamento, 
        chained_field="pais",
        chained_model_field="countries_id", 
        show_all=True
    )
    provincia = ChainedForeignKey(
        provincia, 
        chained_field="departamento",
        chained_model_field="departamento_id", 
        show_all=True
    )
    distrito = ChainedForeignKey(
        distrito, 
        chained_field="provincia",
        chained_model_field="provincia_id", 
        show_all=True
    )
    direccion_name = models.CharField(max_length=50, verbose_name="Direccion")

    def __str__(self):
            return self.empresa_name


class local(models.Model):
    local_name = models.CharField(max_length=30, verbose_name="Local")
    local_direccion = models.CharField(max_length=50, verbose_name="Direccion")
    pais = models.ForeignKey(countries, verbose_name="Pais",on_delete=models.CASCADE)
    departamento = ChainedForeignKey(
        departamento, 
        chained_field="pais",
        chained_model_field="countries_id", 
        show_all=True
    )
    provincia = ChainedForeignKey(
        provincia, 
        chained_field="departamento",
        chained_model_field="departamento_id", 
        show_all=True
    )
    distrito = ChainedForeignKey(
        distrito, 
        chained_field="provincia",
        chained_model_field="provincia_id", 
        show_all=True
    )
    empresa_id = models.ForeignKey(empresa, verbose_name="Empresa",on_delete=models.CASCADE)

    def __str__(self):
            return self.local_name

class area(models.Model):
    area_name = models.CharField(max_length=30, verbose_name="Area")
    empresa_id = models.ForeignKey(empresa, verbose_name="Empresa",on_delete=models.CASCADE)

    def __str__(self):
            return self.area_name

class horario(models.Model):
    horario_name = models.CharField(max_length=30, verbose_name="Horario")
    horario_entrada = models.TimeField(null=False, verbose_name="Hora de entrada")
    horario_salida = models.TimeField(null=False, verbose_name="Hora de salida")
    horario_tolerancia = models.SmallIntegerField(null=False, verbose_name="Tiempo de tolerancia")

    def __str__(self):
            return self.horario_name + ": " + self.horario_entrada.strftime("%H:%M:%S") + " - " + self.horario_salida.strftime("%H:%M:%S")

class empleado(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuario",on_delete=models.CASCADE)
    empleado_direccion = models.CharField(null=False,blank=False,max_length=30, verbose_name="Direccion",validators=[validation_emple_direccion])
    pais = models.ForeignKey(countries, verbose_name="Pais",on_delete=models.CASCADE)
    departamento = ChainedForeignKey(
        departamento, 
        chained_field="pais",
        chained_model_field="countries_id", 
        show_all=True
    )
    provincia = ChainedForeignKey(
        provincia, 
        chained_field="departamento",
        chained_model_field="departamento_id", 
        show_all=True
    )
    distrito = ChainedForeignKey(
        distrito, 
        chained_field="provincia",
        chained_model_field="provincia_id", 
        show_all=True
    )
    empleado_telefono = models.CharField(null=False,blank=False,max_length=12, verbose_name="Telefono",validators=[validation_emple_telefo])
    area_id = models.ForeignKey(area, verbose_name="Area",on_delete=models.CASCADE)
    documento_id = models.ForeignKey(documento, verbose_name="Tipo de documento",on_delete=models.CASCADE)
    empleado_nrodocumento = models.CharField(max_length=12,null=False, verbose_name="Numero de documento")
    local_id = models.ForeignKey(local, verbose_name="Local",on_delete=models.CASCADE)
    horario_id = models.ForeignKey(horario, verbose_name="Horario",on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_username()

class asistencia(models.Model):
    empleado_id = models.ForeignKey(empleado,on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)