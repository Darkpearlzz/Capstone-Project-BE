from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'date_and_time', 'capacity')
    list_filter = ('date_and_time', 'location')