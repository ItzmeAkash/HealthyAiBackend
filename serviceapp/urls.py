from django.urls import path
from .views import DietRecommendationView,FoodClassificationView,FoodRecipeGeneratorView

urlpatterns = [
    path('dietrecommendation/',DietRecommendationView.as_view(),name='dietrecommendation'),
    path('foodimageclassification/',FoodClassificationView.as_view(),name='foodimageclassification'),
    path('foodrecipegenerator/',FoodRecipeGeneratorView.as_view(),name='foodrecipegenerator'),
]