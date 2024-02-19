from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from inboxi.models.base import BaseUUIDTimestampModel


class UserMananger(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        if not full_name:
            raise ValueError("Users must have an full name")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, full_name, password):
        user = self.create_user(
            email=email,
            full_name=full_name,
            password=password
        )
        user.role = "admin"
        user.save(using=self._db)

        return user


class User(BaseUUIDTimestampModel, AbstractBaseUser):
    class Role(models.TextChoices):
        ADMIN = ("admin", "Admin")
        STAFF = ("staff", "staff")

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=225)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.STAFF)
    is_active = models.BooleanField(default=True)

    objects = UserMananger()

    REQUIRED_FIELDS = ["full_name"]
    USERNAME_FIELD = "email"

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.role == self.Role.ADMIN
