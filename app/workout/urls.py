from django.urls import path
from .views import WorkoutViewSet

workout_list = WorkoutViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

workout_detail = WorkoutViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    path('workouts/', workout_list, name='workout-list'),
    path('workouts/<int:pk>/', workout_detail, name='workout-detail'),
]