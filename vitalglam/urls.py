from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
