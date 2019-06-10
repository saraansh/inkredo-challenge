from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Company

def home(request):
	context = {
		'companies': Company.objects.all()
	}
	return render(request, 'dashboard/home.html', context)

def settings(request):
	return render(request, 'dashboard/settings.html', {'title': 'Settings'})