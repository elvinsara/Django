from django.urls import path
from . import views
urlpatterns = [
    path('movie/addmovies/',views.create_movies,name='create'),
    path('movie/getmovies/',views.view_movies,name='view'),
    path('movie/updatemovies/',views.update_movies,name='update')
]