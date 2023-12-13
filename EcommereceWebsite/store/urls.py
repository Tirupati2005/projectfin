from django.urls import path
from . import views
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
]
