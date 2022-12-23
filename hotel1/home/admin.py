from django.contrib import admin
from .models import City, Hotel, Reservation, Room

admin.site.register(City)
admin.site.register(Hotel)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        'room',
        'guest',
        'user',
        'check_in',
        'check_out',
    ]

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "hotel",
        "type",
        "price",
    ]

