from django.contrib.admin import site, ModelAdmin
from .models import Room, Message
from .forms import RoomForm

class RoomAdmin(ModelAdmin):
  form = RoomForm

site.register(Room, RoomAdmin)

site.register(Message)