
from django.shortcuts import render,get_object_or_404
from .models import Album


def index(request):
    albumm = Album.objects.all()
    context= dict( albumm=albumm )

    return render(request,'music/index.html',context)



def detail(request, album_Name_id):
    alb=get_object_or_404(Album,pk=album_Name_id)

    return render(request,'music/detail.html',{'alb':alb})
