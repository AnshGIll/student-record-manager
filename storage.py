import json
from json import JSONDecodeError
from pathlib import Path
from models import Student

DATA_FILE = Path("students.json")


def load_students():
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE,"r", encoding="utf-8") as file:
            data = json.load(file)
        students = [Student.from_dict(student) for student in data]
        return students
    except (JSONDecodeError, OSError):
        return []


def save_students(students):
    try:
        with open(DATA_FILE,"w", encoding="utf-8") as file:
            data = [student.to_dict() for student in students]
            json.dump(data, file, indent=4)
    except OSError as e:
        print(f"Error saving students: {e}")