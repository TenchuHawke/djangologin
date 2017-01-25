from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages

def index(request):
    return render(request, 'login/index.html')

def login(request):
    if request.method == "POST":
        response_from_models = Users.objects.check_user(request.POST)
        #check to make sure it passed validation
        route=check_login(request, response_from_models)
        if route:
            return redirect('/login/success')
    return redirect('/login/index')

def register(request):
    if request.method == "POST":
        print request.POST
        response_from_models = Users.objects.add_user(request.POST)
        #check to make sure it passed validation
        route=check_login(request, response_from_models)
        if route:
            return redirect('/login/success')
    return redirect('/login/index')

def check_login(request, response_from_views):
    if not response_from_views['status']:
        for error in response_from_views['errors']:
            messages.error(request, error)
        return False
    else:
        request.session['user_id'] = response_from_views['user'][0].id
        request.session['username'] = Users.objects.only('first_name').get(id=request.session['user_id']).first_name
        return True


def success(request):
    if not request.session['user_id']:
        messages.error(request, "Must be logged in!")
        return redirect('/login/index')
    return render(request, 'login/success.html')

def logout(request):
    request.session.clear()
    return redirect('/login/index')
