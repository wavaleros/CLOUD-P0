from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from users import views

app_name = 'users'

urlpatterns = [
    path('api/create-user/', views.UserCreateView.as_view(), name='create_user'),
    # path('api/api-auth/', views.UserLogin.as_view(), name='get_token'),
    path('api/api-auth/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/api-auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
