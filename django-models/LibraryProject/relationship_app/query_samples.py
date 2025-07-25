from .models import Author, Book, Library, Librarian

# 1. Querry all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Books.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"No author found with name '{author_name}'"

# 2. List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return f"No library found with name '{library}'"

# 3. Retrieve the librarian for a llibrary
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return libarian
    except

