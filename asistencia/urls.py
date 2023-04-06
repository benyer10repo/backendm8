from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"empresa", views.EmpresaViewSet)
router.register(r"empleado", views.EmpleadoViewSet)
router.register(r"asistencia", views.AsistenciaViewSet)
router.register(r"local", views.LocalViewSet)

urlpatterns =[
    path("contact/<str:name>",views.contact, name="contact"),
    #path("", views.index,name="index")
    path("asistencia/horario",views.horarios_ver, name="horario"),
    path("", include(router.urls))
]
