#--------------------------------------------
#--------Criação de View do app de Planos----
#--------------------------------------------

from rest_framework import viewsets

from .models import Plano
from .serializers import PlanoSerializer

class PlanoViewSet(viewsets.ModelViewSet):

    queryset = Plano.objects.all()

    serializer_class = PlanoSerializer