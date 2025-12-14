from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        # Ensure the password is required for registration, 
        # but is never sent back in the response (write_only).
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # We override the create method to use create_user
        # This automatically hashes the password.
        user = User.objects.create_user(**validated_data)
        return user
    
class EventSerializer(serializers.ModelSerializer):
    # We display the organizer's username instead of just their ID for better readability
    organizer = serializers.ReadOnlyField(source='organizer.username')

    class Meta:
        model = Event
        fields = ['id', 'organizer', 'title', 'description', 
                  'date_and_time', 'location', 'capacity', 'created_date']
        
        # 'organizer' and 'created_date' should not be editable by the user
        read_only_fields = ['organizer', 'created_date']

    # VALIDATION: Check for past dates
    def validate_date_and_time(self, value):
        # Check that the event date is not in the past.

        if value < timezone.now():
            raise serializers.ValidationError("Event date cannot be in the past!")
        return value