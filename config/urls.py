from django.urls import path

from config import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('category/<int:category_id>', views.category_detail, name='category_detail'),
    path('product_list/', views.product_list, name='product_list'),
    path('contact/', views.contact, name='contact'),

]

