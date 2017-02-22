from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Qs(models.Model):
	quote = models.CharField(max_length=511)
	date = models.DateField(("Date"), default=datetime.date.today)
	slug = models.SlugField(unique=True)