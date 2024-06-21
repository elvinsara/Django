from django.shortcuts import render

# Create your views here.

def view_movies(request):
    return render(request,'viewmovies.html')

def create_movies(request):
    return render(request,'createmovies.html')

def update_movies(request):
    return render(request,'updatemovies.html')