from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm
from .models import Company

def home(request):
	context = {
		'companies': Company.objects.all()
	}
	return render(request, 'dashboard/home.html', context)

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('dashboard-home')
	else:
		form = UserRegistrationForm()
	return render(request, 'dashboard/register.html', {'form': form})

@login_required
def settings(request):
	return render(request, 'dashboard/settings.html', {'title': 'Settings'})