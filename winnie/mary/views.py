from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse,HttpResponseRedirect



# Create your views here.
# def index (request):
#     p_title = "Django Templating Language" 
#     author = 'Winnie Among'
#     yob = 2003
#     current_year = 2023
#     age = current_year-yob
#     return render(request,'index.html',{'p_title':p_title,'author':author,'yob':yob,'current_year':current_year,'age':age})

def index (request):
    if request.method == 'POST':
        # continents = ['Africa','/n','Asia','/n','North America']
        continent = request.POST['continent']
       
        return render(request,'index.html',{'continent':continent})
    else:
        # continent = ['Africa','/n','Asia','/n','North America']
        return render(request,'index.html')
        
    # continents = ['Africa','/n','Asia','/n','North America']
    # return render(request,'index.html',{'continent':continent})
    # p_title = "Django Templating Language" 
    # author = 'winnie Among'
    # yob = 2003
    # current_year = 2023
    # African = 'African'
    # Asian = 'Asian'
    # #context = [p_title,author,yob,current_year]
    # return render(request,'index.html')

def data_collect(request):
    if request.method == 'POST':
        print('POSTED')
        name = request.POST['username']
        age = request.POST['age']
        phone = request.POST['phone']
        context = [name,age,phone]
        print(context)
        return render(request,'loop.html',{'context':context})
    
    return render(request,'data_collect.html')
    

def loop (request):
    p_title = "Django Templating Language" 
    author = 'winnie Among'
    yob = 2003
    current_year = 2023
    African = 'True'
    Asian = True
    #context = [p_title,author,yob,current_year]
    return render(request,'loop.html',{'African':African})


        
