from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Q
from .models import Event
from .serializers import EventSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

# User Registration View
class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] # Anyone can register

# Event List & Create View
class EventListCreate(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        This view should return a list of all events,
        optionally filtered by title, location, and date.
        """
        queryset = Event.objects.all()
        
        # Filter: View Upcoming Events
        # Usage: /events/?upcoming=true
        upcoming = self.request.query_params.get('upcoming')
        if upcoming is not None and upcoming.lower() == 'true':
            queryset = queryset.filter(date_and_time__gt=timezone.now())

        # Filter: Search by Title or Location
        # Usage: /events/?search=concert
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(location__icontains=search_query)
            )

        return queryset

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the organizer
        serializer.save(organizer=self.request.user)

# Event Detail, Update, Delete View
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # Only the owner can update/delete; others can only read
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]