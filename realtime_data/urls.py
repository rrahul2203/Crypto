from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^price/$', views.get_price_details, name='current_price'),
    re_path(r'^price/btc', views.QueryDatewise.as_view())
]