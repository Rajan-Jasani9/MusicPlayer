from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    mood = (
        (1, 'Happy'),
        (2, 'Relaxing'),
        (3, 'Sad'),
        (4, 'Energetic'),
    )
    option = models.IntegerField(choices=mood)
    filepath = models.CharField(max_length=600, null = True)
    
    def __str__(self):
        return self.title         