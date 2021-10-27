from django.urls import path

from . import views
from .views import SearchResultsView


urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:order_id>', views.order, name='order'),
    path('order/new', views.OrderCreateView.as_view(), name='order-new'),
    path('order/<int:pk>/update', views.OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete', views.OrderDeleteView.as_view(), name='order-delete'),
    path('image_order_product/new', views.ImageOrderProductCreateView.as_view(), name='image-order-product-new'),
    path('add_order_product/', views.OrderProductCreateView.as_view(), name='add-order-product'),
    path('add_order_product_pictures/<int:product_id>', views.add_pictures, name='add-order-product-picture'),
    path('take_product_pictures/', views.take_pictures, name='take-product-picture'),
    path('', views.index, name='index'),
]