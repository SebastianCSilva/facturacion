from django.shortcuts import render, redirect
from django.views import generic
from .models import Proveedor
from django.urls import reverse_lazy

from django.http import HttpResponse
import json

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .forms import ProveedorForm



# Create your views here.
class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    
    form_class = ProveedorForm
    success_url = reverse_lazy("cmo:proveedor_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)


def proveedor_inactivar(request, id):
    proveedor = Proveedor.objects.filter(pk=id).first()
    contexto = {}
    template_name = "cmp/inactivar_prv.html"

    if not proveedor:
        return HttpResponse('Proveedor no existe '+ str(id))
    if request.method == 'GET':
        contexto = {'obj':proveedor}
    
    if request.method == 'POST':
        proveedor.estado = False
        proveedor.save()
        contexto = {'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')


    return render(request, template_name, contexto)

