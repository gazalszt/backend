import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import City, Hotel, Reservation, Room
import datetime
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import signupform
from django.contrib import messages

# Create your views here.

def sinin(request):
    return render(request=request, template_name='templates/signin.html')

def home(request):
    return render(request=request, template_name='templates/home.html')

def contactus(request):
    return render(request=request, template_name='templates/contactus.html')

def lasvegas(request):
    return render(request=request, template_name='templates/lasvegas.html')

def hawaii(request):
    return render(request=request, template_name='templates/hawaii.html')

def newyork(request):
    return render(request=request, template_name='templates/newyork.html')

def losangeles(request):
    return render(request=request, template_name='templates/losangeles.html')

def chicago(request):
    return render(request=request, template_name='templates/chicago.html')

def signup(response):
    if response.method == "POST":
        form = signupform(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = signupform()

    return render(response, 'templates/signup.html', {"form": form})

def signin(request):
    if request.method == "POST":
        username =request.POST['username']
        password= request.POST['password']
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Successful Sign in")
            print("Login Successful")
            return redirect("/home")
        else:
            messages.warning(request, "Incorrect username or password")
            return redirect("/signin")
    return HttpResponse(render(request, "signin.html"))

def detail(request, location_id):
    return HttpResponse("<h2> You're looking at the Location id :  %s. </h2>" % location_id)

def hotel_list(request):
    city = request.GET.get("citylist")
    from_date = request.GET.get("check-in-date")
    to_date = request.GET.get("check-out-date")
    check_in_datetime = datetime.datetime.strptime(from_date,'%Y-%m-%d')
    check_out_datetime = datetime.datetime.strptime(to_date,'%Y-%m-%d')
    delta = check_out_datetime - check_in_datetime
    days = delta.days
    guest = int(request.GET.get("guestnumber"))
    city_DB = City.objects.get(name=city)
    hotels = Hotel.objects.prefetch_related("room_set").filter(city=city_DB)

    data = {
        'city': city,
        'check_in_date': check_in_datetime,
        'check_out_date': check_out_datetime,
        'from_date': from_date,
        'to_date': to_date,
        'guest': guest,
        'days': days,
        "hotels": [{"name": hotel.name, 'rooms': 
                        [{"id": room.id, "name": room.name, 'type':room.get_type_display(), 'price' : room.price, 'total_price': room.price * days * guest} for room in hotel.room_set.all()]} for hotel in hotels],
    }
    return render(request=request, template_name='templates/hotel-list.html', context={"data": data})

def reserve(request):
    if request.user.is_authenticated:
        roomId = int(request.GET.get("roomId"))
        from_date = request.GET.get("from-date")
        to_date = request.GET.get("to-date")
        guest = int(request.GET.get("guest"))
        check_in_datetime = datetime.datetime.strptime(from_date,'%Y-%m-%d')
        check_out_datetime = datetime.datetime.strptime(to_date,'%Y-%m-%d')
        Reservation.objects.create(
            room_id=roomId, 
            check_in = check_in_datetime,
            check_out = check_out_datetime,
            guest=guest,
            user = request.user)
        return HttpResponse("<h2>OK</h2>")
    else:
        return HttpResponse("<h2>Please login</h2>")


    
