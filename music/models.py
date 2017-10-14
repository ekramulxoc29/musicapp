from django.db import  models

class Album(models.Model):
    shilpi=models.CharField(max_length=200)
    album_Name = models.CharField(max_length=200)
    Genre= models.CharField(max_length=200)
    logo=models.CharField(max_length=300)
    video=models.CharField(max_length=600,default='')

    def __str__(self):
     return self.shilpi


class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    Gaan_title = models.CharField(max_length=400)
    fav=models.BooleanField(default=False)

    def __str__(self):
     return self.Gaan_title