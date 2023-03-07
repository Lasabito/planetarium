from django.urls import path

from Planetarium.web.views import IndexView, room_info_view, CreateRoom, EditRoom, DeleteRoom

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('create_new/', CreateRoom.as_view(), name='create_new'),
    path('info/<int:pk>/', room_info_view, name='info'),
    path('update/<int:pk>/', EditRoom.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteRoom.as_view(), name='delete'),
]
