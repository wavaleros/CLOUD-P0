# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers
from api.models import Event


class ping(APIView):
    def get(self, request):
        content = {'message': 'pong'}
        return Response(content, status=status.HTTP_200_OK)


class EventsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        events = Event.objects.filter(user=request.user)
        serializer = serializers.EventSerializer(events, many=True)
        content = {'content': serializer.data, 'message': 'SUCCESS', 'status': 'SUCCESSFUL'}
        return Response(data=content, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            serializer = serializers.EventSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                content = {'content': serializer.data, 'message': 'SUCCESS', 'status': 'SUCCESSFUL'}
                return Response(data=content, status=status.HTTP_201_CREATED)
            content = {'content': '', 'message': serializer.errors, 'status': 'FAILURE'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            content = {'message': 'Internal error', 'status': 'FAILED'}
            print(e)
            return Response(data=content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EventsDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, event_id):
        event = Event.objects.filter(pk=event_id).first()
        if event:
            serializer = serializers.EventSerializer(event)
            content = {'content': serializer.data, 'message': 'SUCCESS', 'status': 'SUCCESSFUL'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'content': '', 'message': 'SUCCESS', 'status': 'SUCCESSFUL'}
            return Response(content, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, event_id):
        event = Event.objects.filter(pk=event_id).first()
        if event:
            event.delete()
        content = {'content': '', 'message': 'SUCCESS', 'status': 'SUCCESSFUL'}
        return Response(content, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, event_id):
        request_user = request.user
        event = Event.objects.filter(pk=event_id).first()
        if request_user.id != event.user.id:
            content = {'content': '', 'message': 'Unauthorized', 'status': 'FAILURE'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        serializer = serializers.EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            content = {'content': serializer.data, 'message': 'SUCCESS', 'status': 'SUCCESSFUL'}
            return Response(content, status=status.HTTP_200_OK)
        content = {'content': '', 'message': serializer.errors, 'status': 'FAILURE'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
