from django.contrib import admin
from django.urls import path
from .views import PostAPIView

urlpatterns = [
    path('posts', PostAPIView.as_view())
]