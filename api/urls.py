from rest_framework import routers
from .apis import ClientesViewSet
from django.urls import path,include
router = routers.DefaultRouter()

router.register('cliente', ClientesViewSet, 'project')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]