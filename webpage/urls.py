from django.urls import path
from . import views  # ✅ ต้อง import views.py

urlpatterns = [
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("products/", views.products, name="products"),
    path("cart/", views.cart_view, name="cart"),
    path("contact/", views.contact_view, name="contact"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
]
