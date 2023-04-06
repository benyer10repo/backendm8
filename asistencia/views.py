from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import EmpresaSerializer
from .serializers import EmpleadoSerializer
from .serializers import AsistenciaSerializer
from .serializers import LocalSerializer
from .models import empresa
from .models import horario
from .models import empleado
from .models import local
from .models import asistencia
from rest_framework.decorators import api_view
from django.http import JsonResponse

def index(request):
    return HttpResponse("hola mundito")

def contact(request,name):
    return HttpResponse(f"Bienvenido {name} a la clase")



class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = empleado.objects.all()
    serializer_class = EmpleadoSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = asistencia.objects.all()
    serializer_class = AsistenciaSerializer

class LocalViewSet(viewsets.ModelViewSet):
    queryset = local.objects.all()
    serializer_class = LocalSerializer

#custumizar API
@api_view(["GET"])
def horarios_ver(request):
    try:
        horario_name = horario.objects.count()
        return JsonResponse(
            {
            "horario_name": horario_name
        },
        safe=False,
        status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)
