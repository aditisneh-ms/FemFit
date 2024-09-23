import sqlite3

def init_db():
    conn = sqlite3.connect('well_ai.db')  # Make sure the path matches your db path in db_manager.py
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            menstrual_start_date TEXT,
            cycle_length INTEGER
        )
    ''')

    # Create any additional tables you need here

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

if __name__ == '__main__':
    init_db()
