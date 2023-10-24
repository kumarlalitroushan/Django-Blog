from django.urls import path
from . import views 
from .views import PostListView, PostDetailView

# urlpatterns = [
#     path('', views.home, name='blog-home'),
#     path('about/', views.about, name='about-page')
# ]
 
# Replacing views.home with PostListView
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about-page')
]

# <app>/<model>_<viewtype>.html