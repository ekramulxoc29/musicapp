
from django.shortcuts import render,get_object_or_404
from .models import Album,Song


def index(request):
    albumm = Album.objects.all()
    context= dict( albumm=albumm )

    return render(request,'music/index.html',context)



def detail(request, album_Name_id):
    alb=get_object_or_404(Album,pk=album_Name_id)

    return render(request,'music/detail.html',{'alb':alb})

def favorite(request, album_Name_id):
    alb=get_object_or_404(Album,pk=album_Name_id)
    try:
        selected=alb.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):


     return render(request,'music/detail.html',
                  {'alb':alb,
                   'error_message':"invalid", })
    else:
        selected.fav=True
        selected.save()
        return render( request, 'music/detail.html', {'alb': alb} )

