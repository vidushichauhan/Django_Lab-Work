"""
URL configuration for carsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from carapp import views
from carapp.views import SignupView, login_here, logout_here, list_of_orders

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', SignupView.as_view(), name='signup'),
    path('/homepage', views.homepage, name='homepage'),  # Homepage
    ##path('vehicles/', views.vehicle_list, name='vehicle_list'),  # Vehicle list
    path('aboutus/', views.aboutus, name='aboutus'),  # About us page
    path('<int:cartype_no>/', views.cardetail, name='cardetail'),  # Car type details

    path('team/', views.team_members, name='team_members'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('orderhere/', views.orderhere, name='orderhere'),



    path('login/', login_here, name='login_here'),
    path('logout/', logout_here, name='logout_here'),
    path('myorders/', list_of_orders, name='myorders'),
]
