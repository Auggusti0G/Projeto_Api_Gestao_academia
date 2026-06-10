#--------------------------------------------
#-----criacao do registro da app de plano----
#--------------------------------------------

from django.contrib import admin
from .models import Plano

admin.site.register(Plano)