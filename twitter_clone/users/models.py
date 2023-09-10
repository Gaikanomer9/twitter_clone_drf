from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models



class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    username = models.CharField(
        max_length=128, unique=True,
        verbose_name='Ник-нейм пользователя')
    email = models.EmailField(blank=False, unique=True,
                              verbose_name='Электронная почта')
    first_name = models.CharField('Имя', max_length=128)
    last_name = models.CharField('Фамилия', max_length=128)
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers',
        verbose_name='Подписки', blank=True)
    

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username