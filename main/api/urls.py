from django.urls import path

from api import views

app_name = 'api'
# add url path to the API

urlpatterns = [
    path('ping', views.test.as_view(), name='test'),
    path('api/events', views.EventsView.as_view(), name='get_events'),
    path('api/events/<str:event_id>', views.EventsDetailView.as_view(), name='get_events'),
]
