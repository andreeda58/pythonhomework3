from django.shortcuts import render
from django.views.generic import ListView
from .models import Book ,Genre
from django.db.models import Count

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

# Create your views here.
def books_by_author(request,author_id):
    total = Book.total_books()
    books=Book.objects.filter(authors__id=author_id)
    return render(request,'books_by_author.html',{'books':books,'total_books':total})


def books_by_genre(request, genre_code):
    books = Book.objects.filter(genre__name=genre_code)
    return render(request, 'books_by_genre.html', {'books': books})

def genre_stats(request):
    stats = Genre.objects.annotate(total_books=Count('book'))
    return render(request, 'genre_stats.html', {'stats': stats})