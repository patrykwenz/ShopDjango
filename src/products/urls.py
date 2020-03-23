from django.contrib import admin
from django.urls import path, include
from .views import HomeView, ProductView, add_to_cart, remove_from_cart, OrderSummaryView, remove_single_item_from_cart

urlpatterns = [
    path('', HomeView.as_view(), name="shop_views-home"),
    path('product/<pk>', ProductView.as_view(), name="shop_views-product"),
    path('add-to-cart/<pk>', add_to_cart, name="shop_views-add-to-cart"),
    path('remove-from-cart/<pk>', remove_from_cart, name="shop_views-remove-from-cart"),
    path('summary/', OrderSummaryView.as_view(), name="shop_views-summary"),
    path('remove-item-from-cart/<pk>/', remove_single_item_from_cart,
         name='shop_views-remove-single-item-from-cart'),
    # path('checkout/',, name="shop_views-checkout")

]
