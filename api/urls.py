from django.urls import path
from . import views

urlpatterns = [
    path('efiscal', views.efiscal)
]
