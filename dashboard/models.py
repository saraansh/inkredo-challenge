from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
# 	name = models.CharField(max_length=200)	
# 	email = models.CharField(max_length=200)
# 	username = models.CharField(max_length=50)
# 	password = models.CharField(max_length=50)
# 	active = models.BooleanField(default=True)

class Company(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	website = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name