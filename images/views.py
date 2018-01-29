from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from django.shortcuts import redirect
# Create your views here.


def index(request):
    user = request.user
    if user.is_authenticated:
        all_images = Image.objects.all().order_by('-created_at')
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


def upload(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            location = request.POST.get('location')
            caption = request.POST.get('caption'),
            uploaded_file = request.FILES.get('file')
            Image.objects.create(
                file=uploaded_file,
                location=location,
                caption=caption,
                created_by=user,
            )
            return redirect('/')
        else:
            return HttpResponse('You have to log in')
    else:
        return HttpResponse('Nothing to see here')
