from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , DeleteView, UpdateView 
from django.urls import reverse_lazy, reverse
from django.contrib  import messages

from django.views.decorators.cache import never_cache
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    return render(request, "index.html")

def loggin(request):
    return render(request, "index.html")

def createUser(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['password']
        

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        messages.success(request, "Your Account has been created Successfully!")
        
        return redirect('login')
    
    return render(request, 'Loggin/signup.html')

def signin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password = password)
        if user is None:
            messages.success(request, 'Invalid Credentials')
            return redirect('login')    
            
        if user is not None:
            login(request,user)
            fname = user.first_name
            url = reverse('mood_select', kwargs={'fname': fname})
            print(url)
            print(fname)
            return redirect(url)
        else:
            flag = 1
            messages.error(request, "Bad Credentials")
            return redirect('login')    
    return render(request, 'Loggin/login.html')

def signout(request):
    logout (request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('login')