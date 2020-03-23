from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.about_view, name="shop_views-about")

]
