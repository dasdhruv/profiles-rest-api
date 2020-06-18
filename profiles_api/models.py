# Default user model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
	"""Manager for user profiles"""

	def create_user(self, email, name, password=None):
		"""Create a new user profile"""
		if not email:
			raise ValueError('Users must have an email address')

		# email will be converted to normalized form using BaseUserManager.normalize_email function
		email = self.normalize_email(email)

		# email and name will be passed to the function BaseUserManager.model
		user = self.model(email=email, name=name)

		# set_password is used to mock the password into #s
		user.set_password(password)
		# Any RDBMS can be configured by using the statements
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password):
		"""Create and save a new superuser with given details"""
		# Since superuser is also a user
		user = self.create_user(email, name, password)

		# The user is superuser
		user.is_superuser = True

		# The user is an office staff
		user.is_staff = True

		# Save setails in db
		user.save(using=self._db)

		return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Database model for users in the system"""
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	# objects will hold user's manager profile
	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		"""Retrieve full name for user"""
		return self.name

	def get_short_name(self):
		"""Retrieve short name of user"""
		return self.name

	def __str__(self):
		"""Return string representation of user"""
		return self.email
