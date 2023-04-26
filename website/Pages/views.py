from django.shortcuts import render,get_object_or_404
from .models import News,Services

# Create your views here.


#creating news list

def news_list(request):
    news = News.published.all()
    return render(request, 'news/list.html',{'news':news})


def news_detail(request,id):
     news = get_object_or_404(News,id=id,status=News.Status.PUBLISHED)
     return render(request, 'news/detail.html',{'news':news})
 

def services_list(request):
    services = Services.objects.all()
    return render(request,'services/list.html',{'services':services})