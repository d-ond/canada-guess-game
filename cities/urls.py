# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # The main index page
    path('check-guess/', views.check_guess, name='check_guess'),  # The check_guess endpoint
]
