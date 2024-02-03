
# For classed based Views
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Entry, EntryEmbedding
from .serializers import EntrySerializer
from .permissions import IsAuthorOrReadOnly

# For function based views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .customs.vectors import create_vector_from_content
from pgvector.django import L2Distance

from .models import EntryEmbedding

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



# class GetEntriesFromVector()
    

    


@api_view(['POST'])
def GetEntriesFromVector(request):
    if request.method == 'POST':
        text = request.data.get('text', '')

        if not text:
            return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)

        embedding = create_vector_from_content(text)

        # Filter EntryEmbedding queryset based on the author of the entry
        user_entries = Entry.objects.filter(author=request.user)

        # Get the primary keys of matching EntryEmbedding instances
        matching_entry_ids = EntryEmbedding.objects.filter(entry__in=user_entries).order_by(L2Distance('embedding', embedding))[:5].values_list('entry__id', flat=True)

        # Retrieve the corresponding Entry instances
        matching_entries = Entry.objects.filter(pk__in=matching_entry_ids)

        # Serialize the matching entries or perform any other operations you need
        serializer = EntrySerializer(matching_entries, many=True)

        return Response({'entries': serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
def echo_text(request):
    if request.method == 'POST':
        text = request.data.get('text', '')
        return Response({'text': text}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)