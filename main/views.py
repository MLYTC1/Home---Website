from django.shortcuts import render
from django.http import HttpResponse

def index(request) -> HttpResponse:
    context = {
        'title': 'Home',
        'content': 'main store page',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }
    
    return render(request,'main/index.html', context)

def about(request) -> HttpResponse:
    return HttpResponse('About page')