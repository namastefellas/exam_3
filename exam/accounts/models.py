from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='User', blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Avatar')

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'