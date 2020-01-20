"""Users URL's"""

# Django
from django.urls import path

# Views
from cride.circles.views import UserLoginAPIView, create_circle

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
]