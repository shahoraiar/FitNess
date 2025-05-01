from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings

class Workout(models.Model):
    DIFFICULTY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    GOALS = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('flexibility', 'Flexibility'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    goal = models.CharField(max_length=20, choices=GOALS)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS)
    video = CloudinaryField(resource_type='video')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


