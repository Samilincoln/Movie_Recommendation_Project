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


"""def rating_view(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(watched=False).order_by('-rating'[:30])
        context = {'movie_list': movies}

        return render (request, 'recommender/by_rating.html')"""



def rating_view(request):
    # Check if the request is to show only recommended movies
    show_recommended = request.GET.get('recommended', 'false').lower() == 'true'
    
    if show_recommended:
        # Fetch recommended movies sorted by rating
        movies = Movie.objects.filter(watched=False, recommended=True).order_by('-vote_average')[:30]
    else:
        # Fetch all unwatched movies sorted by rating
        movies = Movie.objects.filter(watched=False).order_by('-vote_average')[:30]
    
    context = {'movie_list': movies, 'show_recommended': show_recommended}
    return render(request, 'recommender/rating.html', context)

    
