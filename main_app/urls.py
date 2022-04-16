from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bikes/', views.bikes_index, name='index'),
    path('bikes/<int:bike_id>', views.bikes_detail, name='detail'),
    path('bikes/create/', views.BikeCreate.as_view(), name='bikes_create'),
    path('bikes/<int:pk>/update/', views.BikeUpdate.as_view(), name='bikes_update'),
    path('bikes/<int:pk>/delete/', views.BikeDelete.as_view(), name='bikes_delete'),
    path('bikes/<int:bike_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
    path('sockets/', views.Socketlist.as_view(), name='sockets_index'),
    path('sockets/create/', views.SocketCreate.as_view(), name='sockets_create'),
    path('bikes/<int:bike_id>/assoc_tool/<int:socket_id>/', views.assoc_tool, name='assoc_tool')
]