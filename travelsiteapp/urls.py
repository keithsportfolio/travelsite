from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index),
    path('signup', views.signup),
    path('register', views.register),
    path('home', views.dashboard),
    path('login', views.login),
    path('signin', views.signIn),
    path('new_trip/', views.tripAdd),
    path('createTrip/', views.createTrip),
    path('logout', views.logout),
    path('continents', views.continentsPage),
    path('go_to_continents', views.showTripByContinent)
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 