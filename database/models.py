from django.db import models

class Doctor(models.Model):
	first_name = models.CharField(max_length=50)
	last_surname = models.CharField(max_length=50)
