from django.urls import path
from .views import (
        BookListCreateView,
        BookRetrieveUpdateDestroyView
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='books-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='detail-update-destory'),
    path('books/create/',),
    path('books/update/',),
    path('books/<int:pk>/',),
    path('books/<int:pk>/', ),
]

