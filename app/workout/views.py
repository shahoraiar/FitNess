from rest_framework import viewsets, permissions
from .models import Workout
from .serializers import WorkoutSerializer
from app.user.permissions import IsAdminUserType  # You already created this
from rest_framework.response import Response
from rest_framework import status

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserType]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(uploaded_by=request.user)

        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'Workout created successfully',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )
