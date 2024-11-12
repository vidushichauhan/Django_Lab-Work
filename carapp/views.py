from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

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


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'carapp/signup.html'
    success_url = reverse_lazy('login_here')

def login_here(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('homepage')  # Redirect to homepage
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Login details are incorrect.')
    return render(request, 'carapp/login_here.html')

@login_required
def logout_here(request):
    logout(request)
    return redirect('homepage')

@login_required
def list_of_orders(request):
    # Check if the logged-in user is a Buyer
    try:
        buyer = request.user.buyer  # Fetch the buyer object for the user
    except AttributeError:
        return HttpResponse('You are not registered as a buyer.')

    # Retrieve all orders placed by the buyer
    orders = buyer.ordervehicle_set.all()

    # Pass orders to the template
    return render(request, 'carapp/list_of_order.html', {'orders': orders})

def homepage(request):
    # Increment session counter
    session_counter = request.session.get('counter', 0)
    request.session['counter'] = session_counter + 1

    # Set cookie
    response = render(request, 'carapp/homepage.html', {'counter': session_counter})
    response.set_cookie('last_visit', 'Welcome!', max_age=10)
    return response

