from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.movie_detail, name='detail'),
    path('movie/<int:movie_id>/seats/', views.seats, name='seats'),
    path('payment/<int:movie_id>/', views.payment, name='payment'),
]