from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_price_details, name='current_price'),
]