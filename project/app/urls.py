from django.urls import path
from .views import nav, main

urlpatterns = [
    path('', nav, name='nav'),
    path('main', main, name='main'),
]