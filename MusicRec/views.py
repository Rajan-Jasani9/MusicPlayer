from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , DeleteView, UpdateView 
from django.urls import reverse_lazy
from django.urls import reverse

from django.views.decorators.cache import never_cache
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Songs

# Create your views here.
@login_required(login_url = reverse_lazy("index"))
def moodSelect(request, fname):
    context = {'fname': fname}
    return render(request, "homepage.html", context)

@login_required(login_url = reverse_lazy("index"))
def about(request):
    current_user = request.user
    fname = current_user.first_name
    context = {'fname': fname}

    return render(request, "about.html", context)

def contact(request):
    return render(request, "contact.html")

@login_required(login_url = reverse_lazy("index"))
def happysongs(request):
    
    current_user = request.user
    fname = current_user.first_name
    context = {'fname': fname}
    songs = Songs.objects.all().filter(option=1)
    return render(request, "happysongs.html", {'songs': songs, 'fname':fname} )


@login_required(login_url = reverse_lazy("index"))
def relaxingsongs(request):
    
    current_user = request.user
    fname = current_user.first_name
    songs = Songs.objects.all().filter(option=2)
    return render(request, "relaxingsongs.html", {'songs': songs, 'fname':fname} )


@login_required(login_url = reverse_lazy("index"))
def sadsongs(request):
    
    current_user = request.user
    fname = current_user.first_name
    songs = Songs.objects.all().filter(option=3)
    return render(request, "sadsongs.html", {'songs': songs, 'fname':fname} )


@login_required(login_url = reverse_lazy("index"))
def energeticsongs(request):
    
    current_user = request.user
    fname = current_user.first_name
    songs = Songs.objects.all().filter(option=4)
    return render(request, "energeticsongs.html", {'songs': songs, 'fname':fname} )