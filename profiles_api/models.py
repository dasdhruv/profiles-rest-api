# Default user model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(this, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        # email will be converted to normalized form using BaseUserManager.normalize_email function
        email = this.normalize_email(email)

        # email and name will be passed to the function BaseUserManager.model
        user = this.model(email=email, name=name)

        # set_password is used to mock the password into #s
        user.set_password(password)
        # Any RDBMS can be configured by using the statements
        user.save(using=this._db)

        return user

    def create_superuser(this, email, name, password):
        """Create and save a new superuser with given details"""
        # Since superuser is also a user
        user = this.create_user(email, name, password)

        # The user is superuser
        user.is_superuser = True

        # The user is an office staff
        user.is_staff = True

        # Save setails in db
        user.save(using=this._db)

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

    def get_full_name(this):
        """Retrieve full name for user"""
        return this.name

    def get_short_name(this):
        """Retrieve short name of user"""
        return this.name

    def __str__(this):
        """Return string representation of user"""
        return this.email
