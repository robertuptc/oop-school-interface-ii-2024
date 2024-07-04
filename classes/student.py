import csv
from .user import User

class Student(User):
    @classmethod
    def load_all_students(cls):
        all_students = []
        # because this is getting run from runner.py
        with open('./data/students.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_student = cls(**row)
                all_students.append(new_student)
        return all_students


    def __init__(self, name, age, school_id, password, role="Student"):
        super().__init__(name, age, school_id, password, role)


    @property
    def school_id(self):
        return self.id
    
    @school_id.setter
    def school_id(self, new_id):
        self.id = new_id




    # @property
    # def get_name(self):
    #     return self.name

    # @get_name.setter
    # def set_name(self, new_name):
    #     if type(new_name) is str:
    #         self.name = new_name
    #     else:
    #         print("Name must be a string")

    # def __repr__(self):
    #     return f"{self.name} | {self.age} | {self.role}"