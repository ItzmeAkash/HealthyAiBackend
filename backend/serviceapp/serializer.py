from rest_framework import serializers
from .models import (DietRecommendation,
                     FoodImageModel,
                     RecipeModel)

# Diet Recommendation Serializer
class DietRecomSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietRecommendation
        fields = ( '__all__' )
        
    
    # Validation Check for Age 
    def validate_age(self,age):
        """
        
        Check that the age is greater than 18
        """
        if age <18:
            raise serializers.ValidationError("Age must be greater or equal to 18")
        return age


class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImageModel
        fields = ('__all__')
       

# Recipe Generator 
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeModel
        fields = ('__all__')
        
        
