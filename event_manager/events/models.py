from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    # Link to the user who created the event (Organizer)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    
    # Capacity management
    capacity = models.PositiveIntegerField()
    
    # Auto-add the date when the object is created
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_and_time'] # Default ordering: newest events first

    def __str__(self):
        return f"{self.title} by {self.organizer.username}"

    # Helper method to check if event is full (for later use)
    @property
    def is_full(self):
        return False