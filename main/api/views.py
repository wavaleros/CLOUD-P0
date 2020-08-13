# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers
from api.models import Event


class test(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'pong'}
        return Response(content, status=status.HTTP_200_OK)


class EventsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        events = Event.objects.filter(user=request.user)
        serializer = serializers.EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventsDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, event_id):
        event = Event.objects.filter(pk=event_id).first()
        if event:
            serializer = serializers.EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, event_id):
        event = Event.objects.filter(pk=event_id).first()
        if event:
            event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, event_id):
        event = Event.objects.filter(pk=event_id).first()
        serializer = serializers.EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
