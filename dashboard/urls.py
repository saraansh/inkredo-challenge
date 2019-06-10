from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as dash_views

urlpatterns = [
	path('', dash_views.home, name="dashboard-home"),
	path('register/', dash_views.register, name="register"),
	path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name="login"),
	path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/logout.html'), name="logout"),
	path('settings/', dash_views.settings, name="dashboard-settings"),
]
