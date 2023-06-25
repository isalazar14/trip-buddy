def getSessionUserId(request):
    try:
        user_id = request.session["uid"]
        return user_id
    except KeyError:
        return None