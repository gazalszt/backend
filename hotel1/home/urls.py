from django.urls import path
from . import views

urlpatterns = [
    path('signin/', view=views.signin, name='signin'),
    path('', view=views.home, name='home'),
    path('contactus/', view=views.contactus, name='contactus'),
    path('lasvegas/', view=views.lasvegas, name='lasvegas'),
    path('hawaii/', view=views.hawaii, name='hawaii'),
    path('newyork/', view=views.newyork, name='newyork'),
    path('losangeles/', view=views.losangeles, name='losangeles'),
    path('chicago/', view=views.chicago, name='chicago'),
    path('signup/', view=views.signup, name='signup'),  
    path('signup/', view=views.signup, name='signup'),
    path('reserve/', view=views.reserve, name='reserve'),
    path('hotel-list/', view=views.hotel_list, name='hotel-list'),
        # /home/4/
    path('<int:location_id>/', views.detail, name='detail'),
]