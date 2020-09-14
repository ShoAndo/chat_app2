from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Room, Message
from .forms import MessageForm

@login_required
def index(request):
  user = request.user
  rooms = user.room_set.all()
  return render(request, 'chat/index.html', {'user': user, 'rooms': rooms})

class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'

def new(request):
  if request.method == 'POST':
    if request.POST['name'] and request.POST['user_id']:

      room = Room.objects.create(name=request.POST['name'])
      user = User.objects.get(id=request.POST['user_id'])
      room.users.add(user)
      room.users.add(request.user)
      
    return HttpResponseRedirect(reverse('index'))
  else:
    user = request.user
    users = User.objects.filter(~Q(id=user.id))
    return render(request, 'room/new.html', {'users': users, 'current_user': user})

def message(request, room_id):
  if request.method == 'POST':
    try:
      message = Message()
      print(request.POST)
      print(request.FILES)
      if request.POST['content']:
        message.content = request.POST['content']
      else:
        pass
     
      if request.FILES:
        message.image = request.FILES['image']
      else:
        pass

      room = Room.objects.get(id=room_id)
      message.room = room

      user = request.user
      message.user = user
      message.save()
      messages = Message.objects.filter(room_id=room.id)
      rooms = user.room_set.all()
      context = {'rooms': rooms, 'messages': messages, 'room': room }
      return HttpResponseRedirect(reverse('message', args=(room_id,)))

    except KeyError:
      user = request.user
      rooms = user.room_set.all()
      room = Room.objects.get(id=room_id)
      messages = Message.objects.filter(room_id=room.id)
      context = {'rooms': rooms, 'messages': messages, 'room': room }
      return HttpResponseRedirect(reverse('message', args=(room_id,)))
  else:
    user = request.user
    rooms = user.room_set.all()

    room = Room.objects.get(id=room_id)
    messages = Message.objects.filter(room_id=room.id)

    context = {'rooms': rooms, 'messages': messages, 'room': room }
    return render(request, 'message/index.html', context)

def room_delete(request, room_id):
  room = Room.objects.get(id=room_id)
  room.delete()
  user = request.user
  rooms = user.room_set.all()
  return render(request, 'chat/index.html', {'user': user, 'rooms': rooms})
