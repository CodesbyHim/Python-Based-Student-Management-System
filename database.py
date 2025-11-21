import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL,
                course TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_student(self, name, age, email, course):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, email, course) VALUES (?, ?, ?, ?)",
            (name, age, email, course)
        )
        self.conn.commit()

    def fetch_students(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, age, email, course FROM students")
        return cursor.fetchall()

    def update_student(self, student_id, name, age, email, course):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE students SET name=?, age=?, email=?, course=? WHERE id=?",
            (name, age, email, course, student_id)
        )
        self.conn.commit()

    def delete_student(self, student_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        self.conn.commit()
