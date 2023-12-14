from django.urls import path
from . import views
from .views import ProductListCreateAPIView, OrderListCreateAPIView


urlpatterns = [
    path('', views.home, name='home'),
    path('basepage/', views.basepage, name='basepage'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('add/', views.add_product, name='add'),
    path('product_list/', views.product_list, name='product_list'),
    path('edit/<int:id>', views.edit_product, name='edit'),
    path('delete/<int:id>/', views.delete_product, name='delete'),
    path('order', views.order_product, name='order'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('product_popularity/', views2.visual_representation_product_popularity, name='product_popularity'),
    path('products_api/', ProductListCreateAPIView.as_view(), name='products_api'),
    path('orders_api/', OrderListCreateAPIView.as_view(), name='orders_api'),
]
