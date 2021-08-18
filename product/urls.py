from django.urls import path
from .import views
from .views import PostDetailView

urlpatterns= [
    path('', views.home,name ="Product_home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="product_detail"),

]