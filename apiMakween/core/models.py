from django.db import models

# Create your models here.

class TipoUsuario(models.Model):
    tbtu_cdg_id = models.AutoField(primary_key=True, verbose_name='Id tipo usuario')
    tbtu_dsc_nombre = models.CharField(max_length=255, verbose_name='Nombre tipo usuario')
    
    def __str__(self):
        return self.tbtu_dsc_nombre

class Usuario(models.Model):
    tbus_cdg_id = models.AutoField(primary_key=True, verbose_name='Id Usuario')
    tbus_dsc_nombre = models.CharField(max_length=255, verbose_name='Nombre')
    tbus_dsc_apellido = models.CharField(max_length=255, verbose_name='apellido')
    tbus_dsc_email = models.CharField(max_length=255, verbose_name='E-mail')
    tbus_dsc_pass = models.CharField(max_length=255, verbose_name='Contraseña')
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tbus_dsc_email
    
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id cateroría')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Categoría')
    
    def __str__(self):
        return self.nombreCategoria
    
class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='marca')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='modelo')
    ano = models.IntegerField(verbose_name='Año')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.patente

class Servicios(models.Model):
    tbse_cdg_id = models.AutoField(primary_key=True, verbose_name='Id servicio')
    tbse_dsc_nombre = models.CharField(max_length=255, verbose_name='Nombre servicio')
    
    def __str__(self):
        return self.tbse_dsc_nombre

class Estado(models.Model):
    tbes_cdg_id = models.AutoField(primary_key=True, verbose_name='Id estado')
    tbes_sts_code = models.CharField(max_length=3, verbose_name='Código estado')
    tbes_sts_nombre = models.CharField(max_length=255, verbose_name='Nombre estado')
    
    def __str__(self):
        return self.tbes_sts_nombre

class Atencion(models.Model):
    tbat_cdg_id = models.AutoField(primary_key=True, verbose_name='Id atención')
    tbat_dsc_titulo = models.CharField(max_length=255, verbose_name='titulo')
    tbat_fch_ingreso = models.DateField(max_length=255, verbose_name='Fecha ingreso')
    tbat_dsc_resena = models.TextField(max_length=255, verbose_name='Reseña')
    tbat_dsc_diagnostico = models.TextField(max_length=255, verbose_name='Diagnostico')
    tbat_img_imagena = models.TextField(max_length=255, verbose_name='Imagen 1')
    #tbat_img_imagena = models.ImageField(upload_to="galeria", verbose_name='Imagen 1')
    tbat_img_imagenb = models.TextField(max_length=255, null=True, verbose_name='Imagen 2')
    #tbat_img_imagenb = models.ImageField(upload_to="galeria", null=True, verbose_name='Imagen 2')
    #tbat_img_imagenc = models.ImageField(upload_to="galeria", null=True, verbose_name='Imagen 3')
    tbat_img_imagenc = models.TextField(max_length=255, null=True, verbose_name='Imagen 3')
    patente = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    sts = models.ForeignKey(Estado, on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tbat_dsc_titulo

class Contacto(models.Model):
    tbco_cdg_id = models.AutoField(primary_key=True, verbose_name='Id contacto')
    tbco_dsc_nombre =  models.CharField(max_length=255, verbose_name='Nombre')
    tbco_dsc_apellido =  models.CharField(max_length=255, verbose_name='Apellido')
    tbco_nmr_fono =  models.IntegerField(verbose_name='Teléfono')
    tbco_dsc_email =  models.CharField(max_length=255, verbose_name='Dirección de correo electrónico')
    tbco_dsc_consulta =  models.CharField(max_length=300, verbose_name='¿Cómo podemos ayudarte?')
    
    def nombre_completo(self):
        return '{}, {}'.format(self.tbco_dsc_nombre , self.tbco_dsc_apellido)
    
    def __str__(self):
        return self.nombre_completo