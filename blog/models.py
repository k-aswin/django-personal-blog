from django.db import models
from django.utils import timezone

# Create your models here.

class BlogPost(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    blog_content=models.TextField()
    blog_image=models.ImageField(upload_to='blog/images/')

    def __str__(self):
        return self.title
