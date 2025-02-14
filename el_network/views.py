from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from .models import NetworkNode, Supplier, Product
from .serializers import NetworkNodeSerializer, SupplierSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class IsActiveEmployee(permissions.BasePermission):  # Custom permission
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]  # Require active employee status

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActiveEmployee]  # Require active employee status

class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]  # Require active employee status
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['country']
    search_fields = ['name', 'city']
    ordering_fields = ['name', 'city']
