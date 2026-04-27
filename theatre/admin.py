from django.contrib import admin
from .models import Actor, Genre, Play, TheatreHall, Performance, Reservation, Ticket


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    filter_horizontal = ("genres", "actors")


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = ("name", "rows", "seats_in_row", "capacity")


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("play", "theatre_hall", "show_time")
    list_filter = ("show_time", "play")


class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 1


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("created_at",)
    inlines = (TicketInline,)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("performance", "row", "seat", "reservation")
    list_filter = ("performance",)
