from django.urls import path, include
from rest_framework import routers
from .views import NetworkNodeViewSet, SupplierViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'networknodes', NetworkNodeViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
