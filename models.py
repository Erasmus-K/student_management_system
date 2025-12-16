import sqlite3

def get_connection():
    return sqlite3.connect('database.db')

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            course TEXT NOT NULL
        )
    ''')
    
    # Create FeeStructure table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS FeeStructure (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course TEXT NOT NULL,
            amount REAL NOT NULL
        )
    ''')
    
    # Create Attendance table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course TEXT NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Students (id)
        )
    ''')
    
    # Insert sample students if table is empty
    cursor.execute("SELECT COUNT(*) FROM Students")
    if cursor.fetchone()[0] == 0:
        sample_students = [
            ('John Doe', 'john.doe@email.com', 'Computer Science'),
            ('Jane Smith', 'jane.smith@email.com', 'Mathematics'),
            ('Mike Johnson', 'mike.johnson@email.com', 'Physics'),
            ('Sarah Wilson', 'sarah.wilson@email.com', 'Chemistry'),
            ('David Brown', 'david.brown@email.com', 'Biology')
        ]
        cursor.executemany("INSERT INTO Students (name, email, course) VALUES (?, ?, ?)", sample_students)
    
    conn.commit()
    conn.close()