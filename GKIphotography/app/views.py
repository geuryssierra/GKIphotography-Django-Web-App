"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app import models

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    contact = models.ContactUs.objects.all()
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact Us',
            'message':'Our contact information:',
            'year':datetime.now().year,
            'contact': contact
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    Description = models.AboutUs.objects.all()
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'Description': Description
            
        }
    )

def portfolio(request):
    """Renders the Portfolio page."""
    assert isinstance(request, HttpRequest)

    category = request.GET.get('category')
    if category == None:
        Images = models.Photo.objects.all()
    else :
        Images = models.Photo.objects.filter(category__name__contains=category)

    
    Categories = models.Category.objects.all()
    return render(
        request,
        'app/Portfolio.html',
        {
            'title':'Portfolio',
            'message':'Here i will add my photo collections.',
            'year':datetime.now().year,
            'Images': Images,
            'Categories' : Categories
        }
    )

def Drone(request):
    """Renders the Portfolio page."""
    assert isinstance(request, HttpRequest)
    Videos= models.Video.objects.all()
    return render(
        request,
        'app/Videos.html',
        {
            'title':'Drone Videos',
            'message':'Drone videos coming soon...',
            'year':datetime.now().year,
            'Videos': Videos
        }
    )

