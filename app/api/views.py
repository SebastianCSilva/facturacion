from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_list_or_404

from .serializers import ProductoSerializer
from inv.models import Producto

from django.db.models import Q

class ProductoList(APIView):
    """Retorno de todos los productos"""
    def get(self, request):
        prod = Producto.objects.all()
        data = ProductoSerializer(prod, many=True).data
        return Response(data)


class ProductoDetalle(APIView):
    """Retorno de producto individual"""
    def get(self, request, codigo):
        prod = get_list_or_404(Producto, Q(codigo=codigo)|Q(codigo_barra=codigo))
        data = ProductoSerializer(prod).data
        return Response(data)
