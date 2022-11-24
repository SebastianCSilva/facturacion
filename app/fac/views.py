from django.shortcuts import render
from .models import Cliente, FacturaEnc, FacturaDet

from bases.views import SinPrivilegios
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse


from .forms import ClienteForm
# Create your views here.


class ClienteView(LoginRequiredMixin, generic.ListView):
    model = Cliente
    template_name = "fac/clientes_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'
    permission_required = "fac.view_cliente"


class VistaBaseCreate(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    context_object_name = "obj"
    success_message = "Registro Agregado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class VistaBaseEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    context_object_name = "obj"
    success_message = "Registro Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class ClienteNew(VistaBaseCreate):
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    permission_required = "fac.add_cliente"

class ClienteEdit(VistaBaseEdit):
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    permission_required = "fac.change_cliente"

@login_required(login_url="/login/")
@permission_required("fac.change_cliente", login_url="/login/")
def clienteInactivar(request, id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method == "POST":
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse("OK")
        return HttpResponse("Fail")

    return HttpResponse("Fail")


class FacturaView(SinPrivilegios, generic.ListView):
    model = FacturaEnc
    template_name = "fac/factura_list.html"
    context_object_name = "obj"
    permission_required = "fac.view_facturaenc"


