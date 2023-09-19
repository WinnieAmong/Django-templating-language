from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index1'),
    path('data_collect/',views.data_collect,name='data_collect'),
    path('loop/',views.loop,name='loop'),
    
    

]
#creat your views here.
