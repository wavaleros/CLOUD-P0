from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users import views

app_name = 'users'

urlpatterns = [
    path('api/create-user', views.UserCreateView.as_view(), name='create_user'),
    path('api/api-auth/', obtain_auth_token, name='get_token')
]
