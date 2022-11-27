from django.urls import path
from .views import main_view, home_view # importing the view from the views.py

urlpatterns = [
    path('', main_view, name='main'),
    path('home/', home_view, name='home')
]