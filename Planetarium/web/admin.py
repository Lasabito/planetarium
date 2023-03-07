from django.contrib import admin

from Planetarium.web.models import NewRoomModel, Person


@admin.register(NewRoomModel)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'heading', 'date', 'time']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'for_room', 'seats']