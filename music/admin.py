from django.contrib import admin
from .models import Album,Song

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('shilpi','album_Name','Genre','logo','video')
    search_fields = ('shilpi','album_Name','Genre','logo','video')
admin.site.register(Album,AlbumAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display = ('album','Gaan_title')
    search_fields = ('album','Gaan_title')
admin.site.register(Song,SongAdmin)
