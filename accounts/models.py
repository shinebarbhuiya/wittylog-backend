import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserAccountManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            id=uuid.uuid4(),  # Add this line to generate a UUID
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Add this line for UUID field
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_registration = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True, max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    gender = models.CharField(max_length=10, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    device = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return str(self.first_name)  # Modify this line to return the UUID as a string
