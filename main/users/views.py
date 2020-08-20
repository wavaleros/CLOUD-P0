# Create your views here.
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from users import serializers
from users.models import User
from users.serializers import UserSerializer


class UserCreateView(APIView):
    queryset = User.objects.all()
    serializer = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            user_obj = User.objects.create(
                username=user['username'],
                email=user['email'],
                first_name=user['first_name'],
                last_name=user['last_name'],
            )
            user_obj.set_password(user['password'])
            user_obj.save()
            content = {'content': user, 'message': 'SUCCESS', 'status': 'SUCCESSFUL'}
            return Response(data=content, status=status.HTTP_201_CREATED)
        content = {'content': '', 'message': serializer.errors, 'status': 'FAILURE'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def post(self, request):
        try:
            if request.data is None or len(request.data) < 2:
                content = {'message': 'User or password must be provided', 'status': 'FAILED'}
                return Response(data=content, status=status.HTTP_400_BAD_REQUEST)
            if request.data['username'] is None or request.data['password'] is None:
                content = {'message': 'User or password must be provided', 'status': 'FAILED'}
                return Response(data=content, status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(username=request.data['username'], password=request.data['password'])

            if user is not None:
                token = jwt_encode_handler(jwt_payload_handler(user))
                content = {'content': {'token': token}, 'message': 'SUCCESS', 'status': 'SUCCESSFUL'}
                return Response(data=content, status=status.HTTP_200_OK)
            else:
                content = {'message': 'Invalid credentials', 'status': 'SUCCESSFUL'}
                return Response(data=content, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            content = {'message': 'Internal error', 'status': 'FAILED'}
            print(e)
            return Response(data=content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
