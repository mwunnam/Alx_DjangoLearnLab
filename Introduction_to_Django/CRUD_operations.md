## Command for creating book
`Book.objects.create(title="1984", author="George Orwell", publication_year=1949)`

## Expected output
`<Book: Book object (1)>`

## Command to retrieve all attributes 
`book = Book.objects.get(id=1)
book.title ="Nineteen Eighty-Four"
book.save()`

## Update
`book = Book.objects.get(id=1)
book.title ="Nineteen Eighty-Four"
book.save()
`
## Expected output


## Command to delete book
`book = Book.objects.get(id=1)
book.delete()`

## Epected output
`(1, {'bookshelf.Book': 1})`

