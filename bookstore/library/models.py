from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Author(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    birthdate=models.DateField()
    def __str__(self):
        return self.first_name +" " + self.last_name



class Genre(models.Model):
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('MYST', 'Mystery'),
        ('SCI', 'Science'),
        ('BIO', 'Biography'),
        ('FANT', 'Fantasy'),
        ('ROM', 'Romance'),
    ]

    name = models.CharField(max_length=5, choices=GENRE_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        default=3
    )
    def __str__(self):
        return self.title

    @classmethod
    def total_books(cls):
        return cls.objects.count()

