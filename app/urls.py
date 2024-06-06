from django.urls import path
from . import views

urlpatterns = [
    path('', views.bus_ticket_view, name='index'),
]
