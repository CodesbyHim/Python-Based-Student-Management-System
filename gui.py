import tkinter as tk
from tkinter import ttk, messagebox
from database import DatabaseManager
from utils import is_valid_email, is_valid_age, export_to_excel, export_to_csv


db = DatabaseManager()

# -----------------------------------------------------------
# LOGIN WINDOW
# -----------------------------------------------------------
class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success
        self.root.title("Login - Student Management System")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        tk.Label(root, text="Admin Login", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Username").pack()
        self.username_entry = tk.Entry(root, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Password").pack()
        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack(pady=5)

        login_btn = tk.Button(root, text="Login", width=20, command=self.login)
        login_btn.pack(pady=15)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username == "admin" and password == "admin123":
            self.root.destroy()
            self.on_login_success()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")


# -----------------------------------------------------------
# MAIN STUDENT MANAGEMENT WINDOW
# -----------------------------------------------------------
class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        # Input Frame
        input_frame = tk.Frame(root, padx=10, pady=10, relief=tk.RIDGE, borderwidth=2)
        input_frame.place(x=10, y=10, width=350, height=580)

        tk.Label(input_frame, text="Student Details", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(input_frame, text="Name").pack()
        self.name_entry = tk.Entry(input_frame, width=30)
        self.name_entry.pack(pady=5)

        tk.Label(input_frame, text="Age").pack()
        self.age_entry = tk.Entry(input_frame, width=30)
        self.age_entry.pack(pady=5)

        tk.Label(input_frame, text="Email").pack()
        self.email_entry = tk.Entry(input_frame, width=30)
        self.email_entry.pack(pady=5)

        tk.Label(input_frame, text="Course").pack()
        self.course_entry = tk.Entry(input_frame, width=30)
        self.course_entry.pack(pady=5)

        add_btn = tk.Button(input_frame, text="Add Student", width=20, command=self.add_student)
        add_btn.pack(pady=10)

        update_btn = tk.Button(input_frame, text="Update Student", width=20, command=self.update_student)
        update_btn.pack(pady=10)

        delete_btn = tk.Button(input_frame, text="Delete Student", width=20, command=self.delete_student)
        delete_btn.pack(pady=10)

        export_excel_btn = tk.Button(input_frame, text="Export to Excel", width=20, command=export_to_excel)
        export_excel_btn.pack(pady=10)

        export_csv_btn = tk.Button(input_frame, text="Export to CSV", width=20, command=export_to_csv)
        export_csv_btn.pack(pady=10)

        # Table Frame
        table_frame = tk.Frame(root, padx=10, pady=10, relief=tk.RIDGE, borderwidth=2)
        table_frame.place(x=380, y=10, width=500, height=580)

        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        self.student_table = ttk.Treeview(
            table_frame,
            columns=("id", "name", "age", "email", "course"),
            show="headings",
            yscrollcommand=scroll_y.set
        )
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("age", text="Age")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("course", text="Course")

        self.student_table.column("id", width=40)
        self.student_table.column("name", width=120)
        self.student_table.column("age", width=60)
        self.student_table.column("email", width=150)
        self.student_table.column("course", width=120)

        self.student_table.pack(fill=tk.BOTH, expand=True)
        self.student_table.bind("<ButtonRelease-1>", self.load_selected_student)

        self.load_students()

    # -----------------------------------------------------------
    # CRUD FUNCTIONS
    # -----------------------------------------------------------

    def load_students(self):
        for row in self.student_table.get_children():
            self.student_table.delete(row)

        students = db.fetch_students()

        for student in students:
            self.student_table.insert("", tk.END, values=student)

    def add_student(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        email = self.email_entry.get().strip()
        course = self.course_entry.get().strip()

        if not name or not age or not email or not course:
            messagebox.showwarning("Warning", "All fields are required!")
            return

        if not is_valid_age(age):
            messagebox.showwarning("Invalid Age", "Age must be a number between 1 and 120.")
            return

        if not is_valid_email(email):
            messagebox.showwarning("Invalid Email", "Please enter a valid email format.")
            return

        db.add_student(name, age, email, course)
        self.load_students()
        messagebox.showinfo("Success", "Student added successfully.")

    def load_selected_student(self, event):
        selected = self.student_table.focus()
        if selected:
            values = self.student_table.item(selected, "values")
            self.selected_id = values[0]

            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.course_entry.delete(0, tk.END)

            self.name_entry.insert(0, values[1])
            self.age_entry.insert(0, values[2])
            self.email_entry.insert(0, values[3])
            self.course_entry.insert(0, values[4])

    def update_student(self):
        if not hasattr(self, "selected_id"):
            messagebox.showwarning("Warning", "Select a student from the table first.")
            return

        name = self.name_entry.get()
        age = self.age_entry.get()
        email = self.email_entry.get()
        course = self.course_entry.get()

        if not is_valid_age(age):
            messagebox.showwarning("Invalid Age", "Age must be numeric.")
            return

        if not is_valid_email(email):
            messagebox.showwarning("Invalid Email", "Invalid email format.")
            return

        db.update_student(self.selected_id, name, age, email, course)
        self.load_students()
        messagebox.showinfo("Success", "Student updated successfully.")

    def delete_student(self):
        if not hasattr(self, "selected_id"):
            messagebox.showwarning("Warning", "Select a student first.")
            return

        db.delete_student(self.selected_id)
        self.load_students()
        messagebox.showinfo("Success", "Student deleted successfully.")
