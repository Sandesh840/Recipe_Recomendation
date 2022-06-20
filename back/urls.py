from django.contrib import admin
from django.urls import path
from back import views
from django.contrib.auth import views as auth_views
from back.views import signup,login
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('recipes', views.recipes),
    path('recipe/<str:id>', views.recipe),
    path('tags', views.tags),
    path('template/<str:id>', views.template),
    path('signup', signup.as_view()),
    path('login', login.as_view()),
    path('home', views.home),
    path('logout', views.logout),
    path('search', views.search),
]
