from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import AddPostForm
from .models import *


def mainpage(request):
    posts = AddPost.objects.all().order_by('-id')

    setting = {
        'posts': posts,
        'title': 'Main Page | SocialMedia'  
    }
    return render(request, 'MainLogic/mainpage.html', context=setting)


def addpost(request):
    form = AddPostForm()
    error = ''
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'Щось пішло не так'

    else:
        form = AddPostForm()     
            

    


    setting = {
        'title': 'Add Post | SocialMedia',
        'form': form,
        'error': error,
    }
    return render(request, 'MainLogic/addpost.html', context=setting)

