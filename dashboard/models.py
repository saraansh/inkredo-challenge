from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	website = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user.username} Profile'