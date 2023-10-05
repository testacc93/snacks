from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index),
    path('contact', views.contact),
    path('shop', views.shop),
    path('about', views.about),
    path('export', views.export),
    path('/snacks/<str:snack_name>', views.product),
    path('analyse', views.analyse),




]