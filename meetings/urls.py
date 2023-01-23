from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.roomList, name="rooms"),
    path('newMeeting', views.new, name="newMeeting")
]