from storage import load_students, save_students
from models import Student
students = load_students()

def is_valid_age(age):
    return 0 < age <= 30

def get_valid_age():
    while True:
        try:
            age = int(input("Enter student age: "))
            if is_valid_age(age):
                return age
            print("Age must be between 1 and 30!")
        except ValueError:
            print("Invalid age!")

def is_unique_roll_no(roll_no):
    for student in students:
        if roll_no == student.roll_no:
            return False
    return True

def get_valid_roll_no():
    while True:
        try:
            roll_no = int(input("Enter student roll number: "))
            if is_unique_roll_no(roll_no):
                return roll_no
            else:
                print("Roll number must not be duplicated!")
        except ValueError:
            print("Invalid roll number!")

def add_student():
    roll_no = get_valid_roll_no()
    name = input("Enter student name: ")
    age = get_valid_age()
    gender = input("Enter student gender: ")
    student_class = input("Enter student class: ")
    student = Student( roll_no, name, age, gender, student_class )
    students.append(student)
    save_students(students)
    print("Student added successfully!")

def display_students(student_list):
    if not student_list:
        print("Student list empty!")
    else:
        print("Student list:")
        for student in student_list:
            print("-" * 40)
            print(f"Roll Number : {student.roll_no}")
            print(f"Name        : {student.name}")
            print(f"Age         : {student.age}")
            print(f"Gender      : {student.gender}")
            print(f"Class       : {student.student_class}")
            print("-" * 40)

def view_students():
    display_students(students)

def view_students_by_class():
    student_class = input("Enter student class: ")
    stu = [ student for student in students if student.student_class == student_class ]
    display_students(stu)

def delete_student():
    if not students:
        print("Student list empty!")
    else:
        try:
            remove = int(input("Enter student Roll number to remove: "))
        except ValueError:
            print("Invalid Roll number!")
            return
        found = False
        for student in students:
            if student.roll_no == remove:
                students.remove(student)
                save_students(students)
                found = True
                print("Student deleted successfully!")
                break
        if not found:
            print("Student not found!")

def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. View Student By Class")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            view_students_by_class()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()