import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "students.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

students = load_data()

# ---------- Login Window ----------
def login():
    if username_entry.get() == "Mohit" and password_entry.get() == "842484":
        login_window.destroy()
        main_window()
    else:
        messagebox.showerror("Error", "Invalid Login")

login_window = tk.Tk()
login_window.title("Admin Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Admin Login", font=("Arial", 55)).pack(pady=40)
tk.Label(login_window, text="Username").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=10)

# ---------- Main Window ----------
def main_window():
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("400x400")

    tk.Label(root, text="Student Management System", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Add Student", width=40, command=add_student_window).pack(pady=5)
    tk.Button(root, text="View Students", width=40, command=view_students).pack(pady=5)
    tk.Button(root, text="Delete Student", width=30, command=delete_student).pack(pady=5)

    root.mainloop()

# ---------- Add Student ----------
def add_student_window():
    add = tk.Toplevel()
    add.title("Add Student")
    add.geometry("300x300")

    tk.Label(add, text="Roll No").pack()
    roll_entry = tk.Entry(add)
    roll_entry.pack()

    tk.Label(add, text="Name").pack()
    name_entry = tk.Entry(add)
    name_entry.pack()

    tk.Label(add, text="Course").pack()
    course_entry = tk.Entry(add)
    course_entry.pack()

    tk.Label(add, text="Marks").pack()
    marks_entry = tk.Entry(add)
    marks_entry.pack()

    def save_student():
        roll = roll_entry.get()
        name = name_entry.get()
        course = course_entry.get()
        marks = marks_entry.get()

        for s in students:
            if s["roll"] == roll:
                messagebox.showerror("Error", "Roll already exists")
                return

        students.append({
            "roll": roll,
            "name": name,
            "course": course,
            "marks": marks
        })
        save_data(students)
        messagebox.showinfo("Success", "Student Added")
        add.destroy()

    tk.Button(add, text="Save", command=save_student).pack(pady=10)

# ---------- View Students ----------
def view_students():
    view = tk.Toplevel()
    view.title("Students List")
    view.geometry("400x300")

    text = tk.Text(view)
    text.pack()

    for s in students:
        text.insert(tk.END, f"Roll: {s['roll']} | Name: {s['name']} | Course: {s['course']} | Marks: {s['marks']}\n")

# ---------- Delete Student ----------
def delete_student():
    roll = tk.simpledialog.askstring("Delete", "Enter Roll Number")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_data(students)
            messagebox.showinfo("Success", "Student Deleted")
            return
    messagebox.showerror("Error", "Student not found")

login_window.mainloop()