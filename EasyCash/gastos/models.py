from django.db import models

# Create your models here.

# Modelo para las categorías de ingresos y gastos
class Categoria(models.Model):
    # Nombre de la categoría (ej. "Alimentos", "Transporte", "Salario")
    nombre = models.CharField(max_length=100, unique=True)
    
    # Tipo de categoría: 'Ingreso' o 'Gasto'
    TIPO_CHOICES = [
        ('Ingreso', 'Ingreso'),
        ('Gasto', 'Gasto'),
    ]
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)

    class Meta:
        # Ordenar las categorías alfabéticamente por nombre
        ordering = ['nombre']
        # Nombre plural legible para el administrador de Django
        verbose_name_plural = "Categorías"

    def __str__(self):
        # Representación de cadena del objeto Categoria
        return f"{self.nombre} ({self.tipo})"

# Modelo para registrar cada transacción (ingreso o gasto)
class Transaccion(models.Model):
    # Monto de la transacción
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Fecha en que ocurrió la transacción. Se establece automáticamente al crear.
    fecha = models.DateField(auto_now_add=True)
    
    # Descripción opcional de la transacción
    descripcion = models.TextField(blank=True, null=True)
    
    # Tipo de transacción: 'Ingreso' o 'Gasto'
    TIPO_CHOICES = [
        ('Ingreso', 'Ingreso'),
        ('Gasto', 'Gasto'),
    ]
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    
    # Categoría a la que pertenece la transacción. Puede ser nula.
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL, # Si la categoría se elimina, este campo se pone a NULL
        null=True,
        blank=True,
        related_name='transacciones' # Nombre inverso para acceder desde Categoria
    )

    class Meta:
        # Ordenar las transacciones por fecha de forma descendente (más recientes primero)
        ordering = ['-fecha']
        # Nombre plural legible para el administrador de Django
        verbose_name_plural = "Transacciones"

    def __str__(self):
        # Representación de cadena del objeto Transaccion
        return f"{self.tipo}: {self.monto} el {self.fecha} ({self.categoria or 'Sin Categoría'})"