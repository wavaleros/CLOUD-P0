import uuid

from django.db import models

# Create your models here.
from users.models import User


# from django.utils.translation import gettext as _


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    event_name = models.CharField(max_length=100, null=False, blank=False)

    class EventCategories(models.TextChoices):
        CONFERENCE = ('CONFERENCE', 'CONFERENCE')
        SEMINAR = ('SEMINAR', 'SEMINAR')
        CONGRESS = ('CONGRESS', 'CONGRESS')
        COURSE = ('COURSE', 'COURSE')

    event_category = models.CharField(max_length=50, choices=EventCategories.choices,
                                      default=EventCategories.CONFERENCE)
    event_place = models.CharField(max_length=100, null=False, blank=False)
    event_address = models.CharField(max_length=100, null=False, blank=False)
    event_initial_date = models.DateTimeField()
    event_final_date = models.DateTimeField()

    class EventType(models.TextChoices):
        VIRTUAL = ('VIRTUAL', 'VIRTUAL')
        PRESENCIAL = ('PRESENCIAL', 'PRESENCIAL')

    event_type = models.CharField(max_length=30, choices=EventType.choices)
    thumbnail = models.ImageField(upload_to='thumbnail', null=True)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
