from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, default="Untitled")
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
