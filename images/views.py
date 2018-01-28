from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'feed.html')
    else:
        return render(request, 'login.html')


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
