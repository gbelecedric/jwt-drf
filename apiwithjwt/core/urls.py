from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here for tokenauth

from rest_framework_simplejwt import views as jwt_views  #  for jwt
from core.views import *

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here tokenauth


    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]