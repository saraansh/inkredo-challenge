from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, ProfileRegistrationForm
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Company


def home(request):
	context = {
		'companies': Company.objects.all()
	}
	return render(request, 'dashboard/home.html', context)


def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		profile_form = ProfileRegistrationForm(request.POST, request.FILES)
		if user_form.is_valid(): and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			username = user_form.cleaned_data.get('username')
			messages.sucess(request, f'Account for {username} has been successfully created!')
			return redirect('dashboard-home')
	else:
		user_form = UserRegistrationForm()
		profile_form = ProfileRegistrationForm()
	context = {
		'user_form': user_form,
		'profile_form': profile_form
	}
	return render(request, 'dashboard/register.html', context)


@login_required
def settings(request):
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.sucess(request, f'Your account has been updated!')
			return redirect('settings')
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'title': 'Settings',
		'user_form': user_form,
		'profile_form': profile_form
	}
	return render(request, 'dashboard/settings.html', context)