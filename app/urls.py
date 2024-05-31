from django.urls import path
from .views import *

app_name='app'


urlpatterns = [
    path("",home,name="home_page"),
    path('about/',about,name="about_page"),
    path('contact/',contact,name="contact_page"),
    path('product/add/',add_product,name="add_page"),
    path('product/',all_products,name="show_page"),
    path('product/delete/<int:id>/',delete_product, name="product_delete"),
    path('product/update/<int:id>/',product_update, name="product_update")

]
