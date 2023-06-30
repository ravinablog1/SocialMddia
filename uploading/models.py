from django.db import models

# Create your models here.

class Post(models.Model):
    facebook_post=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='\photo',blank=True)

    def __str__(self):
       return self.facebook_post
