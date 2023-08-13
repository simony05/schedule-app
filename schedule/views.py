from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError

from .models import User

def index(request):

    # If signed in, can view schedule
    if request.user.is_authenticated:
        return render(request, "schedule/index.html")

    # Else have to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def login_page(request):
    if request.method == "POST":

        # Sign in attempt
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "schedule/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "schedule/login.html")
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]

        # Check password confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "schedule/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create the new user with given information
        try:
            user = User.objects.create_user(username, username, password)
            user.save()
        except IntegrityError as error:
            print(error)
            return render(request, "schedule/register.html", {
                "message": "Username address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "schedule/register.html")
