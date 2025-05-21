from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NodeViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'nodes', NodeViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
