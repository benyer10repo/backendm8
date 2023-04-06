from django.test import TestCase
from .models import empleado
from django.core.exceptions import ValidationError

class TestEmpleado(TestCase):
    def test_grabacion(self):
        q = empleado.objects.create(empleado_telefono="No permitido")
        self.assertRaises(ValidationError, q.full_clean)


class TestEmpleado(TestCase):
    def test_grabacion(self):
        q = empleado.objects.create(empleado_direccion="No permitido")
        self.assertRaises(ValidationError, q.full_clean)