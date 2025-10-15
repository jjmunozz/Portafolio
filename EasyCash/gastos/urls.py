from django.urls import path
from . import views 

app_name = 'gastos' # Espacio de nombres para tus URLs

urlpatterns = [
    path('', views.dashboard, name='dashboard'), # Dashboard dentro de 'gastos/'
    path('transacciones/', views.lista_transacciones, name='lista_transacciones'),
    path('transacciones/agregar/', views.agregar_transaccion, name='agregar_transaccion'),
    path('transacciones/editar/<int:pk>/', views.editar_transaccion, name='editar_transaccion'),
    path('transacciones/eliminar/<int:pk>/', views.eliminar_transaccion, name='eliminar_transaccion'),

    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),

    path('reportes/mensual/', views.reporte_mensual, name='reporte_mensual'),
    path('reportes/categoria/', views.reporte_por_categoria, name='reporte_por_categoria'),
]