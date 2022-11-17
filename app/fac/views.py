from django.shortcuts import render
from models import Cliente

from bases.views import SinPrivilegios
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


class ClienteView(LoginRequiredMixin, generic.ListView):
    model = Cliente
    template_name = "fac/clientes_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'
    permission_required = "fac.view_cliente"