from rest_framework import permissions, generics, filters
from rest_framework import generics 
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer
from .models import Book

# Book List View
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'published_date'] # Sort by published date
    ordering = ['title']
    permission_classes = [IsAuthenticatedOrReadOnly]



# Detail View
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



# Update View
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        title = self.request.data.get('title', '').strip()
        if Book.objects.filter(title_iexact=title).exclude(pk=self.get_object().pk).exists():
            raise serializers.ValidationError({"title": "A book with this title already exist"})

        """
        if book.owner != self.request.user:
            raise serializers.ValidationError({
                "permission": "You do not have permission to update this book."
            })
        """
        serializer.save()



# Create View
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        title = self.request.data.get('title', '').strip()
        if Book.objects.filter(title_iexact=title).exists():
            raise serializers.ValidationError({"title": "A Book with title already exist"})

        serializer.save()

# DeleteView
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


