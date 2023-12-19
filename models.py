from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name= 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
  

class Post(models.Model):  
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField(blank=True, null= True, config_name='portal_config')
    hiking_icon = models.BooleanField(default=False, blank=True)
    accomodation_icon = models.BooleanField(default=False, blank=True)
    camping_icon = models.BooleanField(default=False, blank=True)
    days_icon = models.BooleanField(default=False, blank=True)
    hours_icon = models.BooleanField(default=False, blank=True)
    duration = models.CharField(max_length=5, blank=True, null=True)
    
    header_image = models.ImageField(
         null=True, blank=False, upload_to="images/")

    title_tag = models.CharField(max_length=255, default="Blog post")
    post_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
        #return reverse('article-detail', args=(str(self.id)))

  