from django.shortcuts import render, redirect
from django.views import generic
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.messages.views import SuccessMessageMixin

from bases.views import SinPrivilegios

# Create your views here.
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm

class CategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class CategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_categoria"
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"

    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message="Categoria Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"

    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message="Categoria Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(SinPrivilegios, generic.DeleteView):
    permission_required = "inv.delete_categoria"
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = "obj"
    success_url = reverse_lazy("inv:categoria_list")

class SubCategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"

class SubCategoriaNew(SinPrivilegios, generic.CreateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"

    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    permission_required = "inv.add_subcategoria"
    success_message="Sub Categoria Creado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"

    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    permission_required = "inv.change_subcategoria"
    success_message="Sub Categoria Actualizado Satisfactoriamente"


    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    model = SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = "obj"
    success_url = reverse_lazy("inv:subcategoria_list")
    permission_required = "inv.delete_subcategoria"
    success_message="Sub Categoria se ha Eliminado Satisfactoriamente"


class MarcaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_marca"
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"


class MarcaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"

    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    permission_required = "inv.add_marca"
    success_message="Marca Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class MarcaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"

    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    permission_required = "inv.change_marca"
    success_message="Marca Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not marca:
        return redirect("inv:marca_list")

    if request.method == 'GET':
        contexto = {'obj':marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        messages.success(request, 'Marca Inactivada')
        return redirect("inv:marca_list")


    return render(request, template_name, contexto)

class UMView(SinPrivilegios, generic.ListView):
    model = UnidadMedida
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    permission_required = "inv.view_unidadmedida"


class UMNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"

    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:um_list")
    permission_required = "inv.add_unidadmedida"
    success_message="Unidad de medida Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class UMEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"

    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:um_list")
    permission_required = "inv.change_unidadmedida"
    success_message="Unidad de medida Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_unidadmedida', login_url='/login/')
def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not um:
        return redirect("inv:um_list")

    if request.method == 'GET':
        contexto = {'obj':um}

    if request.method == 'POST':
        um.estado = False
        um.save()
        return redirect("inv:um_list")


    return render(request, template_name, contexto)


class ProductoView(SinPrivilegios, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    permission_required = "inv.view_marca"


class ProductoNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"

    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    permission_required = "inv.add_producto"
    success_message="Producto Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class ProductoEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"

    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    permission_required = "inv.change_producto"
    success_message="Producto Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_producto', login_url='/login/')
def producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not producto:
        return redirect("inv:producto_list")

    if request.method == 'GET':
        contexto = {'obj':producto}

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return redirect("inv:producto_list")


    return render(request, template_name, contexto)