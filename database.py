# database.py

import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("reminders.db", check_same_thread=False)
cursor = conn.cursor()

# Create the reminders table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        task TEXT,
        date TEXT,
        time TEXT
    )
''')
conn.commit()

# Insert a new reminder
def insert_reminder(user_id, task, date, time):
    cursor.execute(
        "INSERT INTO reminders (user_id, task, date, time) VALUES (?, ?, ?, ?)",
        (user_id, task, date, time)
    )
    conn.commit()

# Optional: Get all reminders for a user
def get_reminders(user_id):
    cursor.execute("SELECT task, date, time FROM reminders WHERE user_id=?", (user_id,))
    return cursor.fetchall()
# Clear all reminders for a specific user
def clear_reminders(user_id):
    cursor.execute("DELETE FROM reminders WHERE user_id=?", (user_id,))
    conn.commit()
def delete_reminder_by_task(user_id, task_keyword):
    cursor.execute("""
        DELETE FROM reminders 
        WHERE user_id = ? AND task LIKE ?
    """, (user_id, f"%{task_keyword}%"))
    conn.commit()
    return cursor.rowcount  # number of rows deleted

