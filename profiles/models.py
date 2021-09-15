from django.db import models
from datetime import datetime 

# Create your models here.
class Profiles(models.Model):
  first_name = models.CharField(max_length=100)
  photo = models.CharField(max_length=5000)
  birthday = models.DateField(auto_now=False, default=datetime.today)
  bio = models.CharField(max_length=500)
  job_title = models.CharField(max_length=100, blank=True)
  company = models.CharField(max_length=100, blank=True)
  school = models.CharField(max_length=100, blank=True)
  covid_vaccination_status = models.BooleanField(default=True, blank=True)
  current_city = models.CharField(max_length=50)
  hometown = models.CharField(max_length=50)
  gender = models.CharField(max_length=100)
  sexual_orientation = models.CharField(max_length=100)
  height = models.CharField(max_length=100)
  astrological_sign = models.CharField(max_length=100)
  interests_hobbies = models.CharField(max_length=100)
  favorite_restaurant = models.CharField(max_length=100)
  favorite_bar = models.CharField(max_length=100)
  religion = models.CharField(max_length=100)
  drinking = models.CharField(max_length=100)
  smoking = models.CharField(max_length=100)
  kids = models.CharField(max_length=100)
  politics = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name