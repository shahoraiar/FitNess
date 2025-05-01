from rest_framework import serializers

class MealPlanRequestSerializer(serializers.Serializer):
    goal = serializers.ChoiceField(choices=["weight_loss", "muscle_gain", "balanced"])
    duration = serializers.ChoiceField(choices=["daily", "weekly"])
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    height = serializers.FloatField()
    gender = serializers.ChoiceField(choices=["male", "female", "other"])
    activity_level = serializers.ChoiceField(choices=["sedentary", "moderate", "active"])
    sleep_hours_per_night = serializers.FloatField()

