from django.urls import path
from rest.views import lista_vehiculos, detalle_vehiculo, lista_atencion, detalle_atencion, lista_Usuario, detalle_usuario, lista_servicios, detalle_servios
from .viewslogin import login

urlpatterns = [
    path('vehiculos',lista_vehiculos, name='lista_vehiculos'),
    path('atenciones',lista_atencion, name='lista_atencion'),
    path('usuarios',lista_Usuario, name='lista_Usuario'),
    path('servicios',lista_servicios, name='lista_servicios'),
    path('vehiculos/<id>',detalle_vehiculo, name='detalle_vehiculo'),
    path('atenciones/<id>',detalle_atencion, name='detalle_atencion'),
    path('usuarios/<id>',detalle_usuario, name='detalle_usuario'),
    path('servicios/<id>',detalle_servios, name='detalle_servios'),
    path('login',login, name='login'),
]