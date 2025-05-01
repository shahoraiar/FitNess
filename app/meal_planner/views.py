import requests 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
class MealPlanGeneratorView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MealPlanRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        prompt = (
            f"Generate a {data['duration']}-day meal plan for a {data['age']}-year-old {data['gender']} "
            f"who is {data['height']} cm tall, weighs {data['weight']} kg, with a goal of {data['goal']}. "
            f"Activity level is {data['activity_level']} and sleeps {data['sleep_hours_per_night']} hours per night. "
            "Include total daily calories, macronutrient breakdown (protein, carbs, fats), and a brief description of each meal. "
            "Tailor the plan based on energy expenditure and recovery needs."
        )

        headers = {
            "Authorization": "Bearer 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",  
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek/deepseek-r1:free",
            "messages": [
                {"role": "system", "content": "You are a certified nutritionist and fitness meal planner."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            return Response({"meal_plan": result['choices'][0]['message']['content']})
        else:
            return Response({
                "error": "Failed to generate meal plan.",
                "details": response.text
            }, status=response.status_code)


