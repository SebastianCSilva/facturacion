from django.urls import path

from .views import ProveedorView, ProveedorNew, ProveedorEdit

urlpatterns = [
    path('proveedor/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedor/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    #path('proveedor/inactivar/<int:id>', producto_inactivar, name='producto_inactivar'),
]