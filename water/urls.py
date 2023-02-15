from django.contrib import admin
from django.urls import path
from water import views
urlpatterns = [
   path("", views.home1, name='water'),
   path("register1", views.register1, name='water'),
   path("login1", views.login1, name='water'),
   path("signout", views.signout, name='water'),
   path("book1", views.book1, name='water'),
   path("logout",views.signout, name='water'),
   path("book1op",views.res, name='water'),
]
