from django.urls import path
from . import views

urlpatterns = [
    path('', views.base,name='base'),
    path('user_login/', views.user_login,name='user_login'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('registration', views.Userreg,name='Reg')
    ]