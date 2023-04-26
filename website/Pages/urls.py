from django.urls import path
from . import views



app_name = 'pages'

urlpatterns = [
     path('news-list/',views.news_list,name='news_list'),
     path('<int:id>/',views.news_detail,name ='news_detail'),
     path('services/',views.services_list,name='services_list')
]

