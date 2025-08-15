from django.urls import path
from .views import (
        ListView,
        CreateView,
        UpdateView,
        DeleteView,
        DetailView,
)

urlpatterns = [
    path('books/create/', CreateView.as_view(), name='create-book'),
    path('books/update/', UpdateView.as_view(), name='update-book'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='delete-book'),
    path('books/', ListView.as_view(), name='list-view'),
    path('books/<int:pk>/', DetailView.as_view(), name='Detail-view'),
]

