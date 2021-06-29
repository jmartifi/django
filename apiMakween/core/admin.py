from django.contrib import admin
from .models import Categoria, Vehiculo, TipoUsuario, Usuario, Estado, Atencion

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Estado)
admin.site.register(Atencion)