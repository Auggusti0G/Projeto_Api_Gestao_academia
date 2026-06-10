#------------------------------------------
#--Registrando o aplicativo do instrutor---
#------------------------------------------

from django.contrib import admin
from .models import Instrutor

admin.site.register(Instrutor)