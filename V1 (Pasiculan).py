class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.enrolled_students = []

class StudentInformationSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, id, name):
        student = Student(id, name)
        self.students.append(student)
        print(f"Student {name} with ID {id} has been added.")

    def delete_student(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                print(f"Student with ID {id} has been deleted.")
                return
        print(f"Student with ID {id} does not exist.")

    def edit_student(self, id, new_name):
        for student in self.students:
            if student.id == id:
                student.name = new_name
                print(f"Student with ID {id} has been updated.")
                return
        print(f"Student with ID {id} does not exist.")

    def list_students(self):
        print("List of Students:")
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}")

    def search_student(self, keyword):
        print("Search Results:")
        for student in self.students:
            if keyword.lower() in student.name.lower():
                print(f"ID: {student.id}, Name: {student.name}")

    def add_course(self, id, name):
        course = Course(id, name)
        self.courses.append(course)
        print(f"Course {name} with ID {id} has been added.")

    def delete_course(self, id):
        for course in self.courses:
            if course.id == id:
                self.courses.remove(course)
                print(f"Course with ID {id} has been deleted.")
                return
        print(f"Course with ID {id} does not exist.")

    def edit_course(self, id, new_name):
        for course in self.courses:
            if course.id == id:
                course.name = new_name
                print(f"Course with ID {id} has been updated.")
                return
        print(f"Course with ID {id} does not exist.")

    def list_courses(self):
        print("List of Courses:")
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}")

    def search_course(self, keyword):
        print("Search Results:")
        for course in self.courses:
            if keyword.lower() in course.name.lower():
                print(f"ID: {course.id}, Name: {course.name}")

    def enroll_student(self, student_id, course_id):
        student = None
        course = None

        for s in self.students:
            if s.id == student_id:
                student = s
                break

        for c in self.courses:
            if c.id == course_id:
                course = c
                break

        if student is None:
            print(f"Student with ID {student_id} does not exist.")
        elif course is None:
            print(f"Course with ID {course_id} does not exist.")
        else:
            if student in course.enrolled_students:
                print(f"Student with ID {student_id} is already enrolled in the course {course.name}.")
            else:
                course.enrolled_students.append(student)
                print(f"Student with ID {student_id} has been enrolled in the course {course.name}.")

    def list_enrolled_students(self, course_id):
        course = None

        for c in self.courses:
            if c.id == course_id:
                course = c
                break

        if course is None:
            print(f"Course with ID {course_id} does not exist.")
        else:
            print(f"Enrolled Students in Course {course.name}:")
            for student in course.enrolled_students:
                print(f"ID: {student.id}, Name: {student.name}")


# Usage example
sis = StudentInformationSystem()

while True:
    print("\n==== Student Information System ====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Edit Student")
    print("4. List Students")
    print("5. Search Student")
    print("6. Add Course")
    print("7. Delete Course")
    print("8. Edit Course")
    print("9. List Courses")
    print("10. Search Course")
    print("11. Enroll Student in Course")
    print("12. List Enrolled Students in Course")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        break

    if choice == 1:
        id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        sis.add_student(id, name)

    elif choice == 2:
        id = int(input("Enter student ID: "))
        sis.delete_student(id)

    elif choice == 3:
        id = int(input("Enter student ID: "))
        new_name = input("Enter new student name: ")
        sis.edit_student(id, new_name)

    elif choice == 4:
        sis.list_students()

    elif choice == 5:
        keyword = input("Enter search keyword: ")
        sis.search_student(keyword)

    elif choice == 6:
        id = int(input("Enter course ID: "))
        name = input("Enter course name: ")
        sis.add_course(id, name)

    elif choice == 7:
        id = int(input("Enter course ID: "))
        sis.delete_course(id)

    elif choice == 8:
        id = int(input("Enter course ID: "))
        new_name = input("Enter new course name: ")
        sis.edit_course(id, new_name)

    elif choice == 9:
        sis.list_courses()

    elif choice == 10:
        keyword = input("Enter search keyword: ")
        sis.search_course(keyword)

    elif choice == 11:
        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        sis.enroll_student(student_id, course_id)

    elif choice == 12:
        course_id = int(input("Enter course ID: "))
        sis.list_enrolled_students(course_id)

    else:
        print("Invalid choice. Please try again.")
