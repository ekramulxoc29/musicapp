from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
    albumm = Album.objects.all()
    context= dict( albumm=albumm )

    return render(request,'music/index.html',context)



def detail(request, album_Name_id):
    try:
        alb=Album.objects.get(id=album_Name_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exit")

    return render(request,'music/detail.html',{'alb':alb})
