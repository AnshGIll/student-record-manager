class Student:
    def __init__(self,roll_no,name,age,gender,student_class):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.student_class = student_class

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["roll_no"],
            data["name"],
            data["age"],
            data["gender"],
            data["student_class"]
        )

        Student.from_dict(data)