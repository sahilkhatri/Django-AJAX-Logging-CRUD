from django.db import models

# Create your models here.
class CrudUser(models.Model):
	username = models.CharField(max_length=30, blank=True)
	firstname = models.CharField(max_length=30, blank=True)
	lastname = models.CharField(max_length=30, blank=True)
	email = models.CharField(max_length=100, blank=True, null=True)