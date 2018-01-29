from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.


def index(request):
    user = request.user
    if user.is_authenticated:
        print(user.image_set.all())
        all_images = Image.objects.all()
        return render(request, 'feed.html', context={
            'images': all_images
        })
    else:
        return render(request, 'login.html')


def profile(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return HttpResponse('You have to log in')


def explore(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse('You have reached the explore!')
    else:
        return HttpResponse('You have to log in')
