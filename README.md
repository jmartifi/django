DemoDjango
Proyecto Demo Django Framework de apoyo a la Experiencia N°3 de la Asignatura Programación Web

Parte 1: Configuración del entorno
Verificar que Python 3 esté instalado en el equipo
c:\> python --version
Si python no está instalado, instalar según instrucciones de clase Descargar instalador desde sitio oficial de Python

Verificar que PIP esté instalado en el equipo
c:\> py -m pip --version
Si PIP está desactualizado, actualizar.

c:\> py -m pip install --upgrade pip
Instalar Django
c:\> pip install django
Puedes verificar la instalación con:

c:\> py -m django --version
Parte 2: Crear proyecto Django
Debes crear un directorio donde almacenarás el proyecto. Si trabajarás enlazado a un repo, éste es un buen momento para clonarlo. En esta demo, se asumirá que los proyectos se almacenarán en C:/ProyectosDjango

Para crear el directorio y acceder a él desde el cmd

c:\>Users\yo> cd\
c:\>md ProyectosDjango
c:\>cd ProyectosDjango 

c:\ProyectosDjango>
Para acceder al directorio desde el cmd

c:\>cd c:\ProyectosDjango
c:\ProyectosDjango>
Creando proyecto django
c:\ProyectosDjango>django-admin startproject nombre_proyecto
Parte 3: Enlazar proyecto django a Visual Studio Code
Abrir directorio del proyecto django creado en el paso anterior con Visual Studio Code. Ésta será la raiz de nuestro proyecto.

Parte 4: Crear Aplicación
Éste será nuestro sitio web. Desde el terminal de VSCODE, escribir:

c:\ProyectosDjango\Proyecto>py manage.py startapp nombre_aplicacion
Parte 5: Agregar aplicación al proyecto
En el archivo settings.py agregar el nombre de la aplicación a INSTALLED_APPS

    INSTALLED_APPS = [
    #LIBRERIAS DJANGO
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #MI APP
    'nombre_app',
]
Parte 6: Iniciar servidor
En la terminal de VS CODE iniciar el servidor de pruebas. No olvidar que el servidor debe mantenerse corriendo durante todo el uso de la aplicación.

c:\ProyectosDjango\Proyecto>py manage.py runserver
Puedes ver los resultados en http://127.0.0.1:8000/
