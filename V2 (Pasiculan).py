import sqlite3
import tkinter as tk
from tkinter import messagebox, Entry, Button

# Connect to the database
conn = sqlite3.connect('student_info.db')
c = conn.cursor()

# Create Students table

c.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        gender TEXT NOT NULL,
        year_level INTEGER NOT NULL,
        course_code TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL,
        FOREIGN KEY (course_code) REFERENCES courses (code)
    )
''')


# Create Courses table
c.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        code TEXT PRIMARY KEY,
        course TEXT NOT NULL
    )
''')

class Student:
    def __init__(self, id, name, gender, year_level, course_code, age, email):
        self.id = id
        self.name = name
        self.gender = gender
        self.year_level = year_level
        self.course_code = course_code
        self.age = age
        self.email = email

class Course:
    def __init__(self, code, course):
        self.code = code
        self.course = course

class StudentInformationSystem:
    def __init__(self):
        self.conn = sqlite3.connect('student_info.db')
        self.c = self.conn.cursor()

        self.root = tk.Tk()
        self.root.title("Student Information System")
        self.root.geometry("600x500")  # Set the window size to 800x500

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=50, pady=50)
        
        self.student_frame = tk.Frame(self.frame, padx=20, pady=20)  # Create a frame for the student section
        self.student_frame.grid(row=0, column=2, padx=50)  # Place the student frame in column 0

        self.label = tk.Label(self.frame, text="Student ID:")
        self.label.grid(row=0, column=0)
        self.id_entry = tk.Entry(self.frame)
        self.id_entry.grid(row=0, column=1)

        self.label = tk.Label(self.frame, text="Name:")
        self.label.grid(row=1, column=0)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=1, column=1)

        self.label = tk.Label(self.frame, text="Gender:")
        self.label.grid(row=2, column=0)
        self.gender_entry = tk.Entry(self.frame)
        self.gender_entry.grid(row=2, column=1)
        
        self.label = tk.Label(self.frame, text="Age:")
        self.label.grid(row=3, column=0)
        self.age_entry = tk.Entry(self.frame)
        self.age_entry.grid(row=3, column=1)
        
        self.label = tk.Label(self.frame, text="Email:")
        self.label.grid(row=4, column=0)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=4, column=1)

        self.label = tk.Label(self.frame, text="Year Level:")
        self.label.grid(row=5, column=0)
        self.year_level_entry = tk.Entry(self.frame)
        self.year_level_entry.grid(row=5, column=1)

        self.label = tk.Label(self.frame, text="Course Code:")
        self.label.grid(row=6, column=0)
        self.course_code_entry = tk.Entry(self.frame)
        self.course_code_entry.grid(row=6, column=1)

        self.add_student_button = tk.Button(self.frame, text="Add Student", command=self.add_student)
        self.add_student_button.grid(row=7, column=0, pady=15)

        self.delete_student_button = tk.Button(self.frame, text="Delete Student", command=self.delete_student)
        self.delete_student_button.grid(row=7, column=1, pady=15)

        self.edit_student_button = tk.Button(self.frame, text="Edit Student", command=self.edit_student)
        self.edit_student_button.grid(row=8, column=0, pady=10)

        self.list_students_button = tk.Button(self.frame, text="List Students", command=self.list_students)
        self.list_students_button.grid(row=8, column=1, pady=10)
        
        self.search_student_button = tk.Button(self.frame, text="Search Student", command=self.search_student)
        self.search_student_button.grid(row=9, column=0, pady=10)

        self.label = tk.Label(self.frame, text="Course Code:")
        self.label.grid(row=0, column=2)
        self.course_code_entry2 = tk.Entry(self.frame)
        self.course_code_entry2.grid(row=0, column=3)
        
        self.label = tk.Label(self.frame, text="Course:")
        self.label.grid(row=1, column=2)
        self.course_entry = tk.Entry(self.frame)
        self.course_entry.grid(row=1, column=3)

        self.add_course_button = tk.Button(self.frame, text="Add Course", command=self.add_course)
        self.add_course_button.grid(row=2, column=2, padx = 50, pady=10)

        self.delete_course_button = tk.Button(self.frame, text="Delete Course", command=self.delete_course)
        self.delete_course_button.grid(row=2, column=3, pady=10)

        self.edit_course_button = tk.Button(self.frame, text="Edit Course", command=self.edit_course)
        self.edit_course_button.grid(row=3, column=2, padx = 50, pady=10)

        self.list_courses_button = tk.Button(self.frame, text="List Courses", command=self.list_courses)
        self.list_courses_button.grid(row=3, column=3, pady=10)

    def clear_fields(self):
        self.id_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.gender_entry.delete(0,"end")
        self.year_level_entry.delete(0, "end")
        self.course_code_entry.delete(0, "end")

    def add_student(self):
        id = self.id_entry.get()
        name = self.name_entry.get()
        gender = self.gender_entry.get()
        year_level = self.year_level_entry.get()
        course_code = self.course_code_entry.get()
        age = self.age_entry.get()
        email = self.email_entry.get()

        # Check if the course code exists
        self.c.execute("SELECT * FROM courses WHERE code = ?", (course_code,))
        course = self.c.fetchone()

        if course is None:
            messagebox.showwarning("Error", "Invalid course code. Please enter a valid course code.")
            return

        # Validate inputs
        if id and name and gender and year_level and course_code and age and email:
            # Create a new Student instance
            student = Student(id, name, gender, year_level, course_code, age, email)

            # Insert the student into the database
            self.c.execute('INSERT INTO students (id, name, gender, year_level, course_code, age, email) VALUES (?, ?, ?, ?, ?, ?, ?)',
                           (student.id, student.name, student.gender, student.year_level,
                            student.course_code, student.age, student.email))
            self.conn.commit()

            messagebox.showinfo("Success", "Student added successfully.")
        else:
            messagebox.showwarning("Error", "Please fill in all the fields.")


    def delete_student(self):
        id = self.id_entry.get()

        if id:
            self.c.execute('DELETE FROM students WHERE id = ?', (id,))
            if self.c.rowcount > 0:
                self.conn.commit()
                messagebox.showinfo("Success", f"Student with ID {id} has been deleted.")
            else:
                messagebox.showwarning("Error", f"Student with ID {id} does not exist.")
        else:
            messagebox.showwarning("Error", "Please enter a student ID.")

    def edit_student(self):
        id = self.id_entry.get()
        new_name = self.name_entry.get()
        new_gender = self.gender_entry.get()
        new_year_level = self.year_level_entry.get()
        new_course_code = self.course_code_entry.get()

        if id and new_name and new_gender and new_year_level and new_course_code:
            self.c.execute('''
                UPDATE students
                SET name = ?, gender = ?, year_level = ?, course_code = ?
                WHERE id = ?
            ''', (new_name, new_gender, new_year_level, new_course_code, id))
            if self.c.rowcount > 0:
                self.conn.commit()
                messagebox.showinfo("Success", f"Student with ID {id} has been updated.")
            else:
                messagebox.showwarning("Error", f"Student with ID {id} does not exist.")
        else:
            messagebox.showwarning("Error", "Please fill in all fields.")

    def list_students(self):
        self.c.execute('SELECT students.id, students.name, students.gender, students.year_level, students.course_code, courses.course, age, email FROM students LEFT JOIN courses ON students.course_code = courses.code')
        students = self.c.fetchall()
        result = "List of Students:\n\n"
        for student in students:
            result += f"ID: {student[0]}\n"
            result += f"Name: {student[1]}\n"
            result += f"Gender: {student[2]}\n"
            result += f"Year Level: {student[3]}\n"
            result += f"Course Code: {student[4]}\n"
            result += f"Course: {student[5]}\n"
            result += f"Age: {student[6]}\n"
            result += f"Email: {student[7]}\n"
            result += "=====================\n"
        messagebox.showinfo("Students", result)

    def search_student(self):
        keyword = self.id_entry.get()

        if keyword:
            self.c.execute('SELECT students.id, students.name, students.gender, students.year_level, students.course_code, courses.course, age, email FROM students LEFT JOIN courses ON students.course_code = courses.code')
            student = self.c.fetchone()
            if student:
                result = "Search Results:\n\n"
                result += f"ID: {student[0]}\n"
                result += f"Name: {student[1]}\n"
                result += f"Gender: {student[2]}\n"
                result += f"Year Level: {student[3]}\n"
                result += f"Course Code: {student[4]}\n"
                result += f"Course: {student[5]}\n"
                result += f"Age: {student[6]}\n"
                result += f"Email: {student[7]}\n"
                messagebox.showinfo("Search Results", result)
            else:
                messagebox.showwarning("Error", "No student found with the provided ID.")
        else:
            messagebox.showwarning("Error", "Please enter a student ID.")

    def add_course(self):
        code = self.course_code_entry2.get()
        course = self.course_entry.get()

        if code and course:
            new_course = Course(code, course)
            self.c.execute('''
                INSERT INTO courses (code, course)
                VALUES (?, ?)
            ''', (code, course))
            self.conn.commit()
            messagebox.showinfo("Success", f"Course {course} with code {code} has been added.")
        else:
            messagebox.showwarning("Error", "Please fill in all fields.")

    def delete_course(self):
        code = self.course_code_entry2.get()

        if code:
            self.c.execute('DELETE FROM courses WHERE code = ?', (code,))
            if self.c.rowcount > 0:
                self.conn.commit()
                messagebox.showinfo("Success", f"Course with code {code} has been deleted.")
            else:
                messagebox.showwarning("Error", f"Course with code {code} does not exist.")
        else:
            messagebox.showwarning("Error", "Please enter a course code.")

    def edit_course(self):
        code = self.course_code_entry2.get()
        new_course = self.course_entry.get()

        if code and new_course:
            self.c.execute('''
                UPDATE courses
                SET course = ?
                WHERE code = ?
            ''', (new_course, code))
            if self.c.rowcount > 0:
                self.conn.commit()
                messagebox.showinfo("Success", f"Course with code {code} has been updated.")
            else:
                messagebox.showwarning("Error", f"Course with code {code} does not exist.")
        else:
            messagebox.showwarning("Error", "Please fill in all fields.")

    def list_courses(self):
        self.c.execute('SELECT * FROM courses')
        courses = self.c.fetchall()
        result = "List of Courses:\n\n"
        for course in courses:
            result += f"Code: {course[0]}\n"
            result += f"Course: {course[1]}\n"
            result += "=====================\n"
        messagebox.showinfo("Courses", result)

sis = StudentInformationSystem()
sis.root.mainloop()
conn.close()
