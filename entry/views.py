
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Entry, EntryEmbedding
from .serializers import EntrySerializer
from .permissions import IsAuthorOrReadOnly

class EntryListCreateView(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only the entries of the currently authenticated user
        return Entry.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        # Set the author of the entry before saving it
        serializer.save(author=self.request.user)

class EntryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


