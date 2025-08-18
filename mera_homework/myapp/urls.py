from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="hom"),
    path("a", views.about, name="about"),
    path("c", views.contact, name="con"),
    path("ou", views.Courses, name="cou"),
    path("d", views.Dropdown, name="dro"),
    path("e", views.Events, name="eve"),
    path("p", views.Pricing, name="pri"),
    path("t", views.Trainers, name="train"),
]