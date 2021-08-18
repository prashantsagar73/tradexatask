from django.urls import path
from .import views
from .views import ProductDetailView

urlpatterns= [
    path('', views.home,name ="Product_home"),
    path('post/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),

]