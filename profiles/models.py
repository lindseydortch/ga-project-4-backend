from django.db import models
from datetime import datetime 

# Create your models here.
class Profiles(models.Model):
  first_name = models.CharField(max_length=100)
  photo = models.CharField(max_length=5000, blank=True)
  birthday = models.DateField(auto_now=True, blank=True)
  bio = models.CharField(max_length=500, blank=True)
  job_title = models.CharField(max_length=100, blank=True)
  company = models.CharField(max_length=100, blank=True)
  school = models.CharField(max_length=100, blank=True)
  covid_vaccination_status = models.CharField(max_length=100, blank=True)
  current_city = models.CharField(max_length=50, blank=True)
  hometown = models.CharField(max_length=50, blank=True)
  gender = models.CharField(max_length=100, blank=True)
  sexual_orientation = models.CharField(max_length=100, blank=True)
  height = models.CharField(max_length=100, blank=True)
  astrological_sign = models.CharField(max_length=100, blank=True)
  interests_hobbies = models.CharField(max_length=100, blank=True)
  favorite_restaurant = models.CharField(max_length=100, blank=True)
  favorite_bar = models.CharField(max_length=100, blank=True)
  religion = models.CharField(max_length=100, blank=True)
  drinking = models.CharField(max_length=100, blank=True)
  smoking = models.CharField(max_length=100, blank=True)
  kids = models.CharField(max_length=100, blank=True)
  politics = models.CharField(max_length=100, blank=True)
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name