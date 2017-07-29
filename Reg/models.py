# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserData(models.Model):

    phone = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.phone