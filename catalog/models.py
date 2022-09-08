from django.db import models
from django.urls import reverse  # Generate URLs by reversing the patterns
from django.contrib.auth.models import User

import uuid
from datetime import date

# Create your models here.


class Genre(models.Model):
    """Model for book genres"""
    name = models.CharField(
        max_length=200, help_text="Enter a book genre (e.g. Science Fiction)")

    def __str__(self):
        """String for Model object"""
        return self.name


class Book(models.Model):
    """Model for books"""
    title = models.CharField(max_length=200, help_text="Enter a book title")
    # Foreign Key: a book has one author, authors have many books
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description")
    isbn = models.CharField("ISBN", max_length=13, unique=True,
                            help_text="13 Characters <a href='https: // www.isbn-international.org/content/what-isbn'>ISBN number</a>")
    # Many-to-Many: Genre can contain many books, books can have many genres
    genre = models.ManyToManyField(
        Genre, help_text="Select a genre for this book")

    def __str__(self):
        """String for Model object"""
        return self.title

    def get_absolute_url(self):
        """Return URL to access a detail record for this book"""
        return reverse("book-detail", args=[str(self.id)])

    def display_genre(self):
        """Create string for a Genre (used in Admin)"""
        return ", ".join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = "Genre"


class BookInstance(models.Model):
    """Model representing a specific copy of a book (can be borrowed from library)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book in library")
    # Foreign Key: a copy of one book, books have many copies
    book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              blank=True, default="m", help_text="Book availability")
    borrower = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["due_back"]
        permissions = (
            ("can_mark_returned", "Set book as returned"),
            ("can_edit", "Can edit book details"),
        )

    def __str__(self):
        """String representing book object"""
        return f"{self.id}: ({self.book.title})"

    @property
    def is_overdue(self):
        """Determines if the book is overdue based on due date and current date"""
        return bool(self.due_back and date.today() > self.due_back)


class Author(models.Model):
    """Model representing an author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns URL to access a particular author instance"""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing author object"""
        return f'{self.last_name}, {self.first_name}'
