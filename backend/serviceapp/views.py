from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializer import DietRecomSerializer, FoodImageSerializer
from .foodrecomd import FoodRecommendation
from .models import FoodImageModel
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import joblib
import numpy as np
import pandas as pd
import re
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# loading all the enivroment variables and configure the api

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# Load ML models during Django app initialization
diet_model = joblib.load('serviceapp/PredictedModel/model.joblib')
# food_image_model = load_model('serviceapp/PredictedModel/foodimagemodel.h5')

# Food Diet Recommendation
class DietRecommendationView(APIView):
    def post(self, request):
        try:
            # Load the Dataset
            df = pd.read_csv('serviceapp/data/data.csv')
            
            # Process request data with serializer
            serializer = DietRecomSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            filtered_data = serializer.validated_data.copy()
            filtered_data.pop('id', None)
            filtered_data.pop('user', None)
            
            # Calculate calories
            obj = FoodRecommendation(**filtered_data)
            calories = obj.calories()
            
            # Predict calories for each meal and fetch recommended food items
            recommended_food_items = {}
            for meal in ['breakfast', 'lunch', 'snacks', 'dinner']:
                meal_calories = calories[meal]
                meal_prediction = diet_model.predict(np.array(meal_calories).reshape(-1, 1))
                meal_df = df.loc[(df[meal.capitalize()] == 1) & (df['cluster'] == meal_prediction[0]), ['food_items', 'Calories']].sort_values(by='Calories').head()
                recommended_food_items[meal] = meal_df.to_dict(orient='records')
                
            return Response({'recommended_food_items': recommended_food_items}, status=status.HTTP_200_OK)
        
        except Exception as e:
            error_messages = str(e)
            required_messages = {}
            for match in re.finditer(r"'(.*?)': \[ErrorDetail\(string='(.*?)', code='(.*?)'\)\]", error_messages):
                field, message = match.group(1), match.group(2)
                if field != 'unknown':  
                    required_messages[field] = message
            return Response({'error_messages': required_messages}, status=status.HTTP_400_BAD_REQUEST)


#Food image Classification
class FoodClassificationView(APIView):
    def post(self, request): 
        serializer = FoodImageSerializer(data=request.data)
        if serializer.is_valid():
            if 'image' in serializer.validated_data:
                uploadedImage = serializer.validated_data['image']
                bytesdata = BytesIO(uploadedImage.read()).read()
                image_parts = [
                    {
                        "mime_type": uploadedImage.content_type,
                        "data": bytesdata
                    }
                ]

                input_prompt = """
                You are an expert in nutitionist where need to see the food items from the image
                and predict which food is that  and  calculate the total calories, also provide the details of every food items with calories intake
                            is below format

                            1. Item 1 - no of calories
                            2. Item 2 - no of calories
                            ----
                            ----
                            
                        Finally you can also mention whether the food is healthy or not and also
                        mention the
                        percentage split of the ratio of carbohydrates,fats,fibers,suger, and other important 
                        things required in our diet
                        
                        if the image if not food give the response like please give us the foods contained images
                """
                
                response = get_gemini_response(input_prompt, image_parts)
                return Response({"response": response})
            else:
                return Response({"error": "Image field is required"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Function for The Gemini Pro vison Intigrations
def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])
    return response.text
