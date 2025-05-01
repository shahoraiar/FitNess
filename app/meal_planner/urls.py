from django.urls import path
from .views import MealPlanGeneratorView

urlpatterns = [
    path('generate/', MealPlanGeneratorView.as_view(), name='generate-meal-plan'),
]