from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime

from .models import User, Activity

def index(request):
    return render(request, "schedule/index.html")

@login_required
def activities(request, time):
    activities = Activity.objects.filter(user=request.user)
    valid = []
    for activity in activities:
        passed = False
        activity_month = int(activity.date[5:7])
        activity_day = int(activity.date[8:])
        if activity_month == datetime.now().month:
            if activity_day < datetime.now().day:
                passed = True
        if passed == True:
            passed_activity = Activity.objects.get(id=activity.id)
            passed_activity.delete()
        else:
            if time == "today":
                if activity_day == datetime.now().day:
                    valid.append(activity)
            if time == "week":
                if activity_day - datetime.now().day < 7:
                    valid.append(activity)
            if time == "month":
                if activity_month == datetime.now().month:
                    valid.append(activity)
    
    return JsonResponse([activity.serialize() for activity in valid], safe=False)

@login_required
def new_activity(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["description"]
        date = request.POST["time"]
        user = User.objects.get(pk=request.user.id)
        activity = Activity(user=user, title=title, content=content, date=date)
        activity.save()
        return HttpResponseRedirect(reverse(index))

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
            return render(request, "schedule/index.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "schedule/index.html")
    
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
