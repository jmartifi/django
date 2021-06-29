from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vehiculo, Usuario, Servicios, Atencion, Contacto
from .forms import VehiculoForm, UsuarioForm, ServicioForm, AtencionForm, ContactoForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def inicio(request):
    return render(request, 'core/inicio.html')

def listarUsuarios(request):
    usuarios = Usuario.objects.all()
    
    datos = {
        'usuarios' : usuarios
    }
    return render(request, 'core/listarUsuarios.html', datos)

def agregarUsuario(request):
    datos = {
        'form' : UsuarioForm()
    }
    
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        email  = request.POST['tbus_dsc_email']
        
        usuario = Usuario.objects.filter(tbus_dsc_email=email).exists()
        if usuario == True:
            datos['mensaje'] = 'Usuario existente'
        else:
            if formulario.is_valid:
                formulario.save()
                messages.success(request, 'Usuario agregado correctamente')
                return redirect(to='listarUsuarios')

    return render (request, 'core/form_agregarUsuario.html', datos)

def editarUsuario(request, id):
    usuario = Usuario.objects.get(tbus_cdg_id=id)
    
    datos = {
        'form' : UsuarioForm(instance=usuario)
    }
    
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario)
        formulario.save()
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Usuario editado correctamente')
            return redirect(to='listarUsuarios')
            
    return render(request, 'core/form_editarUsuario.html', datos)

def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(tbus_cdg_id=id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado correctamente')
    return redirect(to='listarUsuarios')

def listarVehiculos(request):
    vehiculos = Vehiculo.objects.all()
    
    datos = {
        'vehiculos' : vehiculos
    }
    return render(request, 'core/listarVehiculos.html', datos)

def agregarVehiculo(request):
    datos = {
        'form' : VehiculoForm()
    }
    
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        patente  = request.POST['patente']
        
        vehiculo = Vehiculo.objects.filter(patente=patente).exists()
        if vehiculo == True:
            datos['mensaje'] = 'Vehiculo existente'
        else:
            if formulario.is_valid:
                formulario.save()
                messages.success(request, 'Vehiculo agregado correctamente')
                return redirect(to='listarVehiculos')
    
    return render (request, 'core/form_agregarVehiculo.html', datos)

def editarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente = id)
    
    datos = {
        'form' : VehiculoForm(instance=vehiculo)
    }
    
    if request.method == 'POST':
        formulario = VehiculoForm(data=request.POST, instance=vehiculo)
        formulario.save()
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Vehiculo editado correctamente')
            return redirect(to='listarVehiculos')
            
    return render(request, 'core/form_editarVehiculo.html', datos)

def eliminarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    messages.success(request, 'Vehiculo eliminado correctamente')
    return redirect(to='listarVehiculos')

def listarServicios(request):
    servicios = Servicios.objects.all()
    
    datos = {
        'servicios' : servicios
    }
    return render(request, 'core/listarServicios.html', datos)

def agregarServicio(request):
    datos = {
        'form' : ServicioForm()
    }
    
    if request.method == 'POST':
        formulario = ServicioForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Servicio agregado correctamente')
            return redirect(to='listarServicios')
    
    return render (request, 'core/form_agregarServicio.html', datos)

def editarServicio(request, id):
    servicio = Servicios.objects.get(tbse_cdg_id=id)
    
    datos = {
        'form' : ServicioForm(instance=servicio)
    }
    
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST, instance=servicio)
        formulario.save()
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Servicio editado correctamente')
            return redirect(to='listarServicios')
            
    return render(request, 'core/form_editarServicio.html', datos)

def eliminarServicio(request, id):
    servicio = Servicios.objects.get(tbse_cdg_id=id)
    servicio.delete()
    messages.success(request, 'Servicio eliminado correctamente')
    return redirect(to='listarServicios')

def listarAtenciones(request):
    atenciones = Atencion.objects.all()
    
    datos = {
        'atenciones' : atenciones
    }
    return render(request, 'core/listarAtenciones.html', datos)

def agregarAtencion(request):
    data = {
        'form' : AtencionForm()
    }
    
    if request.method == 'POST':
        formulario = AtencionForm(data=request.POST, files=request.FILES)
        
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Atención agregada correctamente')
            return redirect(to='listarAtenciones')
    
    return render (request, 'core/form_agregarAtencion.html', data)

def editarServicio(request, id):
    atencion = Atencion.objects.get(tbat_cdg_id=id)
    
    datos = {
        'form' : AtencionForm(instance=atencion)
    }
    
    if request.method == 'POST':
        formulario = AtencionForm(data=request.POST, files=request.FILES, instance=atencion)
        formulario.save()
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Atención editada correctamente')
            return redirect(to='listarAtenciones')
            
    return render(request, 'core/form_editarAtencion.html', datos)

def eliminarAtencion(request, id):
    atencion = Atencion.objects.get(tbat_cdg_id=id)
    atencion.delete()
    messages.success(request, 'Atención eliminado correctamente')
    return redirect(to='listarAtenciones')

def agregarContacto(request):
    datos = {
        'form' : ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Contacto ingresado correctamente')
    
    return render (request, 'core/contacto.html', datos)

def listarContacto(request):
    contactos = Contacto.objects.all()
    
    datos = {
        'contacto' : contactos
    }
    return render(request, 'core/listarContacto.html', datos)

def detalleAtencion(request):
    detalle = Atencion.objects.filter(tbat_cdg_id=23)
    
    datos = {
        'detalle' : detalle
    }
    return render(request, 'core/detalleTrabajo.html', datos)