from django.contrib import admin

from .models import Especialidades, DadosMedico, DatasAbertas, Documento

admin.site.register(Especialidades)
admin.site.register(DadosMedico)
admin.site.register(DatasAbertas)
admin.site.register(Documento)