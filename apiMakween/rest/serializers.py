from rest_framework import serializers
from core.models import Vehiculo, Atencion, Usuario, Servicios

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'ano', 'categoria']
        
class AtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atencion
        fields = ['tbat_dsc_titulo', 'tbat_fch_ingreso', 'tbat_dsc_resena', 'tbat_dsc_diagnostico', 'tbat_img_imagena', 'tbat_img_imagenb', 'tbat_img_imagenc', 'patente', 'servicio', 'sts', 'mecanico']
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['tbus_dsc_nombre', 'tbus_dsc_apellido', 'tbus_dsc_email', 'tbus_dsc_pass', 'tipoUsuario']
        
class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ['tbse_dsc_nombre']