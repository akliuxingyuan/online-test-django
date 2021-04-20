from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email_push = models.BooleanField(_('email push'), default=False)

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')
