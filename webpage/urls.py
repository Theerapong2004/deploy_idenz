from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path('Travel_data.json', views.Travel_data, name='Travel_data')
]
