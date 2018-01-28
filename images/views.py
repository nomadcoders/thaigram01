from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'base.html', context={
            'title': 'Feed',
            'message': f'Welcome back {user.username}'
        })
    else:
        return render(request, 'base.html', context={
            'title': 'Log In',
            'message': 'Please log in'
        })


def profile(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse('You have reached the profile!')
    else:
        return HttpResponse('You have to log in')


def explore(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse('You have reached the explore!')
    else:
        return HttpResponse('You have to log in')
