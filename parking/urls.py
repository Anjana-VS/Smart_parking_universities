from django.urls import path
from . import views

urlpatterns = [
    path('', views.available_parking, name='available_parking'),  # Display available parking spots
    path('reserve_parking/<int:spot_id>/', views.reserve_parking, name='reserve_parking'),  # Reserve parking spot
]
