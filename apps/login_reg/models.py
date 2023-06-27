from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime, timedelta
import re
import bcrypt

class UserManager(models.Manager):
  def reg_validator(self, form_data):
    print(f'form_data:\n{form_data}')
    errors = {}

    if len(form_data['fname']) < 2:
      errors['fname'] = "First name must be at least 2 characters"
      
    if len(form_data['lname']) < 2:
      errors['lname'] = "Last name must be at least 2 characters"
      
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not email_regex.match(form_data['email']):
      errors['email'] = "Invalid email address"
    else:
      if len(User.objects.filter(email=form_data['email'])) > 0:
        errors['email'] = f"{form_data['email']} is already registered, please log in."
    
    if form_data['dob'] == '':
      errors['dob'] = "Date of birth is required."
    else:
      # dob = datetime.strptime(form_data['dob'], '%Y-%m-%d')
      # print(f"dob: {form_data['dob']}")
      # print(f"today: {date.today()}")
      
      dob = form_data['dob'].split('-')
      for i in range(len(dob)):
        dob[i] = int(dob[i])
        
      today = date.today().strftime('%Y-%m-%d')
      today = today.split('-')
      for i in range(len(today)):
        today[i] = int(today[i])

      min_age = 13
    
      if today[0] - dob[0] < min_age:
        errors['dob'] = f"Must be at least {min_age} years old"
      elif today[0] - dob[0] == 13:
        if today[1] >= dob[1] and today[2] >= dob[2]:
          pass
        else:
          errors['dob'] = f"Must be at least {min_age} years old"
    
    if len(form_data['pw']) < 8:
      errors['pw'] = 'Password must be at least 8 characters long'
    
    if len(errors) == 0:
      salt = bcrypt.gensalt()
      pw_hash = bcrypt.hashpw(form_data['pw'].encode(), salt)
      User.objects.create(
        fname = form_data['fname'],
        lname = form_data['lname'],
        email = form_data['email'],
        pw_hash = pw_hash,
        salt = salt,
        dob = form_data['dob']
      )
    return errors

  def login_validator(self, form_data):
    errors = {}
    print(form_data)
    email = form_data['email']
    user = User.objects.filter(email = email)
    if user:
      user = user[0]
      if not bcrypt.checkpw(form_data['pw'].encode(), user.pw_hash.encode()):
        errors['pw'] = f"Password entered is incorrect for this user"
    else:
      errors['email'] = f"{form_data['email']} not found. Please register."
    return errors




# Create your models here.
class User(models.Model):
  fname = models.CharField(max_length=20)
  lname = models.CharField(max_length=20)
  email = models.CharField(max_length=50, unique=True)
  pw_hash = models.CharField(max_length=100)
  salt = models.CharField(max_length=32)
  dob = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()