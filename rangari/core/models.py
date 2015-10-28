from django.db import models
from enum import Enum

class Location(models.Model):
	class SelectLocation(Enum):
		Mumbai = "Mumbai"
		Pune = "Pune"


		@classmethod
		def as_tuple(cls):
			return ((item.value, item.name.replace('_', ' ')) for item in cls)
	select_loc = models.CharField(blank=False, max_length=50, choices=SelectLocation.as_tuple())


class Service(models.Model):
	class SelectService(Enum):
		Painting = "Painting"
		Water_prooffing = "Water prooffing"


		@classmethod
		def as_tuple(cls):
			return ((item.value, item.name.replace('_', ' ')) for item in cls)
	select_serv = models.CharField(blank=False, max_length=50, choices=SelectService.as_tuple())

class Login(models.Model):
	first_name = models.CharField(blank=False, max_length=200)
	last_name = models.CharField(blank=False, max_length=200)
	mob_no = models.CharField(blank=False, max_length=200, unique=True)
	email_id = models.EmailField(blank=False, max_length=200, unique=True)
	password = models.CharField(blank=False, max_length=200)


class CustomerEnquiry(models.Model):
	city = models.CharField(blank=False, max_length=50)
	service = models.CharField(blank=False, max_length=200)

