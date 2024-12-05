from django.shortcuts import render, redirect
from .models import ParkingSpot

def available_parking(request):
    # Fetch all available parking spots from the database
    spots = ParkingSpot.objects.filter(available=True)
    return render(request, 'available_parking.html', {'spots': spots})

def reserve_parking(request, spot_id):
    # Get the parking spot by its ID
    spot = ParkingSpot.objects.get(id=spot_id)

    # Mark the spot as reserved
    spot.available = False
    spot.save()

    # Render a confirmation page
    return render(request, 'reserve_parking.html', {'spot': spot})
