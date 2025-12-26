from django.contrib import admin
from .models import Movie, Seat


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'duration')
    search_fields = ('title',)


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_booked')
    list_filter = ('is_booked',)