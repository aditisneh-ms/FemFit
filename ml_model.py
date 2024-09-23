# # import joblib
# # from datetime import datetime

# # # Load the saved model and encoders
# # clf = joblib.load('ml_model.pkl')
# # phase_encoder = joblib.load('phase_encoder.pkl')
# # plan_encoder = joblib.load('plan_encoder.pkl')

# # # Phase mapping for calculating phase based on day in the cycle
# # phase_map = {
# #     "menstrual": 0,
# #     "follicular": 1,
# #     "ovulatory": 2,
# #     "luteal": 3
# # }

# # def calculate_phase(menstrual_start_date, cycle_length):
# #     menstrual_start = datetime.strptime(menstrual_start_date, "%Y-%m-%d")
# #     today = datetime.today()
# #     days_since_menstrual = (today - menstrual_start).days % cycle_length
    
# #     if days_since_menstrual < 7:
# #         return "menstrual"
# #     elif days_since_menstrual < 14:
# #         return "follicular"
# #     elif days_since_menstrual < 21:
# #         return "ovulatory"
# #     else:
# #         return "luteal"

# # # def predict_plan(menstrual_start_date, cycle_length):
# # #     phase = calculate_phase(menstrual_start_date, cycle_length)
# # #     phase_encoded = phase_encoder.transform([phase])[0]
# # #     adherence_history = 1  # Example adherence history, can be dynamic
    
# # #     # Predict the plan
# # #     predicted_plan_encoded = clf.predict([[phase_encoded, adherence_history]])[0]
# # #     predicted_plan = plan_encoder.inverse_transform([predicted_plan_encoded])[0]
# # #     return predicted_plan

# # def get_plan_details(plan):
# #     """Return details for the given plan."""
# #     plans_details = {
# #         "light_workout": {
# #             "workout": "Gentle yoga or walking for 30 minutes.",
# #             "diet": "Focus on light meals, including fruits and vegetables."
# #         },
# #         "heavy_workout": {
# #             "workout": "Strength training, 1 hour session.",
# #             "diet": "High-protein meals, including lean meats and legumes."
# #         },
# #         "hiit": {
# #             "workout": "High-intensity interval training for 20 minutes.",
# #             "diet": "Balanced diet with carbs and protein."
# #         },
# #         "moderate_workout": {
# #             "workout": "30-45 minutes of cycling or jogging.",
# #             "diet": "Moderate diet, including grains, protein, and healthy fats."
# #         },
# #         "iron_diet": {
# #             "workout": "Moderate strength training.",
# #             "diet": "Foods rich in iron, like spinach and beans."
# #         },
# #         "protein_diet": {
# #             "workout": "Focus on endurance training.",
# #             "diet": "High-protein meals, including dairy and eggs."
# #         },
# #         "carb_diet": {
# #             "workout": "Light cardio, like brisk walking.",
# #             "diet": "High-carb meals, including pasta and rice."
# #         },
# #         "magnesium_diet": {
# #             "workout": "Relaxing exercises like stretching.",
# #             "diet": "Foods high in magnesium, like nuts and seeds."
# #         },
# #     }
# #     return plans_details.get(plan, {"workout": "No workout details available.", "diet": "No diet details available."})

# # def predict_plan(menstrual_start_date, cycle_length):
# #     phase = calculate_phase(menstrual_start_date, cycle_length)
# #     phase_encoded = phase_encoder.transform([phase])[0]
# #     adherence_history = 1  # Example adherence history, can be dynamic
    
# #     # Predict the plan
# #     predicted_plan_encoded = clf.predict([[phase_encoded, adherence_history]])[0]
# #     predicted_plan = plan_encoder.inverse_transform([predicted_plan_encoded])[0]

# #     # Get detailed plan information
# #     plan_details = get_plan_details(predicted_plan)

# #     return {
# #         "plan_name": predicted_plan,
# #         "workout": plan_details["workout"],
# #         "diet": plan_details["diet"]
# #     }

# import joblib
# from datetime import datetime
# import os

# # Load the saved model and encoders, handle errors if file not found
# def load_model_and_encoders():
#     try:
#         clf = joblib.load('ml_model.pkl')
#         phase_encoder = joblib.load('phase_encoder.pkl')
#         plan_encoder = joblib.load('plan_encoder.pkl')
#         return clf, phase_encoder, plan_encoder
#     except FileNotFoundError as e:
#         print(f"Error loading model or encoder: {e}")
#         return None, None, None

# # Phase mapping for calculating phase based on day in the cycle
# phase_map = {
#     "menstrual": 0,
#     "follicular": 1,
#     "ovulatory": 2,
#     "luteal": 3
# }

# def calculate_phase(menstrual_start_date, cycle_length):
#     try:
#         menstrual_start = datetime.strptime(menstrual_start_date, "%Y-%m-%d")
#     except ValueError:
#         print("Invalid date format. Use YYYY-MM-DD format.")
#         return None
#     today = datetime.today()
#     days_since_menstrual = (today - menstrual_start).days % cycle_length

#     if days_since_menstrual < 7:
#         return "menstrual"
#     elif days_since_menstrual < 14:
#         return "follicular"
#     elif days_since_menstrual < 17:
#         return "ovulatory"
#     else:
#         return "luteal"

# def get_plan_details(plan):
#     """Return detailed plans for workouts and meals, including images."""
#     plans_details = {
#         "light_workout": {
#             "workout": """*Menstrual Phase (Day 1-7)*
#                           - Focus on light exercises like yoga (Hatha yoga) or walking (30-45 minutes).
#                           - Exercises: Child's pose, cat-cow pose, seated forward bend.
#                           - Benefits: Reduces cramps, promotes relaxation and mindfulness.""",
#             "diet": """*Menstrual Phase (Day 1-7)*
#                        - Prioritize iron-rich foods such as spinach, lentils, and beans.
#                        - Include lots of water and fiber-rich foods to ease digestion.
#                        - Example Meal: Spinach and lentil soup with whole grain bread.""",
#             "workout_image": "https://example.com/light_workout_yoga.png",
#             "diet_image": "https://example.com/light_fruits_veggies.png"
#         },
#         "heavy_workout": {
#             "workout": """*Follicular Phase (Day 8-14)*
#                           - High-energy phase: Focus on strength training and HIIT (20-30 minutes).
#                           - Exercises: Squats, deadlifts, lunges, weight lifting.
#                           - Benefits: Boosts muscle growth and fat burning.""",
#             "diet": """*Follicular Phase (Day 8-14)*
#                        - Include lean proteins (chicken, fish), complex carbs (quinoa, sweet potatoes), and healthy fats (avocado).
#                        - Example Meal: Grilled chicken with quinoa salad and avocado.""",
#             "workout_image": "https://example.com/strength_training.png",
#             "diet_image": "https://example.com/high_protein_meals.png"
#         },
#         "hiit": {
#             "workout": """*Ovulatory Phase (Day 15-17)*
#                           - High-intensity cardio phase: Focus on running, cycling, or swimming (45-60 minutes).
#                           - Exercises: Sprint intervals, swimming, long-distance cycling.
#                           - Benefits: Builds endurance and cardiovascular strength.""",
#             "diet": """*Ovulatory Phase (Day 15-17)*
#                        - Focus on hormone-balancing foods like leafy greens, seeds (flax, chia), and whole grains.
#                        - Example Meal: Green smoothie with spinach, chia seeds, and almond milk.""",
#             "workout_image": "https://example.com/hiit_workout.png",
#             "diet_image": "https://example.com/balanced_meal.png"
#         },
#         "moderate_workout": {
#             "workout": """*Luteal Phase (Day 18-28)*
#                           - Switch to moderate exercises like brisk walking or Pilates (30-45 minutes).
#                           - Exercises: Brisk walking, Pilates stretches, light cardio.
#                           - Benefits: Reduces PMS symptoms and helps maintain energy levels.""",
#             "diet": """*Luteal Phase (Day 18-28)*
#                        - Focus on complex carbs (whole grains), fruits, and leafy greens.
#                        - Include magnesium-rich foods like nuts and seeds to reduce bloating.
#                        - Example Meal: Brown rice with sautéed vegetables and almonds.""",
#             "workout_image": "https://example.com/cycling_jogging.png",
#             "diet_image": "https://example.com/moderate_diet.png"
#         }
#     }
#     return plans_details.get(plan, {
#         "workout": "No workout details available.",
#         "diet": "No diet details available.",
#         "workout_image": "https://example.com/default_workout.png",
#         "diet_image": "https://example.com/default_diet.png"
#     })

# def predict_plan(menstrual_start_date, cycle_length):
#     clf, phase_encoder, plan_encoder = load_model_and_encoders()
#     if not clf or not phase_encoder or not plan_encoder:
#         return {"error": "Model or encoders not loaded properly."}

#     phase = calculate_phase(menstrual_start_date, cycle_length)
#     if not phase:
#         return {"error": "Invalid menstrual start date."}

#     phase_encoded = phase_encoder.transform([phase])[0]
#     adherence_history = 1  # Example adherence history, can be dynamic

#     # Predict the plan
#     try:
#         predicted_plan_encoded = clf.predict([[phase_encoded, adherence_history]])[0]
#         predicted_plan = plan_encoder.inverse_transform([predicted_plan_encoded])[0]
#     except Exception as e:
#         print(f"Error in prediction: {e}")
#         return {"error": "Prediction failed."}

#     # Get detailed plan information
#     plan_details = get_plan_details(predicted_plan)

#     return {
#         "plan_name": predicted_plan,
#         "workout": plan_details["workout"],
#         "diet": plan_details["diet"],
#         "workout_image": plan_details["workout_image"],
#         "diet_image": plan_details["diet_image"]
#     }

# # # Example usage:
# # menstrual_start_date = "2023-09-01"  # Example date
# # cycle_length = 28  # Example cycle length
# # plan_details = predict_plan(menstrual_start_date, cycle_length)
# # print(plan_details)








import joblib
from datetime import datetime
import os

# Load the saved model and encoders, handle errors if file not found
def load_model_and_encoders():
    try:
        clf = joblib.load('ml_model.pkl')
        phase_encoder = joblib.load('phase_encoder.pkl')
        plan_encoder = joblib.load('plan_encoder.pkl')
        return clf, phase_encoder, plan_encoder
    except FileNotFoundError as e:
        print(f"Error loading model or encoder: {e}")
        return None, None, None

# Phase mapping for calculating phase based on day in the cycle
phase_map = {
    "menstrual": 0,
    "follicular": 1,
    "ovulatory": 2,
    "luteal": 3
}

def calculate_phase(menstrual_start_date, cycle_length):
    try:
        menstrual_start = datetime.strptime(menstrual_start_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD format.")
        return None
    today = datetime.today()
    days_since_menstrual = (today - menstrual_start).days % cycle_length

    if days_since_menstrual < 7:
        return "menstrual"
    elif days_since_menstrual < 14:
        return "follicular"
    elif days_since_menstrual < 17:
        return "ovulatory"
    else:
        return "luteal"


def get_plan_details(day):
    """Return detailed plans for workouts and meals based on the specific day in the cycle."""
    plans_details = {
        (1, 5): {
            "phase": "Menstrual Phase (Low Energy)",
            "workout": """• Gentle stretching (10 min)
                          • Walking (30 min)
                          • Yoga (focus on restorative poses)
                          • Breathing exercises (5 min)
                          • Pilates (low-intensity)
                          • Meditation (10-15 min)""",
            "diet": """• Breakfast: Oatmeal with flaxseeds, berries, and almond butter
                       • Lunch: Lentil soup with spinach and a whole-grain roll
                       • Dinner: Grilled salmon with steamed broccoli and quinoa""",
            "general_suggestions": """Focus on hydration, and avoid heavy lifting. Listen to your body; rest if needed."""
        },
        (6, 9): {
            "phase": "Follicular Phase (Increasing Energy)",
            "workout": """• Bodyweight squats (3 sets of 15)
                          • Push-ups (3 sets of 10)
                          • Walking lunges (3 sets of 12 per leg)
                          • Mountain climbers (3 sets of 30 seconds)
                          • Cycling (20-30 min)""",
            "diet": """• Breakfast: Smoothie bowl with banana, spinach, almond milk, chia seeds, and protein powder
                       • Lunch: Quinoa salad with chickpeas, cucumber, tomatoes, olive oil, and lemon
                       • Dinner: Chicken stir-fry with vegetables and brown rice""",
            "general_suggestions": "Energy is on the rise; aim for strength-building exercises and increase protein intake."
        },
        (10, 13): {
            "phase": "Follicular Phase (Increasing Energy)",
            "workout": """• Deadlifts (3 sets of 12)
                          • Kettlebell swings (3 sets of 15)
                          • Pull-ups or assisted pull-ups (3 sets of 8)
                          • Dumbbell shoulder press (3 sets of 12)
                          • High-intensity interval training (HIIT) (20 min)""",
            "diet": """• Breakfast: Smoothie bowl with banana, spinach, almond milk, chia seeds, and protein powder
                       • Lunch: Quinoa salad with chickpeas, cucumber, tomatoes, olive oil, and lemon
                       • Dinner: Chicken stir-fry with vegetables and brown rice""",
            "general_suggestions": "Energy is on the rise; aim for strength-building exercises and increase protein intake."
        },
        (14, 16): {
            "phase": "Ovulatory Phase (Peak Energy)",
            "workout": """• Jump rope (5-10 min warm-up)
                          • Sprints (8 rounds of 30 seconds on, 30 seconds off)
                          • Squat jumps (3 sets of 15)
                          • Burpees (3 sets of 12)
                          • Battle ropes (30 seconds on, 30 seconds off, 5 rounds)
                          • Cycling or running (40 min)""",
            "diet": """• Breakfast: Greek yogurt with mixed nuts, honey, and berries
                       • Lunch: Grilled chicken or tofu, mixed greens with avocado, tomatoes, cucumbers, and olive oil
                       • Dinner: Baked sweet potato with black beans, corn, avocado, and salsa""",
            "general_suggestions": "Your energy is highest; incorporate intense cardio, sprints, and metabolic exercises."
        },
        (17, 19): {
            "phase": "Luteal Phase (Moderate Energy)",
            "workout": """• Deadlifts (3 sets of 10)
                          • Leg press (3 sets of 12)
                          • Chest press (3 sets of 10)
                          • Planks (hold for 1 minute, 3 sets)
                          • Rowing machine (20 min)""",
            "diet": """• Breakfast: Whole-grain toast with avocado, poached eggs, and cherry tomatoes
                       • Lunch: Tuna or chickpea salad with mixed greens, bell peppers, and olive oil
                       • Dinner: Turkey or tofu chili with kidney beans, tomatoes, and a side of steamed spinach""",
            "general_suggestions": "Gradually reduce workout intensity. Increase healthy fats and protein to help with hormone balance."
        },
        (20, 23): {
            "phase": "Luteal Phase (Moderate Energy)",
            "workout": """• Resistance band exercises (3 sets of 15 for glutes, legs, arms)
                          • Step-ups (3 sets of 12 per leg)
                          • Wall sits (3 rounds of 30 seconds)
                          • Dumbbell lateral raises (3 sets of 15)
                          • Elliptical or cycling (30 min)""",
            "diet": """• Breakfast: Whole-grain toast with avocado, poached eggs, and cherry tomatoes
                       • Lunch: Tuna or chickpea salad with mixed greens, bell peppers, and olive oil
                       • Dinner: Turkey or tofu chili with kidney beans, tomatoes, and a side of steamed spinach""",
            "general_suggestions": "Gradually reduce workout intensity. Increase healthy fats and protein to help with hormone balance."
        },
        (24, 30): {
            "phase": "Luteal Phase (Low Energy)",
            "workout": """• Light cardio (walking or swimming, 30 min)
                          • Yoga or Pilates (restorative flows)
                          • Seated dumbbell shoulder press (3 sets of 10)
                          • Leg raises (3 sets of 15)
                          • Glute bridges (3 sets of 12)
                          • Meditation or mindfulness practice (10-15 min)""",
            "diet": """• Breakfast: Smoothie with protein powder, banana, spinach, and almond butter
                       • Lunch: Quinoa bowl with roasted veggies, hummus, and pumpkin seeds
                       • Dinner: Grilled fish with sweet potato and steamed asparagus""",
            "general_suggestions": "Energy starts to dip—focus on lighter activities like yoga or walking, and include complex carbohydrates and iron-rich foods."
        }
    }

    # Handle day 0 (first day of menstrual phase)
    if day == 0:
        return {
            "phase": "Menstrual Phase (First Day)",
            "workout": """• Focus on gentle stretching and restorative poses.
                          • Consider meditation and light walking for relaxation.""",
            "diet": """• Prioritize hydration and light meals.
                       • Herbal teas and iron-rich foods are recommended.""",
            "general_suggestions": """Listen to your body; rest if needed and avoid strenuous activities."""
        }

    # Find the matching plan based on the day
    for day_range, details in plans_details.items():
        if day in range(day_range[0], day_range[1] + 1):
            return details

    # Default plan if no match is found
    return {
        "phase": "Unknown Phase",
        "workout": "No workout details available.",
        "diet": "No diet details available.",
        "general_suggestions": "Please consult your healthcare provider for personalized advice."
    }

def predict_plan(menstrual_start_date, cycle_length, day):
    clf, phase_encoder, plan_encoder = load_model_and_encoders()
    if not clf or not phase_encoder or not plan_encoder:
        return {"error": "Model or encoders not loaded properly."}

    phase = calculate_phase(menstrual_start_date, cycle_length)
    if not phase:
        return {"error": "Invalid menstrual start date."}

    phase_encoded = phase_encoder.transform([phase])[0]
    adherence_history = 1  # Example adherence history, can be dynamic

    # Predict the plan
    try:
        predicted_plan_encoded = clf.predict([[phase_encoded, adherence_history]])[0]
        predicted_plan = plan_encoder.inverse_transform([predicted_plan_encoded])[0]
    except Exception as e:
        print(f"Error in prediction: {e}")
        return {"error": "Prediction failed."}

    # Get detailed plan information based on the day in the cycle
    plan_details = get_plan_details(day)

    return {
        "plan_name": predicted_plan,
        "phase": plan_details["phase"],
        "workout": plan_details["workout"],
        "diet": plan_details["diet"],
        "general_suggestions": plan_details["general_suggestions"]
    }

# # Example usage:
# menstrual_start_date = "2023-09-01"  # Example date
# cycle_length = 28  #
