from django.urls import path

from . import views

app_name = "main"

urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "products/",
        views.products,
        name="products"
    ),

    path(
        "products/<slug:slug>/",
        views.product_detail,
        name="product_detail"
    ),

]