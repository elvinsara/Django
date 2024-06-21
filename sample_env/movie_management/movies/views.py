from django.shortcuts import render
from . models import MovieInfo

# Create your views here.

def view_movies(request):
    #returns query set
    movie_set = MovieInfo.objects.all
    return render(request,'viewmovies.html',{'movie':movie_set})

def create_movies(request):
    if request.POST:
        name = request.POST.get('name')
        year = request.POST.get('year')
        summary = request.POST.get('summary')
        print("--------------------------------------------------")
        print(name,year,summary)
        movie_obj = MovieInfo(name=name,year=year,summary=summary)
        movie_obj.save()
    return render(request,'createmovies.html')

def update_movies(request):
    return render(request,'updatemovies.html')