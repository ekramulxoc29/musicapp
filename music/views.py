from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    albumm = Album.objects.all()
    html=''

    for alb in albumm:
        url= '/music/' + str(alb.id)

        html +='<a href="'+url+' ">' + alb.shilpi+' </a><br>'



    return HttpResponse(html)


def detail(request, album_Name_id):
    return HttpResponse( "<h2>album id:" + str( album_Name_id ) + " </h2>" )
