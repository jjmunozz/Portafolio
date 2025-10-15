"""
URL configuration for control_gastos_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
    # control_gastos_app/urls.py

from django.contrib import admin
from django.urls import path, include # Asegúrate de que 'include' esté aquí

urlpatterns = [
    path('admin/', admin.site.urls), # Deja esta línea, es para el panel de administración
    
    # Esta línea es CLAVE: le dice a Django que todas las URLs que empiecen con 'gastos/'
    # las maneje el archivo 'gastos/urls.py'
    path('gastos/', include('gastos.urls')),
      
    # Esta línea es OPCIONAL: si quieres que el dashboard de gastos sea la página de inicio
    # de tu sitio (ej. http://127.0.0.1:8000/)
    path('', include('gastos.urls')), 
]