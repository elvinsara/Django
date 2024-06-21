from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def print_hello(request):
    movie_details = {
        'movie':[{ 
        'title' : 'ABCD',
        'year' : 2016,
       # 'summary' : 'comic',
        'success' : True
    },
    { 
        'title' : 'ABCD',
        'year' : 2016,
        'summary' : 'comic',
        'success' : True
    }
    ]} 
    return render(request,'index.html',movie_details)
    #return HttpResponse("<b>Hello World</b>")
