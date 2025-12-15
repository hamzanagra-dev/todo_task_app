# This file handles all communication with the database.
# It hides the complexity of database code from the rest of the application.
import sqlite3 # The library for working with SQLite databases.

# This is a constant that holds the name of our database file.
DB_FILE = "tasks.db"

def _get_connection():
    """Gets a database connection and sets the row factory."""
    # Connect to the database file.
    conn = sqlite3.connect(DB_FILE)
    # This special setting makes the database return results as dictionary-like objects,
    # which are much easier to work with than the default (tuples).
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database and creates the tasks table if it doesn't exist."""
    conn = _get_connection()
    cursor = conn.cursor() # A cursor is an object used to send commands to the database.
    # This is an SQL command. 'CREATE TABLE IF NOT EXISTS' is a safe way to create a table,
    # as it won't do anything if the table is already there.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT,
            done BOOLEAN NOT NULL CHECK (done IN (0, 1)),
            due_date TEXT,
            completion_date TEXT
        )
    ''')
    conn.commit() # 'commit' saves the changes we made.
    conn.close()  # Always close the connection when you're done.

def load_tasks():
    """Loads all tasks from the SQLite database."""
    conn = _get_connection()
    cursor = conn.cursor()
    # 'SELECT * FROM tasks' is an SQL command to get all columns from all rows in the 'tasks' table.
    cursor.execute("SELECT * FROM tasks")
    # This converts the list of database rows into a standard list of Python dictionaries.
    tasks = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return tasks

def add_task_db(task):
    """Adds a single task to the database."""
    conn = _get_connection()
    cursor = conn.cursor()
    # 'INSERT INTO' is the SQL command to add a new row.
    # The '?' are placeholders. We provide the actual values as a separate tuple.
    # This is a security measure to prevent a type of attack called SQL Injection.
    cursor.execute(
        "INSERT INTO tasks (id, title, description, priority, done, due_date, completion_date) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (task['id'], task['title'], task['description'], task['priority'], task['done'], task['due_date'], task['completion_date'])
    )
    conn.commit() # Save the new row.
    conn.close()

def update_task_db(task):
    """Updates a single task in the database."""
    conn = _get_connection()
    cursor = conn.cursor()
    # 'UPDATE' is the SQL command to modify an existing row.
    # The 'WHERE id = ?' part specifies which row to update.
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, priority = ?, done = ?, due_date = ?, completion_date = ? WHERE id = ?",
        (task['title'], task['description'], task['priority'], task['done'], task['due_date'], task['completion_date'], task['id'])
    )
    conn.commit() # Save the changes.
    conn.close()

def delete_task_db(task_id):
    """Deletes a single task from the database by its ID."""
    conn = _get_connection()
    cursor = conn.cursor()
    # 'DELETE FROM' is the SQL command to remove a row.
    # 'WHERE id = ?' specifies which row to delete.
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit() # Save the deletion.
    conn.close()
