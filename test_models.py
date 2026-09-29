from models import Student
def test_student_to_dict():
    student = Student(1,"A",20,"M","A")
    assert student.to_dict() == {"roll_no":1,"name":"A","age":20,"gender":"M","student_class":"A"}

def test_student_from_dict():
    data = {"roll_no":1,"name":"A","age":20,"gender":"M","student_class":"A"}
    student = Student.from_dict(data)
    assert student.roll_no == 1
    assert student.name == "A"
    assert student.age == 20
    assert student.gender == "M"
    assert student.student_class == "A"