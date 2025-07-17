Command
book = Book.objects.get(id=1)
book.delete()

Epected output
(1, {'bookshelf.Book': 1})

