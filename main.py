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

def is_unique_roll_number(roll_number):
    for student in students:
        if roll_number == student.roll_number:
            return False

    return True
def get_valid_roll_number():
    while True:
        try:
            roll_number = int(input("Enter student roll number: "))
            if is_unique_roll_number(roll_number):
                return roll_number
            else:
                print("Roll number must not be duplicated!")
        except ValueError:
            print("Invalid roll number!")

def add_student():
    name = input("Enter student name: ")
    age = get_valid_age()
    gender = input("Enter student gender: ")
    student_class = input("Enter student class: ")
    roll_number = get_valid_roll_number()
    student = Student(name, age, gender, student_class, roll_number)
    students.append(student)
    save_students(students)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No Student records found!")
    else:
        print("Student list:")
        for student in students:
            print("-" * 40)
            print(f"Roll Number : {student.roll_number}")
            print(f"Name        : {student.name}")
            print(f"Age         : {student.age}")
            print(f"Gender      : {student.gender}")
            print(f"Class       : {student.student_class}")
            print("-" * 40)

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
            if student.roll_number == remove:
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
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
