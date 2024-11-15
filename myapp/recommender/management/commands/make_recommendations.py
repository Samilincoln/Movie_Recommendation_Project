from django.core.management import BaseCommand
from ...models import Movie

def check_valid_genres(genres: str) -> bool:
    if bool(genres and not genres.isspace()) and genres != 'na':
        return True
    else:
        return False
    
def jaccard_similarity(list1: list, list2 : list) -> float:
    s1 = set(list1)
    s2 = set(list2)

    return float(len(s1.intersection(s2)) / len(s1.union(s2)))


def similarity_between_movies(movie1: Movie, movie2: Movie):
    if check_valid_genres(movie1.genres) and check_valid_genres(movie2.genres):
        m1_genres = movie1.genres.split()
        m2_genres = movie2.genres.split()
        return jaccard_similarity(m1_genres, m2_genres)
    else:
        return 0
    
class Command(BaseCommand):
    help = "Recommend Movies"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        THRESHOLD = 0.8

        watched_movies = Movie.objects.filter(
            watched= True
        )
        unwatched_movies = Movie.objects.filter(
            watched = False
        )

        for unwatched_movie in unwatched_movies:
            max_similarity = 0
            will_recommend = False

            for watched_movie in watched_movies:
                similarity = similarity_between_movies(unwatched_movies,watched_movies)
                if similarity >= max_similarity:
                    max_similarity = similarity
                if max_similarity >= THRESHOLD:
                    break
        if max_similarity > THRESHOLD:
            will_recommend = True
            print(f"Find a movie recommendation: {unwatched_movie.original_title}")
            break

        unwatched_movie.recommended = will_recommend
        unwatched_movie.save()