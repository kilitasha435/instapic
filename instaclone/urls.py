from django.urls import path, include
from .views import (
    PostListView,
    PostCreateView
)
app_name = 'insta'

urlpatterns = [
    path('',PostListView.as_view(),name ='post_list'),
    path('new/',PostCreateView.as_view,name='post_create'),
]