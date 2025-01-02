from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def index(request) -> HttpResponse:
    
    categories = Categories.objects.all()
    
    context = {
        'title': 'Home - Main',
        'content': "HOME Furniture Store",
        'categories': categories
    }
    
    return render(request,'main/index.html', context)

def about(request) -> HttpResponse:
    context = {
        'title': 'Home - About us',
        'content': "About us",
        'text_on_page': "Transform your home with stylish, high-quality furniture designed for comfort and elegance.",
    }
    
    return render(request,'main/about.html', context)