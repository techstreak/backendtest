from django.urls import path
from . import views

from .views import display_data


urlpatterns = [
    path('data/', display_data, name='display_data'),
    path('', views.get_all_products, name='all-products'),
    path('products/', views.get_all_products, name='all-products'),
    path('products/<int:product_id>/', views.get_product, name='product-detail'),
    #path('products/create/', views.create_product, name='create-product'),  # Add URL pattern for create_product view
    # Add URL patterns for update and delete views if needed
    path('', views.index, name='index'),

    
]
