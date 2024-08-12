from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register/',views.UserRegistrationApiView.as_view(),name='user_registration'),
    path('login/',views.UserLoginApiView.as_view(),name='user_login'),
    path('showProfile/<int:pk>/',views.ShowProfile.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]