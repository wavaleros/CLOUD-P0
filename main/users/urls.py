from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('api/create-user/', views.UserCreateView.as_view(), name='create_user'),
    path('api/api-auth/', views.UserLogin.as_view(), name='get_token')
]
