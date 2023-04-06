from django.core.exceptions import ValidationError

def validation_emple_telefo(value):
    if value == "No permitido":
        raise ValidationError("no es una opción viable")


def validation_emple_direccion(value):
    if value == "No permitido":
        raise ValidationError("no es una opción viable")