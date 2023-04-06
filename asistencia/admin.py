# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from .models import empresa
from .models import local
from .models import area
from .models import horario
from .models import empleado

admin.site.register(empresa)
admin.site.register(local)
admin.site.register(area)
admin.site.register(horario)
admin.site.register(empleado)
