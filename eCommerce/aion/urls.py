from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('login/', views.login_view, name='login'),
    ]
