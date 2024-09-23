# import pandas as pd
# import random

# def generate_large_dataset(num_records=5000):
#     """Generate a synthetic dataset with the specified number of records."""
#     phases = ['menstrual', 'follicular', 'ovulation', 'luteal']
#     plans = ['light_workout', 'heavy_workout', 'hiit', 'moderate_workout',
#              'iron_diet', 'protein_diet', 'carb_diet', 'magnesium_diet']
    
#     data = {
#         'phase': [],
#         'adherence_history': [],
#         'recommended_plan': []
#     }
    
#     for _ in range(num_records):
#         phase = random.choice(phases)
#         adherence_history = random.randint(0, 1)  # 0 or 1 for simplicity
#         recommended_plan = random.choice(plans)
        
#         data['phase'].append(phase)
#         data['adherence_history'].append(adherence_history)
#         data['recommended_plan'].append(recommended_plan)
    
#     df = pd.DataFrame(data)
#     df.to_csv('large_synthetic_workout_diet_data.csv', index=False)
#     print(f"Generated {num_records} records and saved to 'large_synthetic_workout_diet_data.csv'.")

# if __name__ == "__main__":
#     generate_large_dataset()

import pandas as pd
import random

def generate_large_dataset(num_records=5000):
    """Generate a synthetic dataset with the specified number of records."""

    phases = ['menstrual', 'follicular', 'ovulatory', 'luteal']
    
    workouts = [
        "Gentle stretching, Walking, Yoga, Breathing exercises, Pilates, Meditation",
        "Bodyweight squats, Push-ups, Walking lunges, Mountain climbers, Cycling",
        "Deadlifts, Kettlebell swings, Pull-ups, Dumbbell shoulder press, HIIT",
        "Jump rope, Sprints, Squat jumps, Burpees, Battle ropes, Cycling",
        "Deadlifts, Leg press, Chest press, Planks, Rowing machine",
        "Resistance band exercises, Step-ups, Wall sits, Dumbbell lateral raises, Cycling",
        "Light cardio, Yoga, Seated dumbbell shoulder press, Leg raises, Glute bridges"
    ]
    
    diets = [
        "Oatmeal with flaxseeds, Lentil soup, Grilled salmon",
        "Smoothie bowl, Quinoa salad, Chicken stir-fry",
        "Greek yogurt, Grilled chicken, Baked sweet potato",
        "Poached Eggs, Whole-grain toast with avocado, Turkey or tofu chili with kidney beans, Baked sweet potato with black beans, Corn",
        "Whole-grain toast, Tuna salad, Turkey chili",
        "Smoothie with protein powder, Quinoa bowl, Grilled fish",
        "Hydration, Snacks, Supplements, Rest"
    ]
    
    general_suggestions = [
        "Focus on hydration, avoid heavy lifting.",
        "Aim for strength-building exercises, increase protein intake.",
        "Incorporate intense cardio, sprints, and metabolic exercises.",
        "Gradually reduce workout intensity, increase healthy fats.",
        "Focus on lighter activities, include complex carbohydrates.",
        "Hydration: Aim for 8-10 glasses of water daily.",
        "Rest and recovery are crucial."
    ]
    
    data = {
        'phase': [],
        'workout': [],
        'diet': [],
        'general_suggestions': [],
        'adherence_history': []
    }
    
    for _ in range(num_records):
        phase_index = random.randint(0, len(phases) - 1)
        phase = phases[phase_index]
        
        data['phase'].append(phase)
        data['workout'].append(workouts[phase_index])
        data['diet'].append(diets[phase_index])
        data['general_suggestions'].append(general_suggestions[phase_index])
        data['adherence_history'].append(random.randint(0, 1))  # 0 or 1 for simplicity
    
    df = pd.DataFrame(data)
    df.to_csv('large_synthetic_workout_diet_data.csv', index=False)
    print(f"Generated {num_records} records and saved to 'large_synthetic_workout_diet_data.csv'.")

if __name__ == "__main__":
    generate_large_dataset()

# import pandas as pd
# import random

# def generate_large_dataset(num_records=5000):
#     """Generate a synthetic dataset with the specified number of records."""
#     phases = ['menstrual', 'follicular', 'ovulation', 'luteal']
#     workouts = [
#         'light_workout', 'heavy_workout', 'hiit', 'moderate_workout',
#         'restorative', 'strength_training', 'cardio', 'low_intensity'
#     ]
    
#     data = {
#         'phase': [],
#         'adherence_history': [],
#         'workout': []
#     }
    
#     for _ in range(num_records):
#         phase = random.choice(phases)
#         adherence_history = random.randint(0, 1)  # 0 or 1 for simplicity
#         workout = random.choice(workouts)
        
#         data['phase'].append(phase)
#         data['adherence_history'].append(adherence_history)
#         data['workout'].append(workout)
    
#     df = pd.DataFrame(data)
#     df.to_csv('large_synthetic_workout_diet_data.csv', index=False)
#     print(f"Generated {num_records} records and saved to 'large_synthetic_workout_diet_data.csv'.")

# if __name__ == "__main__":
#     generate_large_dataset()
