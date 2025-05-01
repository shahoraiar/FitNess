# from django.urls import path
# from .views import RegisterView
from django.urls import path
from .views import RegisterView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),              
    path('login/', TokenObtainPairView.as_view()),        
    path('token/refresh/', TokenRefreshView.as_view()),     
    path('profile/', UserProfileView.as_view()),             
]