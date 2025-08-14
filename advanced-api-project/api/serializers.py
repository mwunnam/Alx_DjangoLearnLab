from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        ''' Validation for publication year, the publication year cannot be in the future'''
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publicaton year can to be in the future year")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    author = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']



