from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    year=models.IntegerField()
    #add img feild
    img=models.ImageField(upload_to='gallery')
    def __str__(self):
        return self.name