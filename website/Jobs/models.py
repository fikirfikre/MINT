from django.db import models
from django.utils import timezone

# Create your models here.
class JobsManager(models.Manager):
    def get_queryset(self):
       return super().get_queryset().filter(status = Jobs.Status.PUBLISHED)
 


class Jobs(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF","Draft"
        PUBLISHED = "PB","Published"

    title =models.CharField(max_length=255)
    slug = models.SlugField(max_length = 255)
    body = models.TextField()
    responsibilities = models.TextField()
    requirement=models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 2,choices=Status.choices,default=Status.DRAFT)
    objects = models.Manager()
    published = JobsManager()



    

    class Meta:
        verbose_name = ("job")
        verbose_name_plural = ("Jobs")
        ordering =["-publish"]

    def __str__(self):
        return self.title

class JobPost(models.Model):
    job =models.ForeignKey(Jobs, verbose_name="job", on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number=models.CharField(max_length=25)   
    file = models.FileField(upload_to = "Cv")

    class Meta:
        verbose_name = 'job Cv'