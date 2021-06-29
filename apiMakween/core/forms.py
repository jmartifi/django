from django import forms
from django.forms import ModelForm
from .models import Vehiculo, Usuario, Servicios, Atencion, Contacto

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'ano', 'categoria']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['tbus_cdg_id', 'tbus_dsc_nombre', 'tbus_dsc_apellido', 'tbus_dsc_email', 'tbus_dsc_pass', 'tipoUsuario']
        
class ServicioForm(ModelForm):
    class Meta:
        model = Servicios
        fields = ['tbse_cdg_id', 'tbse_dsc_nombre']

class AtencionForm(ModelForm):
    class Meta:
        model = Atencion
        fields = ['tbat_cdg_id', 'tbat_dsc_titulo', 'tbat_fch_ingreso', 'tbat_dsc_resena', 'tbat_dsc_diagnostico', 'tbat_img_imagena', 'tbat_img_imagenb', 'tbat_img_imagenc', 'patente', 'servicio', 'sts', 'mecanico']
        
class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['tbco_dsc_nombre', 'tbco_dsc_apellido', 'tbco_nmr_fono', 'tbco_dsc_email', 'tbco_dsc_consulta']