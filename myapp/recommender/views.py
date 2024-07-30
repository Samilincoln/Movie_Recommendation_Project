from django.shortcuts import render
from .models import Movie

# Create your views here.
def movie_recommendation_view(request):
    if request.method == "GET":
        context = generate_movies_context()

        return render (request, 'recommender/movie_list.html', context)

def generate_movies_context():
    context = {}

    recommend_count = Movie.objects.filter(recommended=True).count()

    if recommend_count == 0:
        movies =  Movie.objects.filter(
            watched=False
        ).order_by('-vote_count')[:30]
    else:
        movies = Movie.objects.filter(
            watched=False
        ).filter(
            recommended = True
        ).order_by('-vote_count')[:30]
    context['movie_list'] = movies
    return context


def rating_view(request):
    if request.method == 'GET':
        context = {}

        return render (request, 'recommender/by_rating.html')
    
