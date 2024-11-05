from django.db import models
from django.contrib.auth.models import User

# CarType model to represent categories of cars
class CarType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

# Vehicle model to represent individual vehicles
class Vehicle(models.Model):
    car_type = models.ForeignKey(CarType, related_name='vehicles', on_delete=models.CASCADE)
    car_name = models.CharField(max_length=200)
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)  # Default inventory set to 0
    instock = models.BooleanField(default=True)  # Boolean to track availability
    features = models.CharField(
        max_length=255,
        choices=[
            ('CC', 'Cruise Control'),
            ('AI', 'Audio Interface'),
            ('AB', 'Airbags'),
            ('AC', 'Air Conditioning'),
            ('SH', 'Seat Heating'),
            ('PA', 'ParkAssist'),
            ('PS', 'Power Steering'),
            ('RC', 'Reversing Camera'),
            ('AS', 'Auto Start/Stop'),
        ],
        blank=True
    )

    def save(self, *args, **kwargs):
        # Automatically set instock to False if inventory is 0
        self.instock = self.inventory > 0
        super(Vehicle, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.car_name} ({self.car_type.name}) - ${self.car_price}"

# Buyer model with Many-to-Many relation to CarType
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=300)
    AREA_CHOICES = [
        ('W', 'Windsor'),
        ('T', 'Toronto'),
        ('L', 'Waterloo'),
        ('C', 'Chatham'),
    ]
    area = models.CharField(max_length=2, choices=AREA_CHOICES, default='W')
    interested_in = models.ManyToManyField(CarType, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.area}"

# OrderVehicle model to track orders with status
class OrderVehicle(models.Model):
    STATUS_CHOICES = [
        (0, 'Cancelled'),
        (1, 'Placed'),
        (2, 'Shipped'),
        (3, 'Delivered'),
    ]
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"Order: {self.buyer.user.username} - {self.vehicle.car_name} (Status: {self.get_status_display()})"

    def total_price(self):
        return self.quantity * self.vehicle.car_price

class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    semester = models.PositiveIntegerField()
    personal_link = models.URLField()

    class Meta:
        ordering = ['first_name']  # Sort by first name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
