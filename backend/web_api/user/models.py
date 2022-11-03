import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **kwargs):
        values = [username, email]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError(f'The {field_name} value must be set')

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        # kwargs.setdefault('is_author', False)
        return self._create_user(username, email, password, **kwargs)

    def create_superuser(self, username, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        # kwargs.setdefault('is_author', False)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        # if kwargs.get('is_author') is not False:
        #     raise ValueError('Superuser can not be author.')

        return self._create_user(username, email, password, **kwargs)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), blank=True, null=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    object = CustomUserManager()

    def __str__(self):
        return self.username