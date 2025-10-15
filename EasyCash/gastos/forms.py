from django import forms
from .models import Categoria, Transaccion

# Formulario para el modelo Categoria
class CategoriaForm(forms.ModelForm):
    class Meta:
        # Asocia este formulario con el modelo Categoria
        model = Categoria
        # Incluye todos los campos del modelo en el formulario
        fields = '__all__'
        # Etiquetas personalizadas para los campos del formulario
        labels = {
            'nombre': 'Nombre de la Categoría',
            'tipo': 'Tipo (Ingreso/Gasto)',
        }
        # Widgets personalizados para mejorar la apariencia del formulario
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input rounded-md px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'tipo': forms.Select(attrs={'class': 'form-select rounded-md px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

# Formulario para el modelo Transaccion
class TransaccionForm(forms.ModelForm):
    class Meta:
        # Asocia este formulario con el modelo Transaccion
        model = Transaccion
        # Incluye los campos especificados del modelo en el formulario
        fields = ['monto', 'descripcion', 'tipo', 'categoria']
        # Etiquetas personalizadas para los campos del formulario
        labels = {
            'monto': 'Monto',
            'descripcion': 'Descripción (Opcional)',
            'tipo': 'Tipo (Ingreso/Gasto)',
            'categoria': 'Categoría',
        }
        # Widgets personalizados para mejorar la apariencia del formulario
        widgets = {
            'monto': forms.NumberInput(attrs={'class': 'form-input rounded-md px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500', 'step': '0.01'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-textarea rounded-md px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 3}),
            'tipo': forms.Select(attrs={'class': 'form-select rounded-md px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'categoria': forms.Select(attrs={'class': 'form-select rounded-md px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Permite que el campo categoria sea opcional en el formulario
        self.fields['categoria'].required = False
        # Establece el texto para la opción vacía del select de categoría
        self.fields['categoria'].empty_label = "--- Sin Categoría ---"