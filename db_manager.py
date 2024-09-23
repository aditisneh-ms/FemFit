# from app import app,db

# app.app_context().push()
# # Create the database and tables
# db.create_all()

# print("Database and tables created!")

import sqlite3

import sqlite3

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect('well_ai.db')  # Ensure this matches the path in init_db.py
    conn.row_factory = sqlite3.Row
    return conn

def create_user(name, age, gender, menstrual_start_date=None, cycle_length=None):
    """Creates a new user profile in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, age, gender, menstrual_start_date, cycle_length) VALUES (?, ?, ?, ?, ?)",
        (name, age, gender, menstrual_start_date, cycle_length)
    )
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return user_id

def get_user_by_id(user_id):
    """Fetches a user profile from the database by user ID."""
    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()
    conn.close()
    return user
