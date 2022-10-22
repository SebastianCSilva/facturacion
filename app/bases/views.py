from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
# Create your views here.

class SinPrivilegios(PermissionRequiredMixin):
    """Vista en clase para usuarios que no tengan privilegios necesarioas para funcion"""
    raise_exception=False
    redirect_field_name = "redirect_to"

    def handle_no_permission(self):
        self.login_url = 'bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'


class HomeSinPrivilegios(generic.TemplateView):
    template_name = 'bases/sin_privilegios.html'