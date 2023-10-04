from django.contrib import admin
from django.urls import path, include
from .views import register_view, login_view, profile_view, logout_view

urlpatterns = [
    path('auth/', profile_view, name='auth'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
