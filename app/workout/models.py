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



# from django.db import models

# # Create your models here.
# class WorkoutVideo(models.Model):
#     CATEGORY_CHOICES = [
#         ('weight_loss', 'Weight Loss'),
#         ('muscle_gain', 'Muscle Gain'),
#         ('beginner', 'Beginner'),
#     ]
#     title = models.CharField(max_length=200)
#     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
#     video = models.FileField(upload_to='videos/')
#     created_at = models.DateTimeField(auto_now_add=True)

# class HealthData(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     weight = models.FloatField()
#     height = models.FloatField()
#     activity_level = models.CharField(max_length=100)
#     sleep_hours = models.FloatField()

# class MealPlan(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField()
#     content = models.TextField()
