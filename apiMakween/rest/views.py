from django.views.decorators.csrf import csrf_exempt
from rest.serializers import VehiculoSerializer, AtencionSerializer, UsuarioSerializer, ServiciosSerializer
from django.shortcuts import render
from core.models import Vehiculo, Atencion, Usuario, Servicios
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_vehiculos(request):
    if request.method == 'GET':
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_vehiculo(request, id):
    try:
        vehiculo = Vehiculo.objects.get(patente=id)
    except Vehiculo.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(vehiculo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_atencion(request):
    if request.method == 'GET':
        atencion = Atencion.objects.all()
        serializer = AtencionSerializer(atencion,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AtencionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes((IsAuthenticated,))
def detalle_atencion(request, id):
    try:
        atencion = Atencion.objects.get(tbat_cdg_id=id)
    except Atencion.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AtencionSerializer(atencion)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AtencionSerializer(atencion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        atencion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_Usuario(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes((IsAuthenticated,))
def detalle_usuario(request, id):
    try:
        usuario = Usuario.objects.get(tbus_cdg_id=id)
    except Usuario.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_servicios(request):
    if request.method == 'GET':
        servicios = Servicios.objects.all()
        serializer = ServiciosSerializer(servicios,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ServiciosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes((IsAuthenticated,))
def detalle_servios(request, id):
    try:
        servicio = Servicios.objects.get(tbse_cdg_id=id)
    except Servicios.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ServiciosSerializer(servicio)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ServiciosSerializer(servicio, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        servicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)