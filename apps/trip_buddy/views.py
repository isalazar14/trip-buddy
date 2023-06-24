from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from ..login_reg.models import User
from .models import Trip

# Create your views here
def dashboard(request):
  user_id = None
  try:
    user_id = request.session['uid']
  except KeyError:
    return redirect('/')
  user = User.objects.get(id=user_id)
  data = {
    'user' : user,
    # 'my_trips' : user.trips_created.all().order_by('-created_at'),
    'my_trips' : user.trips_attending.all(),
    'other_trips': Trip.objects.exclude(created_by=user).exclude(people=user)
  }
  return render(request, 'trip_buddy/dashboard.html', data)
  # return HttpResponse('trip buddy app home page')

def create(request):
  if request.method=='GET':
    data = {
      'fname' : User.objects.get(id=request.session['uid']).fname
    }
    return render(request, 'trip_buddy/create_trip.html', data)

  if request.method=='POST':
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
      for error, msg in errors.items():
        messages.error(request, msg)
      return redirect('/trips/create')
    else:
      trip = request.POST

    # make new trip in db
      user = User.objects.get(id=request.session['uid'])
      new_trip = Trip.objects.create(
        created_by = user,
        name = trip['name'],
        destination = trip['destination'],
        start = trip['start'],
        end = trip['end'],
        plan = trip['plan'],
        )
      # add new trip to user's 'trips_attending'
      # User.objects.get(id=int(request.session['uid'])).add(new_trip)
      new_trip.people.add(user)
      return redirect('/trips')

def details(request, tid):
  trip = Trip.objects.get(id=tid)
  data = {
    'fname': User.objects.get(id=request.session['uid']).fname,
    'trip' : trip,
    'people': trip.people.exclude(id=request.session['uid'])
  }
  return render(request, 'trip_buddy/trip_details.html', data)

def edit(request, tid):
  if request.method=='GET':
    data = {
      'trip' : Trip.objects.get(id=tid)
    }
    return render(request, 'trip_buddy/edit_trip.html', data)
  
  if request.method=='POST':
    new = request.POST
    trip = Trip.objects.get(id=tid)
    trip.name = new['name']
    trip.destination = new['destination']
    trip.start = new['start']
    trip.end = new['end']
    trip.plan = new['plan']
    trip.save()
    return redirect('/trips')

def remove(request, tid):
  Trip.objects.get(id=tid).delete()
  return redirect('/trips')

def join(request):
  trip = Trip.objects.get(id=request.POST['tid'])
  user = User.objects.get(id=request.session['uid'])
  trip.people.add(user)
  return redirect('/trips')

def leave(request):
  trip = Trip.objects.get(id=request.POST['tid'])
  user = User.objects.get(id=request.session['uid'])
  trip.people.remove(user)
  return redirect('/trips')