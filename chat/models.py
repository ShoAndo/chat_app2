from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Room(models.Model):
  name = models.CharField('ルーム名', max_length=100)
  users = models.ManyToManyField(User)

  def __str__(self):
    return self.name

class Message(models.Model):
  content = models.CharField('内容', max_length=200, null=True, blank=True, default='')
  image = models.ImageField(upload_to='images', null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=datetime.now())
