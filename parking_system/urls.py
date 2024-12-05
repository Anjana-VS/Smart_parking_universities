from django.contrib import admin
from django.urls import path, include
from parking import views

urlpatterns = [
    path('', views.available_parking, name='available_parking'),  # Root URL for available spots
    path('admin/', admin.site.urls),
    path('reserve_parking/<int:spot_id>/', views.reserve_parking, name='reserve_parking'),  # Reserve parking spot
]
