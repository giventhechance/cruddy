from django.urls import path

from .views import *

app_name = 'main'
urlpatterns = [
    path('show_products/', show_products, name='show_products'),
    path('add_form/', add_form, name='add_form'),
    path('add_product_modelform/', add_product_modelform, name='add_product_modelform'),
    path('add_product_input/', add_product_input, name='add_product_input'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('product_detail/<int:id>/update/', product_update, name='product_update'),
    path('product_detail/<int:id>/delete/', product_delete, name='product_delete'),
    path('product_detail/<int:id>/update_modelform/', product_update_modelform, name='product_update_modelform'),
]
