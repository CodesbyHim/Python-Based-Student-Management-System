import tkinter as tk
from gui import LoginWindow, StudentManagementSystem

def open_main_app():
    main_root = tk.Tk()
    StudentManagementSystem(main_root)
    main_root.mainloop()

def main():
    root = tk.Tk()
    LoginWindow(root, open_main_app)
    root.mainloop()

if __name__ == "__main__":
    main()
