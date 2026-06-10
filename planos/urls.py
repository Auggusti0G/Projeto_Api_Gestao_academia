#-------------------------------------------
#-------- Criação de urls do app planos-----
#-------------------------------------------

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PlanoViewSet

router = DefaultRouter()

router.register(
    r'planos',
    PlanoViewSet
)

urlpatterns = [
    path('', include(router.urls)),
]