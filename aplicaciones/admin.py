from django.contrib import admin
from .models import Aplicaciones

admin.site.site_header = 'Mis Mejores Logros: Portafolio de Proyectos'
admin.site.index_title = 'Portfolio - Mis Proyectos '                 # default: 
admin.site.site_title = 'Sistema de administración' # default: "Django site admin"
admin.site.register(Aplicaciones)
