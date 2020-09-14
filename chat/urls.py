from django.urls import path
from . import views

urlpatterns = [
  path('', views.index , name="index"),
  path('accounts/signup/', views.SignUpView.as_view(), name="signup"),
  path('room/new/', views.new, name="newroom"),
  path('room/<int:room_id>/message/', views.message, name="message"),
  path('room/<int:room_id>/delete/', views.room_delete, name="delete"),
]