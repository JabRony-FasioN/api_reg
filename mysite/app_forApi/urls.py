from django.urls import path
from . import views

urlpatterts = [
    path('', views.getData)
]