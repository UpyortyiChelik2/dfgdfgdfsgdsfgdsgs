from django.urls import path
from . views import RoomListView, book_room
urlpatterns = [path('', RoomListView.as_view(), name='room_list'),
               path('room/<int:room_id>/book/', book_room, name='book_room'),
