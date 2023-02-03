from django.contrib import admin
from django.urls import path, include
from semiauto.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cliente', ClienteViewSet)
router.register('veiculo', VeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/<int:pk>/veiculos/', ListaVeiculosCliente.as_view()),
]
