from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
    now = datetime.now()
    
    return render(
        request,
        "DjangoApp/index.html",
        
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X")
        }
        
    )

def about(request):
    return render(
        request,
        "Djangoapp/about.html",
        {
            'title' : "About DjangoApp",
            'content' : "Example app page for Django."
        }  
    )


