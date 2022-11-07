from django.contrib import admin
from django.urls import path
from .views import PostAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts', PostAPIView.as_view())
]