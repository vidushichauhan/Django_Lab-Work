import django
import os

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carsite.settings')
django.setup()

from carapp.models import CarType, Vehicle, Buyer, OrderVehicle
from django.contrib.auth.models import User

# Add Car Types
car_types = {
    "Toyota": CarType.objects.create(name="Toyota"),
    "Nissan": CarType.objects.create(name="Nissan"),
    "Ford": CarType.objects.create(name="Ford"),
    "Honda": CarType.objects.create(name="Honda"),
    "Mercedes": CarType.objects.create(name="Mercedes"),
    "Cadillac": CarType.objects.create(name="Cadillac")
}

# Add Buyers
buyers_data = [
    {"username": "alex", "password": "alex", "shipping_address": "123 Paul Martin", "area": "W", "interested_in": ["Toyota", "Nissan", "Ford", "Honda", "Mercedes", "Cadillac"]},
    {"username": "ali", "password": "ali", "shipping_address": "444 St. Michel", "area": "T", "interested_in": ["Toyota", "Nissan", "Honda", "Cadillac"]},
    {"username": "lara", "password": "lara", "shipping_address": "788 Dominion Avenue", "area": "L", "interested_in": ["Honda", "Mercedes", "Cadillac"]},
    {"username": "roland", "password": "roland", "shipping_address": "127 Howard Avenue", "area": "C", "interested_in": ["Nissan", "Honda"]},
    {"username": "lina", "password": "lina", "shipping_address": "799 Wyandotte Street", "area": "W", "interested_in": ["Ford", "Honda", "Cadillac"]}
]

for data in buyers_data:
    user = User.objects.create_user(username=data["username"], password=data["password"])
    buyer = Buyer.objects.create(user=user, shipping_address=data["shipping_address"], area=data["area"])
    buyer.interested_in.set([car_types[name] for name in data["interested_in"]])

# Add Vehicles
vehicles_data = [
    {"car_name": "Corolla", "car_type": "Toyota", "car_price": 25000, "inventory": 5},
    {"car_name": "Camry", "car_type": "Toyota", "car_price": 33000, "inventory": 4},
    {"car_name": "RAV4", "car_type": "Toyota", "car_price": 50000, "inventory": 2},
    {"car_name": "ARIYA", "car_type": "Nissan", "car_price": 59000, "inventory": 0},
    {"car_name": "Sentra", "car_type": "Nissan", "car_price": 23500, "inventory": 4},
    {"car_name": "FUSION HYBRID", "car_type": "Ford", "car_price": 25000, "inventory": 14},
    {"car_name": "Escape SEL", "car_type": "Ford", "car_price": 39100, "inventory": 8},
    {"car_name": "Explorer XLT", "car_type": "Ford", "car_price": 35000, "inventory": 0},
    {"car_name": "EcoSport", "car_type": "Ford", "car_price": 25000, "inventory": 24},
    {"car_name": "Bronco Sport Badlands", "car_type": "Ford", "car_price": 45000, "inventory": 12},
    {"car_name": "CR-V", "car_type": "Honda", "car_price": 37000, "inventory": 8},
    {"car_name": "Civic", "car_type": "Honda", "car_price": 23000, "inventory": 19},
    {"car_name": "CLA 250", "car_type": "Mercedes", "car_price": 45000, "inventory": 10},
    {"car_name": "GLA 250", "car_type": "Mercedes", "car_price": 33000, "inventory": 12}
]

for vehicle in vehicles_data:
    Vehicle.objects.create(
        car_name=vehicle["car_name"],
        car_type=car_types[vehicle["car_type"]],
        car_price=vehicle["car_price"],
        inventory=vehicle["inventory"]
    )

# Add Orders
orders_data = [
    {"vehicle": "Corolla", "buyer": "alex", "quantity": 2, "status": 1},
    {"vehicle": "Sentra", "buyer": "lara", "quantity": 1, "status": 2},
    {"vehicle": "ARIYA", "buyer": "lina", "quantity": 1, "status": 0},
    {"vehicle": "Civic", "buyer": "roland", "quantity": 5, "status": 3}
]

for order in orders_data:
    OrderVehicle.objects.create(
        vehicle=Vehicle.objects.get(car_name=order["vehicle"]),
        buyer=Buyer.objects.get(user__username=order["buyer"]),
        quantity=order["quantity"],
        status=order["status"]
    )

print("Data populated successfully!")
