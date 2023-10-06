from django.urls import path
from .views import home

urlpatterns = [
    path('portfolio/', home, name='home'),
]