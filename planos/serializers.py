#----------------------------------------
#------Serializers do app de planos------
#----------------------------------------

from rest_framework import serializers
from .models import Plano

class PlanoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plano
        fields = '__all__'