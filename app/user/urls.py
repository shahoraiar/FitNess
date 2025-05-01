# from django.urls import path
# from .views import RegisterView
from django.urls import path
from .views import RegisterView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),               # POST
    path('login/', TokenObtainPairView.as_view()),           # POST: returns token
    path('token/refresh/', TokenRefreshView.as_view()),      # POST: refresh token
    path('profile/', UserProfileView.as_view()),             # GET: needs JWT token
]