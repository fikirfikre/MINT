from django.contrib import admin
from .models import Jobs,JobPost

# Register your models here.
@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display=['title','slug','publish','status']
    prepopulated_fields ={'slug':('title',)}

@admin.register(JobPost)
class JobsPostAdmin(admin.ModelAdmin):
    list_display =["file","name"]
    