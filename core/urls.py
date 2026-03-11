from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
]