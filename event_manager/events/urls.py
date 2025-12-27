from django.urls import path
from .views import UserCreate, EventListCreate, EventDetail

urlpatterns = [
    # User Registration
    path('register/', UserCreate.as_view(), name='user-register'),
    
    # List all events or Create a new one
    path('events/', EventListCreate.as_view(), name='event-list-create'),
    
    # Retrieve, Update, or Delete a specific event by ID
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
]