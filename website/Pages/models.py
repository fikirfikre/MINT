from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.utils.html import mark_safe

# Create your models here.

class NewsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.PUBLISHED)


class News(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF","Draft"
        PUBLISHED = 'PB',"Published"

    title = models.CharField(max_length= 250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.FileField(
        upload_to='news_images/', validators=[FileExtensionValidator(['svg', 'jpeg', 'png', 'jpg'])])
    publish = models.DateTimeField(default= timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 2,choices=Status.choices,default=Status.DRAFT)
    objects = models.Manager()
    published = NewsManager()

    class Meta:
        ordering = ["-publish"]
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    def preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')



class Services(models.Model):
    title = models.CharField( max_length=250)
    slug = models.SlugField(max_length =250)
    body = models.TextField()
    image = models.FileField(
        upload_to='news_images/', validators=[FileExtensionValidator(['svg', 'jpeg', 'png', 'jpg'])])
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated = models.DateTimeField( auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name_plural = "Services"
        ordering =["-publish"]

    def __str__(self):
        return self.title

    def preview(self):
        return mark_safe(f'<img src= "{self.image.url}" width = "300"/>')