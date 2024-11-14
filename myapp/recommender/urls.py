from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_recommendation_view, name= 'recommendations'),
    path("rating", views.rating_view, name= 'view_by_rating')
]
