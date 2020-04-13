from django.contrib import admin
from django.urls import path, include
from .views import HomeView, ProductView, add_to_cart, remove_from_cart, OrderSummaryView, remove_single_item_from_cart, \
    AboutView

app_name = 'products'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('product/<pk>', ProductView.as_view(), name="product"),
    path('add-to-cart/<pk>', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<pk>', remove_from_cart, name="remove-from-cart"),
    path('summary/', OrderSummaryView.as_view(), name="summary"),
    path('remove-item-from-cart/<pk>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart')
    # path('checkout/',, name="shop_views-checkout")

]
