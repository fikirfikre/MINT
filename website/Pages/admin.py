from django.contrib import admin
from .models import News,Services

# Register your models here.
@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['preview']
    list_display=['title','slug','publish','status','image']
    list_filter =['status','created','publish']
    search_fields =['title','body']
    prepopulated_fields ={'slug':('title',)}
    date_hierarchy = 'publish'
    ordering = ['status','publish']


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ['preview']
    list_display=['title','slug','publish','image']
    search_fields = ['title','body']
    prepopulated_fields ={'slug':('title',)}
    date_hierarchy = 'publish'  