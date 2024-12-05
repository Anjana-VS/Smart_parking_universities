from django.db import models

class ParkingSpot(models.Model):
    spot_name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='parking_images/', null=True, blank=True)  # Image field

    def __str__(self):
        return self.spot_name
