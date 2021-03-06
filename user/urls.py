from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .import views

urlpatterns= [
     path('blog/', views.home,name ="Blog_home"),
     path('blog/', PostListView.as_view(), name ="Blog_home"),
     path('post/<int:pk>/', PostDetailView.as_view(), name ="post_detail"),
     path('post/<int:pk>/update/', PostUpdateView.as_view(), name ="post-update"),
     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name ="post-delete"),
     path('post/new/', PostCreateView.as_view(), name ="post-create"),
     path('about/', views.about,name ="about")
]