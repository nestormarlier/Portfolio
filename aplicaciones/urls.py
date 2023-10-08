from django.urls import path
from .views import home,pag404

urlpatterns = [
    path('', home, name='home'),
    path('404/', pag404, name='404'),
]