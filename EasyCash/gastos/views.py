# gastos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Sum
from .models import Categoria, Transaccion
from .forms import CategoriaForm, TransaccionForm
from datetime import datetime
import calendar

# --- Vistas del Dashboard y Transacciones ---

def dashboard(request):
    """
    Muestra el dashboard principal con un resumen financiero.
    Incluye el balance actual, ingresos y gastos totales, y un desglose
    de gastos por categoría.
    """
    transacciones = Transaccion.objects.all().order_by('-fecha')

    ingresos_totales = Transaccion.objects.filter(tipo='Ingreso').aggregate(Sum('monto'))['monto__sum'] or 0
    gastos_totales = Transaccion.objects.filter(tipo='Gasto').aggregate(Sum('monto'))['monto__sum'] or 0
    
    balance_actual = ingresos_totales - gastos_totales

    gastos_por_categoria = Transaccion.objects.filter(tipo='Gasto') \
                                            .values('categoria__nombre') \
                                            .annotate(total=Sum('monto')) \
                                            .order_by('-total')
    
    ingresos_por_categoria = Transaccion.objects.filter(tipo='Ingreso') \
                                            .values('categoria__nombre') \
                                            .annotate(total=Sum('monto')) \
                                            .order_by('-total')

    context = {
        'transacciones': transacciones[:5],
        'ingresos_totales': ingresos_totales,
        'gastos_totales': gastos_totales,
        'balance_actual': balance_actual,
        'gastos_por_categoria': gastos_por_categoria,
        'ingresos_por_categoria': ingresos_por_categoria,
    }
    return render(request, 'gastos/dashboard.html', context)

def lista_transacciones(request):
    """
    Muestra una lista completa de todas las transacciones.
    Se ha eliminado la funcionalidad de filtrado.
    """
    # Obtener todas las transacciones ordenadas por fecha descendente
    transacciones = Transaccion.objects.all().order_by('-fecha')
    
    # Las variables de filtro ya no son necesarias en el contexto
    context = {
        'transacciones': transacciones,
        # 'categorias' y 'tipo_filtro', 'categoria_filtro' ya no se pasan
    }
    return render(request, 'gastos/lista_transacciones.html', context)

def agregar_transaccion(request):
    """
    Permite al usuario agregar una nueva transacción (ingreso o gasto).
    Maneja la presentación del formulario y el procesamiento de los datos enviados.
    """
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('gastos:lista_transacciones'))
    else:
        form = TransaccionForm()
    
    context = {
        'form': form,
        'titulo': 'Agregar Nueva Transacción',
        'es_edicion': False
    }
    return render(request, 'gastos/formulario_transaccion.html', context)

def editar_transaccion(request, pk):
    """
    Permite al usuario editar una transacción existente.
    'pk' es la clave primaria de la transacción a editar.
    """
    transaccion = get_object_or_404(Transaccion, pk=pk)
    
    if request.method == 'POST':
        form = TransaccionForm(request.POST, instance=transaccion)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('gastos:lista_transacciones'))
    else:
        form = TransaccionForm(instance=transaccion)
    
    context = {
        'form': form,
        'titulo': 'Editar Transacción',
        'es_edicion': True
    }
    return render(request, 'gastos/formulario_transaccion.html', context)

def eliminar_transaccion(request, pk):
    """
    Permite al usuario eliminar una transacción existente.
    'pk' es la clave primaria de la transacción a eliminar.
    Solo se permite la eliminación mediante petición POST.
    """
    transaccion = get_object_or_404(Transaccion, pk=pk)
    
    if request.method == 'POST':
        transaccion.delete()
        return redirect(reverse_lazy('gastos:lista_transacciones'))
    
    return redirect(reverse_lazy('gastos:lista_transacciones'))

# --- Vistas de Categorías ---

def lista_categorias(request):
    """
    Muestra una lista de todas las categorías disponibles.
    """
    categorias = Categoria.objects.all().order_by('nombre')
    context = {
        'categorias': categorias
    }
    return render(request, 'gastos/lista_categorias.html', context)

def crear_categoria(request):
    """
    Permite al usuario crear una nueva categoría.
    """
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('gastos:lista_categorias'))
    else:
        form = CategoriaForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Nueva Categoría',
        'es_edicion': False
    }
    return render(request, 'gastos/formulario_categoria.html', context)

def editar_categoria(request, pk):
    """
    Permite al usuario editar una categoría existente.
    """
    categoria = get_object_or_404(Categoria, pk=pk)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('gastos:lista_categorias'))
    else:
        form = CategoriaForm(instance=categoria)
    
    context = {
        'form': form,
        'titulo': 'Editar Categoría',
        'es_edicion': True
    }
    return render(request, 'gastos/formulario_categoria.html', context)

def eliminar_categoria(request, pk):
    """
    Permite al usuario eliminar una categoría existente.
    """
    categoria = get_object_or_404(Categoria, pk=pk)
    
    if request.method == 'POST':
        categoria.delete()
        return redirect(reverse_lazy('gastos:lista_categorias'))
    
    return redirect(reverse_lazy('gastos:lista_categorias'))

# --- Vistas de Reportes ---

def reporte_mensual(request):
    """
    Genera un reporte de ingresos y gastos agrupados por mes.
    """
    transacciones = Transaccion.objects.all()

    reporte_data = {}

    for transaccion in transacciones:
        mes_anio_key = transaccion.fecha.strftime('%Y-%m')
        mes_nombre = calendar.month_name[transaccion.fecha.month]
        
        if mes_anio_key not in reporte_data:
            reporte_data[mes_anio_key] = {
                'mes_nombre': f"{mes_nombre} {transaccion.fecha.year}",
                'ingresos': 0,
                'gastos': 0,
                'balance': 0
            }
        
        if transaccion.tipo == 'Ingreso':
            reporte_data[mes_anio_key]['ingresos'] += transaccion.monto
        else:
            reporte_data[mes_anio_key]['gastos'] += transaccion.monto
        
        reporte_data[mes_anio_key]['balance'] = reporte_data[mes_anio_key]['ingresos'] - reporte_data[mes_anio_key]['gastos']
    
    reporte_lista = sorted(reporte_data.items())

    context = {
        'reporte_mensual': [item[1] for item in reporte_lista]
    }
    return render(request, 'gastos/reporte_mensual.html', context)

def reporte_por_categoria(request):
    """
    Genera un reporte de ingresos y gastos agrupados por categoría.
    """
    gastos_por_categoria = Transaccion.objects.filter(tipo='Gasto') \
                                            .values('categoria__nombre') \
                                            .annotate(total=Sum('monto')) \
                                            .order_by('categoria__nombre')
    
    ingresos_por_categoria = Transaccion.objects.filter(tipo='Ingreso') \
                                            .values('categoria__nombre') \
                                            .annotate(total=Sum('monto')) \
                                            .order_by('categoria__nombre')

    context = {
        'gastos_por_categoria': gastos_por_categoria,
        'ingresos_por_categoria': ingresos_por_categoria,
    }
    return render(request, 'gastos/reporte_por_categoria.html', context)