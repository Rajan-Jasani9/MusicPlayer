from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('', views.register, name = "index"),
    path('signout', views.signout, name = "signout"),
    path('login', views.loggin, name = "login"),
    path('signup', views.createUser, name = "signup"),
    path('signin', views.signin, name = "signin"),
    path('moodSelect/', include("MusicRec.urls")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
