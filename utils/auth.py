from django.shortcuts import redirect
from functools import wraps


def get_session_user_id(request):
  try:
    user_id = request.session["uid"]
    return user_id
  except KeyError:
    return None
  
### Auth decorator
def authenticate_user(view_function):
  @wraps(view_function)
  def wrapper(request, *args, **kwargs):
    user_id = get_session_user_id(request)
    if user_id == None:
      return redirect('root')
    return view_function(request, user_id, *args, **kwargs)
  return wrapper