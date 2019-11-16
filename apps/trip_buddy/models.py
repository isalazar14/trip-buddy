from django.db import models
from ..login_reg.models import User
from datetime import date, datetime

class TripManager(models.Manager):
  def trip_validator(self, form_data):
    errors = {}
    if len(form_data['name']) < 2:
      errors['name'] = "Trip name must be longer than 3 letters"

    if len(form_data['destination']) < 3:
      errors['destination'] = " Destination must be longer than 3 letters"

    if len(form_data['plan']) < 3:
      errors['plan'] = "Plan must be longer than 3 letters"

    # start = datetime.strptime(form_data['start'], "%Y-%m-%d")
    # if start < date.today():
    #   errors['start'] = "Start date must be in the future."

    # end = datetime.strptime(form_data['end'], "%Y-%m-%d")
    # if end < date.today():
    #   errors['end'] = "End date must be in the future."
    # elif end < start:
    #   errors['end'] = "End date must be after start date"

    if len(form_data['end']) < 3:
      errors['end'] = " must be longer than "


    return errors

# Create your models here.
class Trip(models.Model):
  created_by = models.ForeignKey(User, related_name='trips_created')
  name = models.CharField(max_length=50)
  destination = models.CharField(max_length=25)
  start = models.DateField()
  end = models.DateField()
  plan = models.TextField()
  people = models.ManyToManyField(User, related_name='trips_attending')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = TripManager()
  