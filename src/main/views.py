from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
from django.contrib.auth.decorators import login_required

def main_view(request):
    return render(request, "main.html")
# Create your views here.

@login_required
def home_view(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'home.html', context)

#retrieving the listings in the database and giving them to the html file