from django.urls import path
from .views import BookListView\
    ,books_by_genre\
    ,books_by_author\
    ,genre_stats

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('author/<int:author_id>/', books_by_author, name='books_by_author'),
    path('genre/<str:genre_code>/', books_by_genre, name='books_by_genre'),
    path('stats/genres/', genre_stats, name='genre_stats'),
]
