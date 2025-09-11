from django.urls import path
from .views import RegistrationView, CookieTokenObtainPairView, CookieTokenRefreshView
from . import views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', RegistrationView.as_view(), name="registration"),

    path('hello/', views.HelloWorldView.as_view(), name='hello')
]
