from django.contrib.auth.models import User
from django.db import models


class Activate(models.Model):
    """ 仮登録したユーザを本登録するためのModel """

    user = models.OneToOneField(User)
    key = models.CharField(max_length=255, unique=True)
