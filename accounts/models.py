from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
from accounts.mixins import UserModelMixin
from school.models import Courses


class UserProgress(models.Model):
    pass


class User(UserModelMixin, AbstractBaseUser):
    STATUSES = (
        (ADMIN := 'ADMIN', 'Администратор'),
        (AUTHOR := 'AUTHOR', 'Автор курса'),
        (STD := 'STUDENT', 'Студент'),
    )

    user_status = models.CharField('статус пользователя', max_length=25, choices=STATUSES, default=STD)
    courses = models.ForeignKey(Courses, models.DO_NOTHING, verbose_name='Курс')
    progress = models.ForeignKey(UserProgress, models.DO_NOTHING, verbose_name='Прогресс в обучении')
    last_name = models.CharField('фамилия', max_length=150)
    first_name = models.CharField('имя', max_length=30)
    middle_name = models.CharField('отчество', max_length=150)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.get_full_name() or self.get_username()