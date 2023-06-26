from django.shortcuts import render, redirect, HttpResponse
from utils.auth import authenticate_user
from .models import User
from django.contrib import messages
# import bcrypt

# Create your views here.
def enter(request):
  if 'uid' not in request.session:
    return render(request, "login_reg/login_reg.html")
  else:
    return redirect('/trips')

@authenticate_user
def welcome(request, user_id):
  data = {
    'user' : User.objects.get(id=user_id)
  }
  return render(request, "login_reg/welcome.html", data)

def register(request):
  if 'uid' in request.session:
    return redirect('dash')
  else:
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
      for field, error_msg in errors.items():
        messages.error(request, error_msg)
        return redirect('/')
    else:
      # user creation moved to reg validator in models
      
      # initiate uid in session (i.e. keep them logged in)
      user = User.objects.filter(email = request.POST['email'])
      user = user[0]
      request.session['uid'] = user.id
      return redirect('/trips')

def login(request):
  if 'uid' in request.session:
    return redirect('/trips')
  else:
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
      for error, msg in errors.items():
        messages.error(request, msg)
      return redirect('/')
    else:
      user = User.objects.filter(email = request.POST['email'])
      user = user[0]
      # if bcrypt.checkpw(request.POST['pw'].encode(), user.pw_hash.encode()):
      #   return render(request, "login_reg/welcome.html")
      request.session['uid'] = user.id
      return redirect('/trips')

def logout(request):
  request.session.clear()
  return redirect('root')