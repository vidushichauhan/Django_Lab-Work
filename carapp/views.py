from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import CarType, Vehicle, TeamMember
from django.shortcuts import render


# Homepage view to list all car types
def homepage(request):
    cartype_list = CarType.objects.all().order_by('id')
    return render(request, 'carapp/homepage.html', {'cartype_list': cartype_list})

# View to display up to 10 vehicles, sorted by price (descending)
def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by('-car_price')[:10]
    response = HttpResponse()
    heading = '<p>' + 'Top 10 Vehicles (Descending Price):' + '</p>'
    response.write(heading)
    for vehicle in vehicles:
        para = f"<p>{vehicle.car_name} - ${vehicle.car_price}</p>"
        response.write(para)
    return response

# About us page view
def aboutus(request):
    return render(request, 'carapp/aboutus.html')

# View to show vehicles associated with a specific car type
def cardetail(request, cartype_no):
    cartype = get_object_or_404(CarType, pk=cartype_no)
    vehicles = Vehicle.objects.filter(car_type=cartype)
    return render(request, 'carapp/cardetail.html', {'cartype': cartype, 'vehicles': vehicles})


def team_members(request):
    members = TeamMember.objects.all()
    return render(request, 'carapp/team_members.html', {'members': members})

def vehicles(request):
    vehicle_list = Vehicle.objects.all()
    return render(request, 'carapp/vehicles.html', {'vehicle_list': vehicle_list})

def orderhere(request):
    return HttpResponse("You can place your order here.")
