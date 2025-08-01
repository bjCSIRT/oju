from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, PermissionViewSet

router = DefaultRouter()
router.register(r'permissions', PermissionViewSet)
router.register(r'', RoleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]