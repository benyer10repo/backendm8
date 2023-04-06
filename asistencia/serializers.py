from rest_framework import serializers
from .models import empresa
from .models import empleado
from .models import asistencia
from .models import  local


#para modelo empresa
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = empresa
        fields = "__all__"

#para modelo empleado
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleado
        fields = "__all__"

#para modelo asistencia
class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = asistencia
        fields = "__all__"

#para modelo local
class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = local
        fields = "__all__"