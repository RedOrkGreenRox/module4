from django.contrib import admin
from django.urls import path, include
from .views import profile_view, login_view, logout_view

urlpatterns = [
    path('auth/', profile_view, name='auth'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]
