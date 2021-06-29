from django.urls import path
from .views import index, inicio, listarVehiculos, agregarVehiculo, editarVehiculo, eliminarVehiculo, listarUsuarios, agregarUsuario, editarUsuario, eliminarUsuario, listarServicios, agregarServicio, editarServicio, eliminarServicio, listarAtenciones, agregarAtencion, editarServicio, eliminarAtencion, agregarContacto, listarContacto, detalleAtencion

urlpatterns = [
    path('',index, name='index'),
    path('inicio',inicio, name='inicio'),
    path('contacto',agregarContacto, name='agregarContacto'),
    path('detalle',detalleAtencion, name='detalleAtencion'),
    path('usuarios/listar',listarUsuarios, name='listarUsuarios'),
    path('usuarios/agregar',agregarUsuario, name='agregarUsuario'),
    path('usuarios/editar/<id>',editarUsuario, name='editarUsuario'),
    path('usuarios/eliminar/<id>',eliminarUsuario, name='eliminarUsuario'),
    path('vehiculo/listar',listarVehiculos, name='listarVehiculos'),
    path('vehiculo/agregar',agregarVehiculo, name='agregarVehiculos'),
    path('vehiculo/editar/<id>',editarVehiculo, name='editarVehiculo'),
    path('vehiculo/eliminar/<id>',eliminarVehiculo, name='eliminarVehiculo'),
    path('servicios/listar',listarServicios, name='listarServicios'),
    path('servicios/agregar',agregarServicio, name='agregarServicio'),
    path('servicios/editar/<id>',editarServicio, name='editarServicio'),
    path('servicios/eliminar/<id>',eliminarServicio, name='eliminarServicio'),
    path('atenciones/listar',listarAtenciones, name='listarAtenciones'),
    path('atenciones/agregar',agregarAtencion, name='agregarAtencion'),
    path('atenciones/editar/<id>',editarServicio, name='editarServicio'),
    path('atenciones/eliminar/<id>',eliminarAtencion, name='eliminarAtencion'),
    path('contactos/listar',listarContacto, name='listarContacto'),
]