# # from flask import Flask, render_template, request, redirect, url_for
# # from db_manager import create_user, get_user_by_id
# # from ml_model import predict_plan

# # app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return render_template('index.html', title="Home")

# # @app.route('/about')
# # def about():
# #     return render_template('about.html', title="About")

# # @app.route('/profile', methods=['GET', 'POST'])
# # def profile():
# #     if request.method == 'POST':
# #         # Save user data and redirect to user profile page
# #         name = request.form['name']
# #         age = int(request.form['age'])
# #         gender = request.form['gender']
# #         menstrual_start_date = request.form['menstrual_start_date']
# #         cycle_length = request.form['cycle_length']
# #         user_id = create_user(name, age, gender, menstrual_start_date, cycle_length)
# #         return redirect(url_for('user_profile', user_id=user_id))
# #     return render_template('profile.html', title="Create Profile")

# # @app.route('/user_profile/<int:user_id>')
# # def user_profile(user_id):
# #     user = get_user_by_id(user_id)
# #     recommended_plan = predict_plan(user.menstrual_start_date, user.cycle_length)
# #     return render_template('user_profile.html', user=user, recommended_plan=recommended_plan, title=f"{user.name}'s Profile")

# # if __name__ == '__main__':
# #     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html', title="Home")

# @app.route('/about')
# def about():
#     return render_template('about.html', title="About")

# @app.route('/profile', methods=['GET', 'POST'])
# def profile():
#     if request.method == 'POST':
#         from db_manager import create_user
#         name = request.form['name']
#         age = int(request.form['age'])
#         gender = request.form['gender']
#         menstrual_start_date = request.form['menstrual_start_date']
#         cycle_length = request.form['cycle_length']
#         user_id = create_user(name, age, gender, menstrual_start_date, cycle_length)
#         return redirect(url_for('user_profile', user_id=user_id))
#     return render_template('profile.html', title="Create Profile")


# @app.route('/user_profile/<int:user_id>')
# def user_profile(user_id):
#     # Import here to avoid circular import issue
#     from db_manager import get_user_by_id
#     from ml_model import predict_plan

#     user = get_user_by_id(user_id)
#     recommended_plan = predict_plan(user['menstrual_start_date'], user['cycle_length'])
#     return render_template('user_profile.html', user=user, recommended_plan=recommended_plan, title=f"{user['name']}'s Profile")

# @app.route('/create_profile', methods=['POST'])
# def create_profile():
#     from db_manager import create_user
    
#     # Collect data from the form submission
#     name = request.form['name']
#     age = int(request.form['age'])
#     gender = request.form['gender']
#     menstrual_start_date = request.form['menstrual_start_date']
#     cycle_length = request.form['cycle_length']
    
#     # Create user and get the user ID
#     user_id = create_user(name, age, gender, menstrual_start_date, cycle_length)
    
#     # Redirect to the user's profile page
#     return redirect(url_for('user_profile', user_id=user_id))

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for, flash
# from ml_model import predict_plan  # Import the updated predict_plan function
# from db_manager import create_user, get_user_by_id
# from datetime import datetime

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# @app.route('/')
# def home():
#     return render_template('home.html', title="Well-AI Home")

# @app.route('/about')
# def about():
#     return render_template('about.html', title="About Well-AI")

# @app.route('/create_profile', methods=['POST'])
# def create_profile():
#     try:
#         # Collect user inputs from the form
#         name = request.form['name']
#         age = int(request.form['age'])
#         menstrual_start_date = request.form['menstrual_start_date']
#         cycle_length = int(request.form['cycle_length'])

#         # Create a new user in the database
#         user_id = create_user(name, age, menstrual_start_date, cycle_length)

#         # Redirect to user profile page with the new user ID
#         return redirect(url_for('user_profile', user_id=user_id))
#     except Exception as e:
#         flash(f"Error creating profile: {e}")
#         return redirect(url_for('home'))

# @app.route('/profile/<int:user_id>')
# def user_profile(user_id):
#     try:
#         # Get user details from the database
#         user = get_user_by_id(user_id)
#         if not user:
#             flash("User not found.")
#             return redirect(url_for('home'))

#         # Calculate the current day in the cycle based on menstrual start date
#         menstrual_start_date = datetime.strptime(user['menstrual_start_date'], "%Y-%m-%d")
#         today = datetime.today()
#         cycle_length = user['cycle_length']
#         day = (today - menstrual_start_date).days % cycle_length

#         # Get workout and diet plan based on menstrual cycle phase
#         plan_details = predict_plan(user['menstrual_start_date'], cycle_length, day)

#         if "error" in plan_details:
#             flash(plan_details['error'])
#             return redirect(url_for('home'))

#         return render_template('profile.html', 
#                                user=user, 
#                                title="User Profile", 
#                                plan_name=plan_details['plan_name'],
#                                workout=plan_details['workout'], 
#                                diet=plan_details['diet'],
#                                workout_image=plan_details['workout_image'], 
#                                diet_image=plan_details['diet_image'])
#     except Exception as e:
#         flash(f"Error loading profile: {e}")
#         return redirect(url_for('home'))

# @app.route('/get_started')
# def get_started():
#     return render_template('create_profile.html', title="Create Profile")

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        from db_manager import create_user
        name = request.form['name']
        age = int(request.form['age'])
        gender = request.form['gender']
        menstrual_start_date = request.form['menstrual_start_date']
        cycle_length = request.form['cycle_length']
        user_id = create_user(name, age, gender, menstrual_start_date, cycle_length)
        return redirect(url_for('user_profile', user_id=user_id))
    return render_template('profile.html', title="Create Profile")


@app.route('/user_profile/<int:user_id>')
def user_profile(user_id):
    # Import here to avoid circular import issue
    from db_manager import get_user_by_id
    from ml_model import predict_plan

    user = get_user_by_id(user_id)
    
    # Calculate the current day in the menstrual cycle
    menstrual_start_date = user['menstrual_start_date']
    cycle_length = user['cycle_length']
    today = datetime.today()

    # Calculate the number of days since the menstrual start date
    days_since_menstrual = (today - datetime.strptime(menstrual_start_date, "%Y-%m-%d")).days % cycle_length

    # Call the predict_plan function
    recommended_plan = predict_plan(user['menstrual_start_date'], user['cycle_length'], days_since_menstrual)
    
    return render_template('user_profile.html', user=user, recommended_plan=recommended_plan, title=f"{user['name']}'s Profile")

@app.route('/create_profile', methods=['POST'])
def create_profile():
    from db_manager import create_user
    
    # Collect data from the form submission
    name = request.form['name']
    age = int(request.form['age'])
    gender = request.form['gender']
    menstrual_start_date = request.form['menstrual_start_date']
    cycle_length = request.form['cycle_length']
    
    # Create user and get the user ID
    user_id = create_user(name, age, gender, menstrual_start_date, cycle_length)
    
    # Redirect to the user's profile page
    return redirect(url_for('user_profile', user_id=user_id))

if __name__ == '__main__':
    app.run(debug=True)
