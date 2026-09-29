from dataclasses import dataclass

@dataclass
class Student:
    roll_no : int
    name : str
    age : int
    gender : str
    student_class : str

    def to_dict(self)->dict:
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "student_class": self.student_class
        }


    @classmethod
    def from_dict(cls, data:dict)-> "Student":
        return cls(
            data["roll_no"],
            data["name"],
            data["age"],
            data["gender"],
            data["student_class"]
        )
