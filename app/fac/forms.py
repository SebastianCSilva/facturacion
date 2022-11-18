from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombres', 'apellidos', 'tipo', 'celular', 'estado']
        exclude = ['usuario_modifica', 'fecha_modificacion', 'usuario_crea', 'fecha_creacion']

    """
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modifica = models.IntegerField(blank=True, null=True)

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
