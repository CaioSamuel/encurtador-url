from django.urls import path
from . import views

urlpatterns = [
    path('encurtar', views.encurtar, name="encurtar"),
    path('<str:codigo_curto>/', views.redirecionar, name="redirecionar"),
]
