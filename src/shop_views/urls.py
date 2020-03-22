from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name="shop_views-home"),
    path('about/', views.about_view, name="shop_views-about")

]
