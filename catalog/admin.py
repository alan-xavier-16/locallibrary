from django.contrib import admin
from .models import Author, Book, Genre, BookInstance


class AuthorAdmin(admin.ModelAdmin):
    """Model representing an admin class"""
    list_display = ("last_name", "first_name",
                    "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Model representing an admin class"""
    list_display = ("title", "author", "display_genre")

    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Model representing an admin class"""
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ("status", "due_back")

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
