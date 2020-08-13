from rest_framework import serializers

from api import models


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ['id', 'event_name', 'event_category', 'event_place', 'event_address', 'event_initial_date',
                  'event_final_date', 'event_type', 'thumbnail']
