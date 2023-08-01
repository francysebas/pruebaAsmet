from django.contrib import admin
from .models import Persona, Juzgado, Caso, TipoPersona, TipoDocumento
# Register your models here.

admin.site.register(Persona)
admin.site.register(Juzgado)
admin.site.register(Caso)
admin.site.register(TipoPersona)
admin.site.register(TipoDocumento)