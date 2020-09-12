from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    message = ''
    if request.method == 'POST':
        name = request.POST["firstname"]
        password = request.POST["password"]
        # in this case firstname acts like a username which is unique
        # could also use email since email is unique
        try:
            user = User.objects.get(firstname=name)
        except:
            user = None

        if user is not None:
            if password == user.password:
                return HttpResponseRedirect(reverse("crud_project:dash"))
            else:
                message = "wrong credentials"
        else:
            message = "User not found"

    return render(request, "temp/index.html", {"message": message})


def dashboard(request):
    return render(request, "temp/dashboard.html", )


def users(request):
    user = User.objects.all()
    return render(request, "temp/viewusers.html", {"users": user})


def register(request):
    if request.method == 'POST':
        user = User(firstname=request.POST["firstname"], password=request.POST["password"], email=request.POST["email"],
                    lastname=request.POST["lastname"]
                    )
        user.save()
        return HttpResponseRedirect(reverse("crud_project:dash"))
    return render(request, "temp/register.html", )


def update(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        user.firstname = request.POST["firstname"]
        user.password = request.POST["password"]
        user.email = request.POST["email"]
        user.lastname = request.POST["lastname"]

        user.save()
        return HttpResponseRedirect(reverse("crud_project:view"))
    return render(request, "temp/update.html", {"user": user})


def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()

    return HttpResponseRedirect(reverse("crud_project:view"))
