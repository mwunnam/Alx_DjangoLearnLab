from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
    # Create user and authenticate
        self.user = User.objects.create_user(username='testuser', password="password123")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.author = Author.objects.create(name="John Doe")

        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2020
        )

        # Endpoints
        self.list_url = reverse("list-view")
        self.detail_url = reverse("detail-view", args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data[0])


    def test_update_book(self):
        data = {"title": "Updated Book", "author": "John Doe", "publication_year": 2021}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")


    # Test for Deleting Book
    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)


    # Test for Searching
    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


    # Test for Ordering
    def test_order_books(self):
        Book.objects.create(title="A BOOK", author="Alice", publication_year=2020) 
        response = self.client.get(self.list_url, {"ordering": "title"})
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))

