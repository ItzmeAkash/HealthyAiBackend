from django.contrib import admin
from .models import DietRecommendation,FoodImageModel,RecipeModel
# Register your models here.
admin.site.register(DietRecommendation)
admin.site.register(FoodImageModel)
admin.site.register(RecipeModel)

