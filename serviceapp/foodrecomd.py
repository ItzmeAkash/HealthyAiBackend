# import pandas as pd
# import numpy as np
# import joblib

# #Diet Recommendation


# # Load the model
# model = joblib.load('model\model.joblib')

# #load the dataset
# df = pd.read_csv("data\diet_recommendation.csv") 
class FoodRecommendation:

    PHYSICAL_ACTIVITY_FACTORS = {
        "Sedentray": 1.2,
        "LightlyActive": 1.375,
        "ModeratelyActive": 1.725,
        "ExtremelyActive": 1.9
    }

    def __init__(self, age, gender, weight, height, physical_activity, goal):
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.physical_activity = physical_activity
        self.goal = goal  
    
    
    # Calculateing calories
    def calories(self):
        factor = self.PHYSICAL_ACTIVITY_FACTORS.get(self.physical_activity, 1.2)

        bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + (5 if self.gender == 'Male' else -161)
        calories = round(bmr * factor)
        
        # Conditions for maintain loss, gain, mainatin weight
        adjustment = 500 if self.goal == 'WeightGain' else (-500 if self.goal == 'WeightLoss' else 0)
        calories += adjustment
        
        # return the calories for each meals
        meal_portions = {
            'breakfast': int(0.30 * calories),
            'lunch': int(0.25 * calories),
            'snacks': int(0.15 * calories),
            'dinner': int(0.27 * calories)
        }

        return meal_portions
    
    # def prediction(self):
    #     breakfast = np.array(meal_portions['breakfast']).reshape(-1,1)
    #     lunch = np.array(meal_portions['lunch']).reshape(-1,1)
    #     snacks = np.array(meal_portions['snacks']).reshape(-1,1)
    #     dinner = np.array(meal_portions['dinner']).reshape(-1,1)
    #     breakfast = model.predict(breakfast)[0]
    #     lunch = model.predict(lunch)[0]
    #     snacks = model.predict(snacks)[0]
    #     dinner = model.predict(dinner)[0]              
    #     return breakfast,lunch,dinner,snacks
    
    
    

# obj = FoodRecommendation(25, "Male", 55, 150, "ExtremelyActive", "loss")
# meal_portions = obj.calories()
# print(meal_portions)
# predict = obj.prediction()
# print(predict)
# df['cluster'] = model.labels_
# df.to_csv('data.csv', index=False)
# breakfast_df =df.loc[(df['Breakfast'] == 1) & (df['cluster'] == predict[0]), ['food_items', 'Calories']]
# lunch_df =df.loc[(df['Breakfast'] == 1) & (df['cluster'] == predict[1]), ['food_items', 'Calories']]
# snacks_df =df.loc[(df['Breakfast'] == 1) & (df['cluster'] == predict[2]), ['food_items', 'Calories']]
# dinner_df =df.loc[(df['Breakfast'] == 1) & (df['cluster'] == predict[3]), ['food_items', 'Calories']]


# print("breakfast is",breakfast_df.head())
# print('lunch is',lunch_df.head())
# print('snack is',snacks_df.head())
# print(dinner_df.head())
