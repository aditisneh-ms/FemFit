# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.ensemble import RandomForestClassifier
# import joblib

# # Load the large dataset
# data = pd.read_csv('large_synthetic_workout_diet_data.csv')

# # Encode categorical features
# phase_encoder = LabelEncoder()
# data['phase'] = phase_encoder.fit_transform(data['phase'])

# plan_encoder = LabelEncoder()
# data['recommended_plan'] = plan_encoder.fit_transform(data['recommended_plan'])

# # Split the dataset into features and target variable
# X = data[['phase', 'adherence_history']]
# y = data['recommended_plan']

# # Split the data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train the model
# clf = RandomForestClassifier(n_estimators=100, random_state=42)
# clf.fit(X_train, y_train)

# # Save the model and encoders
# joblib.dump(clf, 'ml_model.pkl')
# joblib.dump(phase_encoder, 'phase_encoder.pkl')
# joblib.dump(plan_encoder, 'plan_encoder.pkl')

# # Print model accuracy
# accuracy = clf.score(X_test, y_test)
# print(f"Model trained with accuracy: {accuracy:.2f}")


# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.ensemble import RandomForestClassifier
# import joblib

# # Load the large dataset
# data = pd.read_csv('large_synthetic_workout_diet_data.csv')

# # Encode categorical features
# phase_encoder = LabelEncoder()
# data['phase'] = phase_encoder.fit_transform(data['phase'])

# # Instead of 'recommended_plan', we will now predict the workout
# # so we need to encode workouts instead
# workout_encoder = LabelEncoder()
# data['workout'] = workout_encoder.fit_transform(data['workout'])

# # Split the dataset into features and target variable
# X = data[['phase', 'adherence_history']]
# y = data['workout']

# # Split the data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train the model
# clf = RandomForestClassifier(n_estimators=100, random_state=42)
# clf.fit(X_train, y_train)

# # Save the model and encoders
# joblib.dump(clf, 'ml_model.pkl')
# joblib.dump(phase_encoder, 'phase_encoder.pkl')
# joblib.dump(workout_encoder, 'workout_encoder.pkl')

# # Print model accuracy
# accuracy = clf.score(X_test, y_test)
# print(f"Model trained with accuracy: {accuracy:.2f}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the large dataset
data = pd.read_csv('large_synthetic_workout_diet_data.csv')

# Encode categorical features
phase_encoder = LabelEncoder()
data['phase'] = phase_encoder.fit_transform(data['phase'])

workout_encoder = LabelEncoder()
data['workout'] = workout_encoder.fit_transform(data['workout'])

# Split the dataset into features and target variable
X = data[['phase', 'adherence_history']]
y = data['workout']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train the model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save the model and encoders
joblib.dump(clf, 'ml_model.pkl')
joblib.dump(phase_encoder, 'phase_encoder.pkl')
joblib.dump(workout_encoder, 'workout_encoder.pkl')

# Print model accuracy
accuracy = clf.score(X_test, y_test)
print(f"Model trained with accuracy: {accuracy:.2f}")
