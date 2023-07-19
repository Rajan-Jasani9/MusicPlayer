from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.moodSelect, name = "home"),
    path('<str:fname>/', views.moodSelect, name='mood_select'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),  
    path('happysongs', views.happysongs, name='happysongs'),
    path('relaxingsongs', views.relaxingsongs, name='happysongs'),
    path('sadsongs', views.sadsongs, name='happysongs'),
    path('energeticsongs', views.energeticsongs, name='happysongs'),
    path('<str:fname>', views.moodSelect, name='moodSelect'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
