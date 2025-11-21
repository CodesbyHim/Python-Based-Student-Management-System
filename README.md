# Python Based Student Management System (SQLite Integration)

This is a simple desktop-based Student Management System built using **Core Python, Tkinter**, and **SQLite3**.  
I made this project mainly to practice CRUD operations, database handling, and GUI development in Python.

The application allows you to:
- Add new students  
- View all student records  
- Update existing records  
- Delete students  
- Search students  
- Export data to Excel or CSV  
- Login authentication (username + password)  
- Clean UI built with Tkinter

---

## 🔧 Tech Stack Used

- **Python (Core + OOPs)**
- **Tkinter** for GUI
- **SQLite3** for database
- **OpenPyXL** for Excel export
- **CSV module** for exporting CSV

---

## 📂 Project Structure
project-folder/
│
├── main.py
├── gui.py
├── database.py
├── utils.py
├── students.db
└── README.md

---

## 🚀 Features

### ✔ Login System
Basic login window with pre-defined username and password.

### ✔ Add Student
You can add name, age, gender, email, and course.

### ✔ Update Student
Select a record and update it easily.

### ✔ Delete Student
Remove records from the database.

### ✔ Search Student  
Search by name, course, or email.

### ✔ Export to Excel and CSV  
Useful for backup or reporting.

---

## 🛠 How to Run the Project

### 1. Create virtual environment
```
python -m venv SMSvenv
```
### 2. Activate the environment
Windows:
```
SMSvenv\Scripts\activate
```
### 3. Install required packages
```
pip install openpyxl
```
### 4. Run the project
```
python main.py
```

### 📌 Default Login Credentials
```
Username: admin
Password: admin123
```

You can modify these in the code if needed.

## ✍️ What I Learned from This Project

- Working with Tkinter forms and widgets
- Handling CRUD operations in SQLite
- Using Python OOP to organize GUI + database code
- Exporting database records to Excel and CSV
- Building a simple but functional desktop application
