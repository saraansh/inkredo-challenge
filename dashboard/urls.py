from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="dashboard-home"),
    path('settings/', views.settings, name="dashboard-settings"),
]
