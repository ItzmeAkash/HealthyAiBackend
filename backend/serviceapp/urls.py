from django.urls import path
from .views import DietRecommendationView,FoodClassificationView

urlpatterns = [
    path('dietrecommendation/',DietRecommendationView.as_view(),name='dietrecommendation'),
    path('foodimageclassification/',FoodClassificationView.as_view(),name='foodimageclassification'),
]